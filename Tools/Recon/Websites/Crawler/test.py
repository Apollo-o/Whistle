# Author: o-o
# Date: 5/28/2019
# Description: A Simple Website Crawler.

from collections import OrderedDict
import requests
import re
import webbrowser

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
        print("",end="")

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

            chmod = link.split(".")

            if "https" in link:
                temp.append(link.strip())
            elif "http" in link:
                temp.append(link[:4] + "s" + link[4:].strip())
            elif "&quot;" in link:
                data = link.split("/")
                temp.append(url + "/" + data[1])
            elif link[0] == "/" or link[0] == "#":
                temp.append(url + link.strip())
            elif link[0:3] == "../":
                temp.append(url + "/" + link.strip())
            elif chmod[-1] == "html" or chmod[-1] == "shtml":
                temp.append(url + "/" + link.strip())
            elif "/" in link:
                temp.append(url + "/" + link.strip())
            else:
                print("",end="")

        # Return Links.
        return temp

# ===================================================================

# Author: o-o
# Date: 5/28/2019
# Description: A File Writer.

# Write the Data to a File.
# Precondition: A String | A List.
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
# Precondition: A String.
# Postcondition: Write the Data to a File.
def main():

    # Storage.
    links = []

    # Homepage URL.
    try:
        url     = str(input("url:\t"))
        scan    = int(input("pages:\t"))
        nlinks  = link_crawler(url)
        nlinks  = list(OrderedDict.fromkeys(nlinks))
        print()
        
        # Crawl Entire Site.
        switch = 0
        for link in nlinks:

            data = link_crawler(link)
            if switch == scan:
                break
            elif data != None:
                links.append(data)
            switch += 1

        # Convert a Multi-dimensional to a List. 
        data = [col for rows in links for col in rows]
        data = list(OrderedDict.fromkeys(nlinks + data))

        # Formats Subdomains.
        final = []
        for line in data:

            if "///" in line:
                temp = line.split("///")
                final.append(temp[0] + "//" + temp[-1])
            elif "//" in line:
                temp = line.split("//")
                final.append(temp[0] + "//" + temp[-1])
            else:
                final.append(line)

        # Write the data to the file.
        writer("links.txt",final)

        # Open the links in the browser.
        count   = 0
        for link in final:

            if count == 5:
                count = 0
                try:
                    input(".....")
                except KeyboardInterrupt:
                    quit()

            webbrowser.open_new_tab(link)
            count += 1
        reader.close()

    except Exception as e:
        print("\nError: " + str(e))

main()
