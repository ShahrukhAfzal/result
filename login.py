#!/home/shah/yes/bin/python


print("Content-Type: text/html")
print()

import cgi
form = cgi.FieldStorage()

user_name = form.getvalue("user")
pwd = form.getvalue("pwd")

#print(user_name,'---',pwd)
import mysql.connector

con = mysql.connector.connect(user='root',password='',host='localhost',database='result_demo')
cur = con.cursor()

cur.execute("SELECT USERNAME,DECODE(PASSWORD,'secret') FROM user where USERNAME=%s and DECODE(PASSWORD,'secret')=%s ",(user_name,pwd))
z=cur.fetchall()

if z!=[]:
    print("<br><br><h1>Successful logged in</h1>")
    redirectURL = "enter_url.html"
    print('<html>')
    print('  <head>')
    print('    <meta http-equiv="refresh" content="0;url=' + str(redirectURL) + '" />')
    print('  </head>')
    print('</html>')

else:
    print("<br><br><center><h1>!!!  No such user  !!!</h1></center>")


print("connection succes")


con.commit()
cur.close()
con.close()

print("connection close")