#!/usr/bin/env python3
import os, json, cgi, cgitb
from templates import login_page

print('Content-type:text/html\r\n\r\n')
print()
print('<html>')
print('<head>')
print('<title>Test CGI</title>')
print('</head>')
print('<body>')
print("<H1>This is my first CGI script</H1>")
print('<p>Hello world.</p>')
print('</body>')
print('</html>')


'''
# Q1 
#print(os.environ)
json_object = json.dumps(dict(os.environ), indent=4)
print(json_object)
'''

# Q2 
for p in os.environ.keys():
    if (p == 'QUERY_STRING'):
        print( '<b>%20s</b>: %s<br>' % (p, os.environ[p]) )


# Q3 
for p in os.environ.keys():
    if (p == 'HTTP_USER_AGENT'):
        print( '<b>%20s</b>: %s<br>' % (p, os.environ[p]) )


# Q4 + 
for p in os.environ.keys():
    if (p == 'HTTP_COOKIE'):
        print( '<b>%20s</b>: %s<br>' % (p, os.environ[p]) )


print( login_page() )