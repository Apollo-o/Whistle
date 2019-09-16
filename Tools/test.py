import requests
import re

request   = "https://www.washington.edu/contact/"
response  = requests.get(request)
response  = re.findall("", str(response.content))
print(response)
