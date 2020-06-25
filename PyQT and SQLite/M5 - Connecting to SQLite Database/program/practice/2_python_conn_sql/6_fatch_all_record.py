#program to fatch all the records

import sqlite3

#connect to the database
MySchool = sqlite3.connect('schooltest.db')

sql = "SELECT * FROM Student"

curschool = MySchool.cursor()

curschool.execute(sql)

result=curschool.fetchall()
for record in result:
    print (record)
