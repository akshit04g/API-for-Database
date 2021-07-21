#! C:/Python39/python.exe

print("Content-Type: text/html\n")

print("Hello there")

import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',password='')
mycursor = mydb.cursor()
mycursor.execute("use southwind")
mycursor.execute("select * from products where name like 'p%'")

for i in mycursor:
    print(i)
