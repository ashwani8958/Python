#update the existing record

import sqlite3

#open the connection to the database
MySchool = sqlite3.connect('schooltest.db')

name = input("Enter the name of student who's record has to be updated:- ")

sql = "SELECT * FROM Student WHERE Name = '"+name+"';" # +nm+ string Concatenation

curschool = MySchool.cursor()
curschool.execute(sql)
record = curschool.fetchone()#fetch only the record which is matched
print(record)#print the record so the user can view that it is diser to modify

marks = float(input("Enter the corrected marks:- "))#ask user to enter the corrected marks


sql="UPDATE student SET marks='"+str(marks)+"' WHERE name='"+name+"';"

try:
    curschool.execute(sql)
    MySchool.commit()
    print ("record updated successfully")
except:
    print ("error in update operation")
    MySchool.rollback()
