# Author: o-o
# Date: 5/28/2019
# Description: A Simple Website Crawler.

import requests
import re

# Collect All Links.
# Precondition: A String.
# Postcondition: A List.
def link_crawler(url):
    html  = requests.get(url)
    links = re.findall(r'href=[\'"]?([^\'" >]+)',str(html.content))
    print(len(links))
    links = link_formatter(url,links)
    return links

def link_formatter(url,links):
  temp = []
  for link in links:
    if "https" in link:
      temp.append(link)
    elif "http" in link:
      temp.append(link[:4] + "s" + link[4:])
    elif link[0] == "/":
      temp.append(url + link[1:])
    elif link[0] == "#":
      temp.append(url + link)
  return temp

url   = "https://www.tacoma.uw.edu/"
links = link_crawler(url)
print(len(links))
