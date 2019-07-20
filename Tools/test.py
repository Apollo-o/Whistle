# Author: o-o
# Date: 7/20/19
# Description: A Simple Antivirus Script.

import json
import hashlib

from virus_total_apis import PublicApi as api

# Parse the data.
# Precondition: A List.
# Postcondition: A String || Prints Results.

def parse(data,sequence):

  for index in range(len(data)):
    if data[index] == "resource" and sequence == 1:
      hash_ = data[index+2]
      return hash_
    else:
      if results[index].strip(",") == "true":
        print("{}: {}".format(results[index-2].split("\"")[1],results[index]).split(",")[0])

try:
  
  # Assign the API Key.

  key       = "2539516d471d7beb6b28a720d7a25024edc0f7590d345fc747418645002ac47b"

  # Scan the file.
  
  obj       = api(key)
  response  = obj.scan_file(r"C:\Users\Apollo\Downloads\write-data-to-text-file-result.png", from_disk= True, timeout= 2)
  data      = json.dumps(response).split("\"")
  hash_     = parse(data,1)

  # Get the report.

  response  = obj.get_file_report(hash_)
  data      = json.dumps(response, sort_keys=False,).split(" ")
  parse(data,2)

except (KeyboardInterrupt, Exception) as e: print(str(e))
