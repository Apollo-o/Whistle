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
        links = link_formatter(url,links)
        print(len(links))
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
            temp.append(link)
        elif "http" in link:
            temp.append(link[:4] + "s" + link[4:])
        elif link[0] == "/" or link[0] == "#":
            temp.append(url + link)
        else:
            print(link)
    print(len(links))
    return temp

# Start Program.
# Precondition: A String.
# Postcondition: Files.
def main():
    # Homepage Links.
    url   = "https://www.tacoma.uw.edu"
    links = link_crawler(url)

    # Crawl Entire Site.
    for link in links:
        links = link_crawler(link)
main()
