
import sqlite3

#insert new record
MySchool = sqlite3.connect('schooltest.db')

curschool = MySchool.cursor()

curschool.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='{Student}';''')

curschool.execute('''INSERT INTO Student(StudentID, Name, Age, Marks) VALUES
(5, 'Sherlock', 14, 50);''')

#don't forget to commit the changes to confirm them.
MySchool.commit()

#close the connection with database
MySchool.close()
