#Catch an error while writing to the table
import sqlite3

#connecting to database
MySchool = sqlite3.connect('schooltest.db')

#creating a handly to make the changes in the database
curschool = MySchool.cursor()

my_id = int(input("Enter the Student ID:- "))
my_name = input("Enter the Student Name:- ")
my_age = input("Enter the Student Age:- ")
my_marks = float(input("Enter the student Marks:- "))

#try block to catch exceptions
try:
    MySchool.execute("INSERT INTO Student (StudentID, Name, Age, Marks) VALUES (?, ?, ?, ?);",(my_id, my_name, my_age, my_marks))
    MySchool.commit()
    print("One Record added succussfully")

#except block to handle exceptions
except:
    MySchool.rollback()
    print ("Error in operation.")

MySchool.close()
