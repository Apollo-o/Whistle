# AUTHOR: o-o
# DATE: 1/14/2019
# TIME: 12:04

import os
import socket

# Starts the Program.
# Precondition: String & List.
# Postcondition: Save Information.
# EX: runNetwork("192.168.0.1", [21,23,80])
def runNetwork(remote_ip, port_list):

    for port in port_list:
        network(remote_ip,port)

# A Simple Client to Server Connection.
# Precondition: String & Integer.
# Postcondition: Saves Returned Data.
# EX: runNetwork("192.168.0.1", 80)
def network(remote_ip, port_number):

    # Local Variables.
    host = remote_ip
    port = port_number

    # Client >> Server : Establish Connection.
    try:

        # Create Socket Object ======================================
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Attempt To Connect ========================================
        server.connect((host, port))

        # Request HTTP Status Code ==================================
        get_status_code = b"GET / HTTP/1.1\r\n\r\n"
        try:
            server.sendall(get_status_code)
        except socket.error:
            quit()

        # Receive Data ==============================================
        data = str(server.recv(3000)).split("\\r\\n")

        # Save Data =================================================
        banner = open("banner.pgp","w")
        banner.write("\n")
        for element in data:
            banner.write(element + "\n")
        banner.write("\n" + "_" * 65 + "\n")

        # Close Network =============================================
        banner.close()
        server.close()

    # ERROR: Raise Exception.
    except Exception as e:
        print(str(e) + "\n")
