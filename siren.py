# Aurhor: o-o
# Date: 8/31/2020
# Description: A simple script that finds IP Addresses.

import grequests
import random
import re

# Format IP Address.
# Precondition: A String.
# Postcondition: Return String.
def ip(ip_address):

    # Format IP Address (1)
    if ip_address.find("https") != -1:
        ip_address = ip_address.strip("https:").strip("/")
    elif ip_address.find("http") != -1:
        ip_address = ip_address.strip("http:").strip("/")

    # Format IP Address (2)
    if ip_address.find("/") != -1:
        ip_address = ip_address.split("/")[0].strip()
    if ip_address.find("www.") != -1:
        ip_address = ip_address.split("www.")[1].strip()

    # Return IP Address.
    return ip_address

# Start the Script.
# Precondition: None.
# Postcondition: Display Data.
def main():

    # Local Variables (DATA)
    header     = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3; en-US) AppleWebKit/601.3.4 (KHTML, like Gecko) Version/13.1.3 Safari/601.3.4"}
    t_errors   = ["40","50","Welcome","Test Page","Default","ERROR","Direct IP access not allowed","Site not found &middot; DreamHost",r"\xb2\xa1\xe6\x9c\x89\xe6\x89\xbe\xe5\x88\xb0\xe7\xab\x99\xe7\x82\xb9",r"\xe7\xbd\x91\xe7\xab\x99\xe8\xae\xbf\xe9\x97\xae\xe6\x8a\xa5\xe9\x94\x99"]
    c_errors   = ["40","50","is invalid","installed","error","You see this page because there is no Web site at this address.",r"\xbd\xa8\xc9\xe8\xd6\xd0"]

    # Local Variables (DISPLAY)
    color      = "\033[0;34;20m"
    default    = "\033[0;0;20m"
    spaces     = 60

    # Find 10 IP Addresses.
    min_count  = 0
    max_count  = 10
    print("{}IP ADDRESS{} {} | {}TITLE{}".format(color,default,(spaces-len("IP ADDRESS")) * " ",color,default))
    while min_count != max_count:

        # Generate 100 URLS.
        urls         = set(["http://{}.{}.{}.{}".format(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254)) for i in range(100)])

        # Find IP Addresses (HTTP)
        requests     = (grequests.get(url,headers=header,timeout=5) for url in urls)
        responses    = grequests.imap(requests, grequests.Pool(len(urls)))

        # Check IP Addresses.
        for response in responses:

            # Find Title.
            content = str(response.content)
            title   = re.findall("<title[^>]*>(.*?)</title>",content)

            # Display Data.
            if len(title) == 1 and any(error in title[0] for error in t_errors) == False:
                ip_address = ip(response.url)
                print("{} {} | {}".format(ip_address, (spaces-len(ip_address)) * " ",title[0].strip()))
                min_count += 1
            elif len(title) == 0 and any(content.find(error) == -1 for error in c_errors) == False:
                ip_address = ip(response.url)
                print("{} {} | {}".format(ip_address, (spaces-len(ip_address)) * " ",""))
                min_count += 1

            # Check Amount.
            if min_count == max_count:
                print("{}REPORT{} {} | {}{}{}".format(color,default,(spaces-len("REPORT")) * " ",color,"https://microsoft.com/en-us/wdsi/support/report-unsafe-site-guest",default))
                quit()

# Start the Script.
main()
