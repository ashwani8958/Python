#expect user input data

import sqlite3

#connect to database
MySchool = sqlite3.connect('schooltest.db')

#create cursor
curschool = MySchool.cursor()

#Ask the user to input data
my_id = int(input("Enter the Student ID: -  "))
my_name = input("Enter the Student Name: - ")
my_age = int(input("Enter the Student age: -"))
my_marks = float(input("Enter the Student marks: - "))

#put value in the table
#curschool.execute(''' INSERT INTO Student(StudentID, Name, Age, Marks)
 #VALUES (my_id, my_name, my_age, my_marks);''')

curschool.execute("INSERT INTO Student (StudentID, Name, Age, Marks) VALUES (?,?,?,?);", (my_id,my_name,my_age,my_marks))

#commit te changes
MySchool.commit()

#close the connect
MySchool.close()
