import requests
import re

def search(raw_url):

  try:

    user_agent    = {"User-Agent" : \
                    "Mozilla/5.0 (X11; Linux x86_64)\
                     AppleWebKit/536.5 (KHTML, like Gecko)\
                     Chrome/19.0.1084.9 Safari/536.5"}

    raw_url       = raw_url.split(":")
    base_url,port = "{}://{}".format(raw_url[0],raw_url[1][2:]), ":" + raw_url[2]

    if requests.get(base_url + port, headers= user_agent).status_code == 200:

      save    = open("Directories.txt","w") 
      save.write("\nScan Website: {}\n\n".format(base_url))
      del raw_url, port

      reader  = open("Paths.txt","r")
      paths   = tuple(reader.read().split("\n"))
      reader.close()

      for path in paths:

        request   = base_url + "/" + path
        response  = requests.get(request, headers = user_agent)
        title     = str(re.findall(r'<title.*?>(.+?)</title>',str(response.content)))

        if title:
          if response.status_code == 200 and title.find("404") == -1:
            save.write(request + "\n")

      save.close()

  except (KeyboardInterrupt, Exception) as e: print(str(e))

search("https://www.scottshotz.com.au:443")
