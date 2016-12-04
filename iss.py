# ISS API
"""
import requests

req = requests.get("http://api.open-notify.org/iss-now.json?")

#print(req.status_code)
print(req.content, req.status_code)
"""

import urllib2
import json

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

print obj['timestamp']
print obj['iss_position']['latitude'], obj['data']['iss_position']['latitude']