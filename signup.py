#!/home/shah/yes/bin/python

print("Content-Type: text/HTML")
print()
import cgi

print("<center><h1>This is your sign up page</h1></center>")
print("<hr/>")


form = cgi.FieldStorage()
'''
user_name ='abcd' #
pwd = 123#
clg = 'qw'#
dept = 'ds'#
type = 222
'''
user_name=form.getvalue("user")
pwd=form.getvalue("pwd")
clg=form.getvalue("clg")
dept=form.getvalue("dept")
type=form.getvalue("type")

#print(user_name,pwd,clg,dept,type)

import mysql.connector

con = mysql.connector.connect(user='root',password='',host='localhost',database='result_demo')
cur = con.cursor()

cur.execute("INSERT INTO user(USERNAME,PASSWORD,COLLEGE,BRANCH,ROLE) values(%s,ENCODE(%s,'secret'),%s,%s,%s)",tuple(list([user_name,pwd,clg,dept,type])))

#SELECT DECODE(PASSWORD, 'secret') AS `pswd` FROM `user` WHERE COLLEGE='OTHER';


print("<html>Record successfully entered for </html>",user_name)

con.commit()
cur.close()
con.close()
print("<hr/>")
print("Connection closed")
print("<a href='home.html'>Home</a>")