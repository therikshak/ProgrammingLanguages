#!/usr/bin/env python3

import cgi
import cgitb
import re

# ENABLE CGI 
# This line will result in Python syntax errors displayed in browser
cgitb.enable()

print("Content-Type: text/html")

# give a name to your cgi.FieldStorage()
parmObj = cgi.FieldStorage()

# FIND a particular key and value
lookForKey = 'phone'
if 'phone' in parmObj:
    check_value = parmObj.getvalue(lookForKey)
    re_s = re.search(r"([0-9]{3})([-.]?)([0-9]{3})\2([0-9]{4})", check_value)
    if re_s is None:
        print("<p>" + "Improper Format for {}".format(check_value) + "</p>")
    else:
        print("<h2>" + "{}{}{}".format(re_s.group(1), re_s.group(3), re_s.group(4)) + "</h2>")
else:
    print("Missing Parameter:" + lookForKey)
