# Author: o-o
# Date: 5/28/2019
# Description: A Simple Website Crawler.

import requests
import re

# Collect All Data.
# Precondition: A String.
# Postcondition: A List.
def link_crawler(url):
    try:
        html    = requests.get(url)
        rlinks  = re.findall(r'href=[\'"]?([^\'" >]+)',str(html.content))
        link_formatter(url,rlinks)
    except Exception as e:
        print(str(e))

# ===================================================================

# Formats Data.
# Precondition: A String | A List.
# Postcondition: Returns A List.
def link_formatter(url, links):
    
    temp1 = []
    temp2 = []
    if links != None:
        for link in links:
            if "https" in link:
                temp1.append(link.strip())
            elif "http" in link:
                temp1.append(link[:4] + "s" + link[4:].strip())
            elif link[0] == "/" or link[0] == "#":
                temp1.append(url + link)
            else:
                print("",end="")

        email_crawler(temp1)

        for link in temp1:
            try:
                html    = requests.get(link)
                title   = re.findall(r'<title[^>]*>([^<]+)</title>', str(html.content))
                heading = ""
                if len(title) >= 1:
                    line = title[-1].split(" ")
                    for element in line:
                        if element.isalpha():
                            heading += element + " "
                        else:
                            index = element.find("\\")
                            if index > -1:
                                heading += element[:index] + " "
                temp2.append(heading.strip() + "," + link.strip())
            except Exception as e:
                print(e)
        writer("links.csv",temp2)

# ===================================================================

# Parse For Emails.
# Precondition: A List.
# Postcondition: Returns A List.
def email_crawler(links):
    temp = []
    if links != None:
        temp  = [link[7:].strip() for link in links if "mailto:" in link and not("#" in link)]
        writer("emails.csv",temp)

# ===================================================================

# Author: o-o
# Date: 5/28/2019
# Description: A file writer.

# Write the data to a file.
# Precondition: A String | A List.
# Postcondition: Write the data to a file.

def writer(name,data):

    # Create the file.
    with open(name,"w") as profile:

        # Write the data to the file.
        for value in data:
            profile.write("%s\n" % (value))

    # Close the file.
    profile.close()

# ===================================================================

# Start Program.
# Precondition: A String.
# Postcondition: A CSV File.
def main():

    # Homepage Links.
    url = "https://www.github.com"
    link_crawler(url)

main()
