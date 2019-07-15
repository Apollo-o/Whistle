# AUTHOR: 0-0
# DATE: 7/5/2019
# DESCRIPTION: Scans websites for open directories.

import requests
import re

# Checks For Open Directories.
# Precondition: A String.
# Postcondition: Saves Links to File.
def search(raw_url):

  # Local Variable: User-agent
  try:

    user_agent    = {"User-Agent" : \
                    "Mozilla/5.0 (X11; Linux x86_64)\
                     AppleWebKit/536.5 (KHTML, like Gecko)\
                     Chrome/19.0.1084.9 Safari/536.5"}

    # Parses Input (Input Validation)
    raw_url       = raw_url.split(":")
    base_url,port = "{}://{}".format(raw_url[0],raw_url[1][2:]), ":" + raw_url[2]

    # Check If Valid Website.
    if requests.get(base_url + port, headers= user_agent).status_code == 200:

      # Open & Store Test Directories.
      reader  = open("Paths.txt","r")
      paths   = tuple(reader.read().split("\n"))
      reader.close()

      # Open & Write Data.
      save = open("Directories.txt","w") 
      save.write("\nScan Website: {}\n\n".format(base_url))
      del raw_url, port

      # Test & Write If Found.
      for path in paths:

        request   = base_url + "/" + path
        response  = requests.get(request, headers = user_agent)
        title     = str(re.findall(r'<title.*?>(.+?)</title>',str(response.content)))

        if title:
          if response.status_code == 200 and title.find("404") == -1: save.write(request + "\n")

      # Close the File.
      save.close()

  except (KeyboardInterrupt, Exception) as e: print(str(e))

# Runs Program.
# Precondition: "http(s)://www.example.com:PORT"
# Postcondition: Saves Found Links.
search("https://ilostmymind.com:443")
