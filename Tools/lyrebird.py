# Author: o-o
# Date: 5/28/2019
# Description: a Simple Website Crawler.

from collections import OrderedDict
import requests
import re

# Collect All Data.
# Precondition: a String.
# Postcondition: a List.
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
# Precondition: a String | a List.
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
# Description: a File Writer.

# Write the Data to a File.
# Precondition: a String | a List.
# Postcondition: Write the Data to a File.

def writer(name,data):

    # Create the File.
    with open(name,"w") as profile:

        # Write the Data to the File.
        for value in data:
            profile.write("%s\n" % (value))

    # Close the File.
    profile.close()

# ===================================================================

# Start Program.
# Precondition: a String.
# Postcondition: Write the Data to a File.
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

    # Convert a Multi-dimensional to a List.
    data = [col for rows in links for col in rows]
    data = list(OrderedDict.fromkeys(nlinks + data))

    # Write the data to the file.
    writer("links.csv", data)

main()
