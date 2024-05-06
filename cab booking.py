#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content.type:text/html\r\n\r\n")
print("<html>")
print("<body>")

Form=cgi.FieldStorage()
fName=Form.getvalue("Name")
fNumber=Form.getvalue("Number")
fPickup=Form.getvalue("Pickup")
fCabname=Form.getvalue("Cabname")
fDestination=Form.getvalue("Destination")
print("<center><h2>Thank You For Booking")
print("<h1>",fName,fNumber,fPickup,fCabname,fDestination,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="booking"
    )
mycursor=mydb.cursor()
sql="INSERT INTO user(Name,Number,Pickup,Cabname,Destination)VALUES(%s,%s,%s,%s,%s)";
value=(fName,fNumber,fPickup,fCabname,fDestination)
mycursor.execute(sql,value)
mydb.commit()
print("</body>")
print("</html>")