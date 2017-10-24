#!/usr/bin/env python3
#--------- the above line  -----------------------------
#          must be the first line of your server program
#          It tells the server which Python to execute.
#          For Python3 replace 'python' with 'python3'
#--------------------------------------------------------

#--------------------------------------------------------
# This code is intended to be used to jumpstart your Python
# server code. When developing your server, remove unneeded code.
# Most tasks you will need to perform are illustrated here.
# 
# GOTCHA: If you write your code in a WINDOWS editor you must
#         login via PuTTY and at cmd prompt run: DosToUnix yourprog.py 
#         If you forget this you will get: SERVER ERROR 
#---------------------------------------------------------

# IMPORT libraries here - add your favorite - remove unneeded
import cgi 
import json
import sys
import cgitb
import re

# ENABLE CGI 
# This line will result in Python syntax ERRORs displayed in browser
cgitb.enable()

# CONTENT-TYPE  HEADER
# The FIRST PRINT statement MUST be a header followed by a blank line.
# For web page display use: 
print "Content-Type: text/html\n\n"

# PARAMETERS passed in via GET or POST are stored in available via cgi.FieldStorage()
# The object returned 'acts' like a Dictionary (with k-v pairs) but is not an actual python dict
# Use methods  .keys()   and .getvalue(somekey)  and .has_key

#give a name to your cgi.FieldStorage()
parmObj = cgi.FieldStorage() 

# Iterate over ALL the incoming Paramter names(keys)
for key in parmObj.keys():
        print "<p>"
	print "key=%s value=%s" % (key, parmObj.getvalue(key)) 
	print "</p>"

# FIND a particular key and value
lookForKey = 'msg'
if (parmObj.has_key('msg')):
	print "found a msg: " + parmObj.getvalue(lookForKey)
else:
	print "no such key:" + lookForKey

#Send HTML back to the client
print "<h2>" + (str)(number_pass) + "</h2>"