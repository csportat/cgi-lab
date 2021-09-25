#!/usr/bin/env python3
import os, json
from templates import login_page, secret_page, after_login_incorrect
import secret

print('Content-type:text/html\r\n\r\n')
print
print('<title>Test CGI</title>')
print('<p>Hello world.</p>')


# Q1 
#print(os.environ)
json_object = json.dumps(dict(os.environ), indent=4)
print(json_object)


# Q2 
for p in os.environ.keys():
    if (p == 'QUERY_STRING'):
        print( '<b>%20s</b>: %s<br>' % (p, os.environ[p]) )


# Q3 
for p in os.environ.keys():
    if (p == 'HTTP_USER_AGENT'):
        print( '<b>%20s</b>: %s<br>' % (p, os.environ[p]) )


print(login_page())
