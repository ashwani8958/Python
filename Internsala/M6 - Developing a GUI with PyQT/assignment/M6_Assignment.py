# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M6_Assignment.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import re
import sqlite3
#from findprice import * #Import module from another file

class Ui_Library(object):
    def setupUi(self, Library):
        Library.setObjectName("Library")
        Library.resize(521, 371)
        self.verticalLayout = QtWidgets.QVBoxLayout(Library)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_book = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setBold(True)
        font.setWeight(75)
        self.lb_book.setFont(font)
        self.lb_book.setAlignment(QtCore.Qt.AlignCenter)

        #label "Book Title"
        self.lb_book.setObjectName("lb_book")
        self.horizontalLayout.addWidget(self.lb_book)
        self.t_bookname = QtWidgets.QLineEdit(Library)

        #lineText where book name will be written
        self.t_bookname.setObjectName("t_bookname")
        ###########################################################################################################################
        regexp = QtCore.QRegExp('([a-zA-Z\s]*)*')### next three line of code make sure that user will be only able to enter
        validator = QtGui.QRegExpValidator(regexp)### name of the book which contain only the alphabets
        self.t_bookname.setValidator(validator)### nothing else is allowed
        ###########################################################################################################################
        
        self.horizontalLayout.addWidget(self.t_bookname)
        self.pb_price = QtWidgets.QPushButton(Library)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setBold(True)
        font.setWeight(75)
        self.pb_price.setFont(font)

        #push button "PRICE" to find the price of book
        self.pb_price.setObjectName("pb_price")
        ######################################################################################################################
        #self.pb_price.clicked.connect(lambda : findprice()) # Connection creation when function is written as seprate module
        self.pb_price.clicked.connect(self.findprice)
        ######################################################################################################################
        self.horizontalLayout.addWidget(self.pb_price)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_price = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setBold(True)
        font.setWeight(75)
        self.lb_price.setFont(font)
        self.lb_price.setAlignment(QtCore.Qt.AlignCenter)

        #label "Price" to show the price of book after successful search
        self.lb_price.setObjectName("lb_price")
        self.horizontalLayout_2.addWidget(self.lb_price)
        self.t_price = QtWidgets.QLineEdit(Library)

        #lineText to show the price of the book
        self.t_price.setObjectName("t_price")
        self.t_price.setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.t_price)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_quantity = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setBold(True)
        font.setWeight(75)
        self.lb_quantity.setFont(font)

        #Ask user quantity of book to price
        self.lb_quantity.setObjectName("lb_quantity")
        self.horizontalLayout_3.addWidget(self.lb_quantity)
        self.t_quantity = QtWidgets.QLineEdit(Library)

        #lineText to enter the number of book required
        self.t_quantity.setObjectName("t_quantity")
        #######################################################################################################
        self.t_quantity.setValidator(QtGui.QIntValidator())###check for the enter value should be integer only
        #######################################################################################################
        self.horizontalLayout_3.addWidget(self.t_quantity)
        self.pb_total = QtWidgets.QPushButton(Library)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setBold(True)
        font.setWeight(75)
        self.pb_total.setFont(font)

        #Pushbotton to find the total price
        self.pb_total.setObjectName("pb_total")
        #########################################################################################################################################
        self.pb_total.clicked.connect(self.cal_total) #connect to the method to calculate the total amount after taking the no of book from user
        #########################################################################################################################################
        self.horizontalLayout_3.addWidget(self.pb_total)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_total = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setBold(True)
        font.setWeight(75)
        self.lb_total.setFont(font)

        #lable total price
        self.lb_total.setObjectName("lb_total")
        self.horizontalLayout_4.addWidget(self.lb_total)
        self.t_totalprice = QtWidgets.QLineEdit(Library)

        #Linetext to display the total price 
        self.t_totalprice.setObjectName("t_totalprice")
        self.horizontalLayout_4.addWidget(self.t_totalprice)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Library)
        QtCore.QMetaObject.connectSlotsByName(Library)
        
   
    def retranslateUi(self, Library):
        _translate = QtCore.QCoreApplication.translate
        Library.setWindowTitle(_translate("Library", "Form"))
        self.lb_book.setText(_translate("Library", "Book Title"))
        self.pb_price.setText(_translate("Library", "Price"))
        self.lb_price.setText(_translate("Library", "Price"))
        self.lb_quantity.setText(_translate("Library", "Quantity"))
        self.pb_total.setText(_translate("Library", "Find Total"))
        self.lb_total.setText(_translate("Library", "Total"))

#############################  method(slot) written to perform action based on the EVENT happen in GUI ##########################

######################################## START: CREATE METHOD ##################################################################        

    def create(self):
        #Create database or connect to existing database
        MyLibrary = sqlite3.connect('Library.db')

        #create a cursor object
        curslibrary = MyLibrary.cursor()
        
        #create the book list and price list to populate the database
        book_list = ["The C Programming Language", "Digital Circuit", "Basic Electronic", "Electronic Devices and Circuits"]
        price_list = [322,564,565,234]

        #index variable 
        i = 0

        #execute the Create table and Insert queries only one time when table is create then database is populate by the for loop
        try:
            curslibrary.execute('CREATE TABLE Bookdetails(Title TEXT(25) NOT NULL, Price REAL NOT NULL);')
            curslibrary.execute('INSERT INTO Bookdetails(Title, Price) VALUES (?, ?);', (book_list[i], price_list[i]))
            MyLibrary.commit()
            i = i + 1

        except:
            pass
        

        for book in book_list[i:]:
            #add the first add to the database
            curslibrary.execute('INSERT INTO Bookdetails(Title, Price) VALUES (?, ?);', (book_list[i], price_list[i]))
            MyLibrary.commit()#commit changes to the database
            i = i + 1
######################################## END: CREATE METHOD ##################################################################



######################################## START: FIND PRICE METHOD ##################################################################

    def findprice(self):

        #call the function create and populate
        self.create()
        
        #Create database or connect to existing database
        MyLibrary = sqlite3.connect('Library.db')

        #create a cursor object
        curslibrary = MyLibrary.cursor()

        #Take text written by user in the bookname widget of GUI and save in a variable
        txt = self.t_bookname.text()

        #
        sql = "SELECT * FROM Bookdetails WHERE Title = '"+txt+"';"
        
        curslibrary.execute(sql)
        
        record = curslibrary.fetchone()#fetch only the record which is matched
    

        if record != None:
            print("\nBook is available")
            print(record)
            self.t_price.setText(str(record[1]))#record is the list, it take price from Price widget of GUI and convert it into text for the display purpose

        else:
            print("\nBook that you are searching is not available")
            
######################################## END: FIND PRICE METHOD ##################################################################



######################################## START: CAL METHOD ##################################################################

    def cal_total(self):
        price = float(self.t_price.text())
        quantity = int(self.t_quantity.text())

        total_price = price * quantity

        self.t_totalprice.setText(str(total_price))#write the price in the GUI total price text line widget
        
######################################## END: CAL METHOD ##################################################################
       
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Library = QtWidgets.QWidget()
    ui = Ui_Library()
    ui.setupUi(Library)
    Library.show()
    sys.exit(app.exec_())
