#update the existing record

import sqlite3

#open the connection to the database
MySchool = sqlite3.connect('schooltest.db')

name = input("Enter the name of student who's record has to be deleted:- ")

sql = "SELECT * FROM Student WHERE Name = '"+name+"';" # +nm+ string Concatenation

curschool = MySchool.cursor()
curschool.execute(sql)
record = curschool.fetchone()#fetch only the record which is matched
print(record)#print the record so the user can view that it is diser to modify

#Delete the record
choice = input("Do you want to delete the record?? (Y/N)")
sql="DELETE FROM Student WHERE name='"+name+"';"

if choice  == 'Y' or 'y':
    try:
        curschool.execute(sql)
        MySchool.commit()
        print ("record deleted successfully")
    except:
        print ("error in update operation")
        MySchool.rollback()

MySchool.close()
