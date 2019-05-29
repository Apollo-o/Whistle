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
        print(e)

# Formats Links.
# Precondition: A String | A List.
# Postcondition: A List.
def link_formatter(url,links):
    temp = []
    for link in links:
        if "https" in link:
            temp.append(link.strip())
        elif "http" in link:
            temp.append(link[:4] + "s" + link[4:].strip())
        elif link[0] == "/" or link[0] == "#":
            temp.append(url + link)
        else:
            print("",end="")

    return temp

def email_crawler(links):
    temp = [link[7:].strip() for link in links if "mailto:" in link]
    return temp

# Start Program.
# Precondition: A String.
# Postcondition: Files.
def main():
    # Homepage Links.
    url = "https://www.tacoma.uw.edu"
    rlinks = link_crawler(url)
    emails = email_crawler(rlinks)
    nlinks = link_formatter(url,rlinks)

    # Crawl Entire Site.
    for link in nlinks:
        rlinks = link_crawler(link)
        emails = email_crawler(rlinks)
        nlinks = link_formatter(url,rlinks)
        print(len(rlinks),len(nlinks),len(emails))
main()
