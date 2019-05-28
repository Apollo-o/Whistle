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
    return links

url = "https://www.tacoma.uw.edu/"

links = link_crawler(url)
print("\n".join(links))

##links = link_crawler(links[50])
##print("\n".join(links))


http(s)://my.uw.edu
(https://www.tacoma.uw.edu)/node/3904
(https://www.tacoma.uw.edu/)#global-secondary
\\u0022#\\u0022
