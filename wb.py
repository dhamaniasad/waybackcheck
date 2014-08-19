# Import libraries

from sys import argv as arg
import urllib2 as urllib
import requests
import json

# Submit url to wayback machine

inputurl = arg[1] # take in url as argument
wbkurl = "http://web.archive.org/save/" # wayback machine submission url
urllib.urlopen(wbkurl+inputurl) # Submit the url

# Return latest snapshot url

wbkav = "http://archive.org/wayback/available?url=" # wayback machine availability api url
wbcheck = urllib.urlopen(wbkav+inputurl) # open wayback availability url
wbcheckjson = json.load(wbcheck) # load json data
archived_snapshots = wbcheckjson['archived_snapshots']
latest_snapshot = archived_snapshots['closest']['url']
print latest_snapshot
