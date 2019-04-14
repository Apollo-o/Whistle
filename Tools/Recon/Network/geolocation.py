# AUTHOR: o-o
# DATE: 1/14/2019
# TIME: 12:04
import json
import requests


# A Simple Geolocation Program.
# Precondition: Two Strings.
# Postcondition: Returns Geolocation Data.
# EX: getGeolocation("192.168.0.1","x0xx00x0x00x0xxx")
def getGeolocation(ip_address, access_key):
    # Local Variables.
    address = str(ip_address)
    key = str(access_key)

    # Sends Request | Receives Status Code (200) | Converts Data to Text.
    send_url = "http://api.ipstack.com/%s?access_key=%s" % (address, key)
    received = requests.get(send_url)
    dict_data = json.loads(received.text)

    # Formats Device Data.
    string_data = "Location:\n\n"
    string_dict_data = ""
    j = 0
    for i in dict_data:
        if "location" not in i:
            string_data += i + ": " + str(dict_data[i]) + "\n"
        else:
            if j == 0:
                string_data += "\n"
                j += 1
            string_dict_data += str(dict_data[i])

    # Creates a new list.
    list_data = string_dict_data.strip().split(",")

    # Formats Country Data.
    location_string = ""
    for i in list_data:
        new_list = i.split("'")
        location_string += str(new_list[1])
        location_string += str(new_list[-1]) + ": "
        value2 = str(new_list[3:4])
        location_string += str(value2[2:-2]) + "\n"
    # Stores Geolocation.
    file = open("Geolocation.pgp", "w")
    temp = (str(string_data.encode("utf-8")) + str(location_string.encode("utf-8"))).split("\\n")
    for element in temp:
        file.write(element + "\n")
    file.close()

getGeolocation("", "")
