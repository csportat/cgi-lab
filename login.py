#!/usr/bin/env python3
import cgi, cgitb, os
from templates import login_page, secret_page, after_login_incorrect
import secret



def main(): 
    cgitb.enable()
    
    # Create instance of FieldStorage 
    form = cgi.FieldStorage()
    
    #Get data from fields 
    username = form.getvalue('username')
    password = form.getvalue('password')
    
    print('Content-type: text/html\r\n\r\n')
    print('<html>')
    print('<head>')
    print('<title>Login - CGI lab</title>')
    print('</head>')
    print('<body>')
    print('<p><b>Username</b> %s <b>password</b> %s </p>' % (username, password))
    print('</body>')
    print('</html>')
        
    print('Set-Cookie: ID = %s' % username)
    print('Set-Cookie: Password = %s' % password)
    
    if username and password:
        if username == secret.username and password == secret.password:
            page_next = secret_page(username, password)
            print(page_next)
        else:
            page_next = after_login_incorrect()
            print(page_next)

main()