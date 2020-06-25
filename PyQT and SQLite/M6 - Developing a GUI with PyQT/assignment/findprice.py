import sqlite3

def findprice():

    #Create database or connect to existing database
    MyLibrary = sqlite3.connect('Library.db')

    #create a cursor object
    curslibrary = MyLibrary.cursor()
    

    book_list = ["The C Programming Language", "Digital Circuit", "Basic Electronic", "Electronic Devices and Circuits"]
    price_list = [322,564,565,234]

    i = 0

    try:
        curslibrary.execute('CREATE TABLE Bookdetails(Title TEXT(25) NOT NULL, Price REAL NOT NULL);')
        curslibrary.execute('INSERT INTO Bookdetails(Title, Price) VALUES (?, ?);', (book_list[i], price_list[i]))
        MyLibrary.commit()
        i = i + 1

    except:
        pass
    

    for book in book_list[i:]:
        print("book")
        #add the first add to the database
        curslibrary.execute('INSERT INTO Bookdetails(Title, Price) VALUES (?, ?);', (book_list[i], price_list[i]))
        MyLibrary.commit()#commit changes to the database
        i = i + 1

