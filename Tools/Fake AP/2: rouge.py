# Author: o-o
# Date: 3/21/2019
# Description: Rouge AP.

import os
import linux

# MONITOR MODE && GATEWAY ===========================================

# Open Tab.
linux.TIME = 1
linux.tab()

# Gets Required Data.
# Precondition: Two Strings && An Int.
# Postcondition: Returns Data.

def get_info(name,command,key):

  # Execute Command.
  linux.command(command)
  
  # Read && Store Data.
  with open(name,"r") as raw_data:
      
    # Options.
    if key == 1:
        data = [device.strip() for device in raw_data]
    elif key == 2:
        data = [gateway.strip().split(" ") for gateway in raw_data]

    # Delete File.
    raw_data.close()
    os.remove(name)

    # Return Data.
    return data

# Get Required Data.
data1 = get_info("Interface.txt","basename -a /sys/class/net/* >> Interface.txt",1)
data2 = get_info("Gateway.txt","route -n >> Gateway.txt",2)

# Close Tab.
linux.end()

# CREATE AP =========================================================

if len(data1) >= 3:

    # Local Variables.
    interface = data1[-1]
    gateway = data2[2][9]
    subgate = gateway[:11]

    # ROUTER CONFIGURATION.
    with open("hostapd.conf","w") as ap:

        ap.write("interface=%smon" % (interface))
        ap.write("\ndriver=nl80211")
        ap.write("\nssid=%s" % (essid))
        ap.write("\nhw_mode=g")
        ap.write("\nchannel=%s" % (channel))
        ap.write("\nmacaddr_acl=0")
        ap.write("\nignore_broadcast_ssid=0")
        ap.close()

    # DNS CONFIGURATION.
    with open("dnsmasq.conf","w") as dns:

        dns.write("interface=%smon" % (interface))
        dns.write("\ndhcp-range=%s.2,%s.30,255.255.255.0,12h" % (subgate,subgate))
        dns.write("\ndhcp-option=3,%s" % (gateway))
        dns.write("\ndhcp-option=6,%s" % (gateway))
        dns.write("\nserver=8.8.8.8")
        dns.write("\nlog-queries")
        dns.write("\nlog-dhcp")
        dns.write("\nlisten-address=127.0.0.1")
        dns.close()

    # Open Tab.
    linux.tab()

    # Start Monitor Mode.
    linux.TIME = 5
    linux.command("airmon-ng start %s" % (interface))    

    # Gateway | Netmask | Routing Tables
    linux.TIME = 1        
    linux.command("ifconfig %smon up %s netmask 255.255.255.0" % (interface,gateway))
    linux.command("route add -net %s.0 netmask 255.255.255.0 gw %s" % (subgate,gateway))

    # Close Tab.
    linux.end()

    # EXECUTE =======================================================

    # Start AP.
    linux.tab()
    linux.command("hostapd hostapd.conf")

    # Start DNS Server.
    linux.tab()
    linux.command("dnsmasq -C dnsmasq.conf -d")