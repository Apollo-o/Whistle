# Author: o-o
# Date: 5/28/2019
# Description: A Simple Website Crawler.

from collections import OrderedDict
import requests
import re

# Collect All Data.
# Precondition: A String.
# Postcondition: Returns a List.
def link_crawler(url):
    try:
        html    = requests.get(url, headers = {'User-Agent' : \
                                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)\
                                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                                Chrome/35.0.1916.47 Safari/537.36'})
        rlinks  = re.findall(r'href=[\'"]?([^\'" >]+)',str(html.content))
        nlinks  = link_formatter(url,rlinks)
        return nlinks
    except Exception as e:
        print(str(e))

# ===================================================================

# Formats Data.
# Precondition: A String | a List.
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

# Get Links Titles.
# Precondition: A List.
# Postcondition: Returns a List.
def link_titles(links):

    # Collet Titles.
    data = []
    if links != None:
        for link in links:
            try:
                html    = requests.get(link, headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64)\
                                                                        AppleWebKit/537.36 (KHTML, like Gecko)\
                                                                        Chrome/61.0.3163.79 Safari/537.36'})
                title   = re.findall(r'<title[^>]*>([^<]+)</title>',str(html.content))
                heading = ""
                if len(title) >= 1:
                    title = title[-1].split(" ")
                    for element in title:
                        if element.isalpha():
                            heading += element + " "
                        else:
                            index = element.find("//")
                            if index > -1:
                                heading += element[:index] + " "

                # Handles "Not Found".
                if not("Not Found" in heading):
                    data.append(heading + "," + link)

            except Exception as e:
                print(str(e))

        # Return Data.
        return data

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
    url     = "https://www.divertns.ca/"
    nlinks  = link_crawler(url)

    # Crawl Entire Site.
    for link in nlinks:
        data = link_crawler(link)
        links.append(data)

    # Convert a Multi-dimensional to a List.
    data = [col for rows in links for col in rows]
    data = list(OrderedDict.fromkeys(nlinks + data))

    # Get Links Titles.
    flinks = link_titles(data)

    # Write the data to the file.
    # writer("links.csv", data)

main()
