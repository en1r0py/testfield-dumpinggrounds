#!/usr/bin/env python
import sqlite3
import sys

print "Content-type: text/html\n\n"
mycon = sqlite3.connect("test.db")
mycursor = mycon.cursor()
mycursor.execute("SELECT * FROM fudge")
data = mycursor.fetchall()
print data
