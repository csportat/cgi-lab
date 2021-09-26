#!/usr/bin/env python3
import cgi, cgitb, os
from templates import login_page, secret_page, after_login_incorrect
import secret
import http.cookies


cookie_string = os.environ.get('HTTP_COOKIE')
#print(cookie_string)

if not cookie_string:
    form = cgi.FieldStorage()
    if len(form) >= 2:
        username = form.getvalue('username')
        password = form.getvalue('password')
        '''
        print('<html>')
        print('<head>')
        print('<title>Login - CGI lab</title>')
        print('</head>')
        print('<body>')
        print('<p><b>Username</b> %s <b>password</b> %s </p>' % (username, password))
        print('</body>')
        print('</html>')
        '''
        if username == secret.username and password == secret.password:
            print('Set-Cookie: Username=%s' % username)
            print('Set-Cookie: Password=%s' % password)
            print('Content-type:text/html\r\n\r\n')
            page_next = secret_page(username, password)
            print(page_next)
        else:
            print('Content-type:text/html\r\n\r\n')
            page_next = after_login_incorrect()
            print(page_next)
    
    else:
        print('Content-type:text/html\r\n\r\n')
        print(login_page())

else:
    cookie = http.cookies.SimpleCookie()
    cookie.load(cookie_string)
    username = cookie['Username'].value
    password = cookie['Password'].value
    if username == secret.username and password == secret.password:
        print('Set-Cookie: Username=%s' % username)
        print('Set-Cookie: Password=%s' % password)
        print('Content-type:text/html\r\n\r\n')
        page_next = secret_page(username, password)
        print(page_next)
    else:
        print('Content-type:text/html\r\n\r\n')
        page_next = after_login_incorrect()
        print(page_next)
        print('<p>Wrong information stored in the cookie; delete the cookie, then try again.</p>')
