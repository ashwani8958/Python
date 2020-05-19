# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginAtMyPC(object):
    def chkPassword(self):
        txt=self.lineEdit_2.text()
        if txt=='ashwani':
            print ('Valid password')
        else:
            print ('Invalid password')


    def setupUi(self, LoginAtMyPC):
        LoginAtMyPC.setObjectName("LoginAtMyPC")
        LoginAtMyPC.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(LoginAtMyPC)
        self.centralwidget.setObjectName("centralwidget")
        self.OK_Button = QtWidgets.QPushButton(self.centralwidget)
        self.OK_Button.setGeometry(QtCore.QRect(50, 230, 99, 27))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OK_Button.setFont(font)
        self.OK_Button.setObjectName("OK_Button")
        self.Reset_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_Button.setGeometry(QtCore.QRect(220, 230, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Reset_Button.setFont(font)
        self.Reset_Button.setObjectName("Reset_Button")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 100, 201, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 100, 68, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 68, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 140, 201, 27))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        LoginAtMyPC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginAtMyPC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName("menubar")
        LoginAtMyPC.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginAtMyPC)
        self.statusbar.setObjectName("statusbar")
        LoginAtMyPC.setStatusBar(self.statusbar)

        self.retranslateUi(LoginAtMyPC)
        self.Reset_Button.clicked.connect(self.lineEdit.clear)
        self.Reset_Button.clicked.connect(self.lineEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(LoginAtMyPC)

        self.OK_Button.clicked.connect(self.chkPassword)

    def retranslateUi(self, LoginAtMyPC):
        _translate = QtCore.QCoreApplication.translate
        LoginAtMyPC.setWindowTitle(_translate("LoginAtMyPC", "MainWindow"))
        self.OK_Button.setText(_translate("LoginAtMyPC", "OK"))
        self.Reset_Button.setText(_translate("LoginAtMyPC", "Reset"))
        self.label.setText(_translate("LoginAtMyPC", "Email"))
        self.label_2.setText(_translate("LoginAtMyPC", "Password"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginAtMyPC = QtWidgets.QMainWindow()
    ui = Ui_LoginAtMyPC()
    ui.setupUi(LoginAtMyPC)
    LoginAtMyPC.show()
    sys.exit(app.exec_())
