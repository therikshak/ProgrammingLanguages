#!/usr/bin/env python3

import cgi
import cgitb
import re
import sys

sys.stderr = sys.stdout

# ENABLE CGI 
# This line will result in Python syntax errors displayed in browser
cgitb.enable()

print("Content-Type: text/html")
print()

# give a name to your cgi.FieldStorage()
parmObj = cgi.FieldStorage()

# FIND a particular key and value
lookForKey = 'phone'
found_key = False

for key in parmObj.keys():
    if key == lookForKey:
        check_value = parmObj.getvalue(lookForKey)
        re_s = re.search(r"([0-9]{3})([-.]?)([0-9]{3})\2([0-9]{4})", check_value)
        if re_s is None:
            print("<p>" + "Improper Format for {}".format(check_value) + "</p>")
        else:
            print("<h2>" + "{}{}{}".format(re_s.group(1), re_s.group(3), re_s.group(4)) + "</h2>")
        found_key = True

if not found_key:
    print("Missing Parameter:" + lookForKey)
