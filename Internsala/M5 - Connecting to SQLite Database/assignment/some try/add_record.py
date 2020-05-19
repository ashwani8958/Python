"This function will add Record in the database"

import sqlite3
import re



def new_record():

    #Loop to check for valid Book ID
    while True:
        book_id = input("Enter the Book ID :- ")
        try:
            book_id = int(book_id)
            break
        except:
            print("Enter the Valid Book ID!! Book ID should be numberical")

    #Loop to check for valid Title
    while True:
        title = input("Enter the Book title :- ")
        if re.search('''[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0-9]''',title):
            print("Invalid!! Please enter the valid Title.")
        else:
            break
            
  
    #Loop to check for valid author
    while True:
        author = input("Enter the Author Name :- ")
        if re.search('''[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0-9]''', author):
            print("Invalid!! Please enter the valid Author.")
        else:
            break
        
    #loop to check for valid Price
    while True:
        price = input("Enter the price :- ")
        try:
            price = float(price)
            break
        except:
            print("Enter the Valid price!!")


    #Add record to the Database

    #Create database or connect to existing database
    MyLibrary = sqlite3.connect('Library.db')

    #create a cursor object
    curslibrary = MyLibrary.cursor()

    

    #check for table in the database and return the list of the table, if no table present in the database the list is empty
    #if len(curslibrary.fetchall()) == 0:
        #print(len(curslibrary.fetchall()))
    try:
        curslibrary.execute('CREATE TABLE Bookdetails(Book_id INTEGER PRIMARY KEY, Title TEXT(25) NOT NULL, Author TEXT(30) NOT NULL, Price REAL NOT NULL);')
        curslibrary.execute('INSERT INTO Bookdetails(Book_id, Title, Author, Price) VALUES (?, ?, ?, ?);', (book_id, title, author, price))
        MyLibrary.commit()
        
    except:
        curslibrary.execute('INSERT INTO Bookdetails(Book_id, Title, Author, Price) VALUES (?, ?, ?, ?);', (book_id, title, author, price))
        MyLibrary.commit()

        
    #Search for 'Bookdetails' table only in the database
    #result = curslibrary.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = 'Bookdetails';")

    #for name in result:
        #if name[0] == 'Bookdetails':
            #try:
                #curslibrary.execute('INSERT INTO Bookdetails(Book_id, Title, Author, Price) VALUES (?, ?, ?, ?);', (book_id, title, author, price))
                #MyLibrary.commit()
                #print("Value added in the table")

            #except:
                #curslibrary.execute('CREATE TABLE Bookdetails(Book_id INTEGER PRIMARY KEY, Title TEXT(25) NOT NULL, Author TEXT(30) NOT NULL, Price REAL NOT NULL);')

                
                
