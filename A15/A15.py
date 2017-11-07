#!/usr/bin/env python3

import cgi
import json
import csv
import cgitb
import re
import sys

sys.stderr = sys.stdout

# ENABLE CGI
# This line will result in Python syntax errors displayed in browser
cgitb.enable()

print("Content-Type: text/json\n\n")

# give a name to your cgi.FieldStorage()
parmObj = cgi.FieldStorage()

# Create dictionary
data = {}
data_send = ['False', 'False', '', '', '']
area_code_key = 'p1'
phone_key = 'p2'
state = ''

# iterate over keys
for key in parmObj.keys():
    state_add = False
    good_number = False
    bad_number = False
    bad_area = False
    # check if area code in csv file
    if key == area_code_key:
        area_code = parmObj.getvalue(key)
        with open('area_codes.csv', newline='') as area_codes:
            reader = csv.reader(area_codes, delimiter=',')
            next(reader)
            for row in reader:
                if area_code in row:
                    state_add = True
                    state = row[1]
                    break
            if not state_add:
                bad_area = True
    # check if phone number is a valid format
    elif key == phone_key:
        phone_number = parmObj.getvalue(key)
        re_s = re.search(r"([0-9]{3})([-.]?)([0-9]{4})", phone_number)
        if re_s is not None:
            good_number = True
        else:
            bad_number = True

    # if allowable key then add it to the dictionary, otherwise return message
    if state_add:
        data_send[4] = state
        data_send[3] = parmObj.getvalue(key)
        data_send[1] = "True"
    elif good_number:
        data_send[2] = parmObj.getvalue(key)
        data_send[0] = "True"
    else:
        if bad_number:
            data_send[0] = "False"
            data_send[2] = parmObj.getvalue(key)
        elif bad_area:
            data_send[1] = "False"
            data_send[3] = parmObj.getvalue(key)

data['result'] = data_send
json_data = json.dumps(data)

# send json back
print(json_data)
