#!/usr/bin/env python3
"""
urlrequest.py 

Simple application that takes in a url from the command
line and prints out its response

This could be useful for submitting basic GET requests
to RESTful APIs
"""

import urllib.request
import sys

if(len(sys.argv) != 2):
	raise SystemExit("Usage: urlrequest.py <url>")

#print("Command options: ", sys.argv)
#raise SystemExit(0)

script, url = sys.argv
u = urllib.request.urlopen(url)
data = u.read()

print(data.decode("utf-8"))
