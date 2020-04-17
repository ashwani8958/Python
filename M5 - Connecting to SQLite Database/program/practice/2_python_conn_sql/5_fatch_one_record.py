#fatch one record at a time

import sqlite3

#connect to the database
MySchool = sqlite3.connect('schooltest.db')

#create the handle
curschool = MySchool.cursor()

sql = "SELECT * FROM Student;"

curschool.execute(sql)

#loop to print all the record
while True:
    record=curschool.fetchone()# will print one record at a time
    if record==None:
        break
    print (record)
