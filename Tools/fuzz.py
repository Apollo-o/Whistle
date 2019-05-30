# Author: o-o
# Date: 5/28/2019
# Description: A Simple Website Crawler.

import requests
import re

# Collect All Links.
# Precondition: A String.
# Postcondition: A List.
def link_crawler(url):
    try:
        html  = requests.get(url)
        links = re.findall(r'href=[\'"]?([^\'" >]+)',str(html.content))
        return links
    except Exception as e:
        print(str(e))

# Formats Links.
# Precondition: A String | A List.
# Postcondition: Returns A List.
def link_formatter(url,links):

    temp = []
    if links != None:
        for link in links:
            #print(link)
            if "https" in link:
                temp.append(link.strip())
            elif "http" in link:
                temp.append(link[:4] + "s" + link[4:].strip())
            elif link[0] == "/" or link[0] == "#":
                temp.append(url + link)
            else:
                print("",end="")
        return temp

# Parse For Emails.
# Precondition: A List.
# Postcondition: Returns A List.
def email_crawler(links):
    temp = []
    if links != None:
        temp = [link[7:].strip() for link in links if "mailto:" in link and not("#" in link)]
        return temp

# Start Program.
# Precondition: A String.
# Postcondition: Files.
def main():
  
    # Storage.
    email = []
    links = []

    # Homepage Links.
    url = "https://www.tacoma.uw.edu"
    rlinks = link_crawler(url)
    emails = email_crawler(rlinks)
    nlinks = link_formatter(url,rlinks)
    print("Emails: " + str(len(emails)) + "\tLinks: " + str(len(nlinks)))

main()
