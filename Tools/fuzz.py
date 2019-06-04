# Author: o-o
# Date: 5/28/2019
# Description: A Simple Website Crawler.

from collections import OrderedDict
import requests
import re

# Collect All Data.
# Precondition: A String.
# Postcondition: A List.
def link_crawler(url):
    try:
        html    = requests.get(url)
        rlinks  = re.findall(r'href=[\'"]?([^\'" >]+)',str(html.content))
        nlinks  = link_formatter(url,rlinks)
        return nlinks
    except Exception as e:
        print(str(e))

# ===================================================================

# Formats Data.
# Precondition: A String | A List.
# Postcondition: Creates File.
def link_formatter(url, links):

    # Local Variables.
    temp = []

    # Format Links.
    if links != None:
        for link in links:
            if "https" in link:
                temp.append(link.strip())
            elif "http" in link:
                temp.append(link[:4] + "s" + link[4:].strip())
            elif link[0] == "/" or link[0] == "#":
                temp.append(url + link.strip())
            else:
                print("",end="")

        # Return Links.
        return temp

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
# Postcondition: Write the data to a file.
def main():

    # Storage.
    links = []

    # Homepage URL.
    url     = "https://www.facebook.com"
    nlinks  = link_crawler(url)

    # Crawl Entire Site.
    for link in nlinks:
        data = link_crawler(link)
        links.append(data)

    print(len(list(OrderedDict.fromkeys(nlinks + links[0]))))
    #writer("links.csv",temp2)

main()
