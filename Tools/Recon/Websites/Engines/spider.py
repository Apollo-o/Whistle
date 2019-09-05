# Author: O-O
# Date: 8/5/2019
# Description: A Dork Search Engine.

# Built-in Modules.
import os

# Third-party Modules.
from collections import OrderedDict
from lxml.html import fromstring
import requests
import re

# Request the Data.
# Precondition: User Input.
# Postcondition: A List.

def dork():

    # Assign User Agent.
    user_agent = {'User-Agent':
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

    # Assign Proxy.
    proxy      = ["http","190.242.41.133:8080"]
    
    # Search Engines.
    engines    = ['https://duckduckgo.com/html/?q={}&ia=web',
                  'https://search.yahoo.com/search?p={}&fp=1&nojs=1',
                  'https://searx.me/?q={}&categories=general&language=en-US',
                  'https://www.bing.com/search?q={}',
                  'https://www.google.com/search?q={}',
                  'https://www.info.com/serp?q={}',
                  'https://www.webcrawler.com/serp?q={}']
    
    # Temporary List.
    furls = []

    # Find URLS.
    query = input("\n Query [{}] <- ".format(proxy[-1]))
    for engine in engines:
        response = requests.get(
            engine.format(query),
            headers=user_agent,
            proxies={proxy[0]:proxy[-1]})
        rurls = re.findall(r'href=[\'"]?([^\'" >]+)',
                           str(response.content))
        furls += [url for url in rurls if url.find(
            "/") != 0 and ("http" in url or "https" in url)]

    # Create HTML File.
    html(furls)
    
# Write the Data to the HTML File.
# Precondition: A List.
# Postcondition: Create's HTML File.

def html(urls):

    # Exclude Words.
    keywords = ("alexa.com",
                "blogger.com",
                "bing",
                "diction",
                "google",
                "infospace",
                "microsoft",
                "searx",
                "web.archive.org",
                "yahoo",
                "yimg")

    # Set Up the HTML Document.
    writer = open("dork.html", "w")
    writer.write("<title>o-o</title>")
    writer.write("<body a link=\"#269ccc\" vlink=\"#0a0a0a\">")

    # Format the Data.
    values = list(OrderedDict.fromkeys(sorted(urls)))
    keys  = []
    for url in values:

        tests = False
        for keyword in keywords:
            if keyword in url:
                tests = True
                break

        if not(tests):
            temp = url.split("//")[1]
            if temp.find("www.") != -1:
                keys.append(temp.split("www.")[1])
            else:
                keys.append(temp)

    keys = sorted(keys)
    for key in keys:
        for value in values:
            if key in value:
                if "web.archive.org" in value:
                    writer.write("<a href=\"https://{}\" target=\"_blank\" rel=\"noopener noreferrer\">{}</a><br>".format(value.split("//")[-1],key))
                else:
                    writer.write("<a href=\"{}\" target=\"_blank\" rel=\"noopener noreferrer\">{}</a><br>".format(value,key))
                break

    writer.write("</body>")
    writer.close()

    # Clear Tracks.
    cwd = os.getcwd()
    os.system("start "" {}\dork.html".format(cwd))
    os.system("ipconfig /flushdns")
    os.system("del /q/f/s %temp%\*")
    os.system("cls")

# Run the Program.
# Precondition: None.
# Postcondition: Returns Results.

def main():
    try:
        while True:
            dork()
        os.system("TASKKILL /F /IM py.exe")
    except (KeyboardInterrupt, Exception) as e:
        print(str(e))

# Start the Program.
main()
