import sqlite3 #import built in module

# CONNECT open connection to database or connect to the existing database
MySchool = sqlite3.connect('schooltest.db')

#cusor method of the connect method 
curschool = MySchool.cursor()

#Execute method is the cursor object to execute any query
curschool.execute('''CREATE TABLE Student(StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT (20) NOT NULL, Age INTEGER, Marks REAL);''')

#close the connection with database
MySchool.close()
