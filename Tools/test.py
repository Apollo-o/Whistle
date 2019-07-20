import json
import hashlib

from virus_total_apis import PublicApi as api

# Assign the API Key.

key      = "2539516d471d7beb6b28a720d7a25024edc0f7590d345fc747418645002ac47b"

# Load the file and encrypt it.

file     = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
encrypt  = hashlib.md5().hexdigest()

#
obj      = api(key)
response = obj.get_file_report(encrypt)
print(json.dumps(response, sort_keys=False, indent=4))
