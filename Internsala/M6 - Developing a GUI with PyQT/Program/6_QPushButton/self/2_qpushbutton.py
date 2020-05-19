# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1_qpushbutton.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(241, 171)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b1 = QtWidgets.QPushButton(Form)

        #For setting btn 1 as a toggle button
        self.b1.setCheckable(True)
        self.b1.toggle()

        #Use this method as slot for clicked signal emitted by b1.
        self.b1.clicked.connect(self.btnstate)

        
        self.b1.setObjectName("b1")
        self.verticalLayout.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setObjectName("b2")
        self.verticalLayout.addWidget(self.b2)
        self.b3 = QtWidgets.QPushButton(Form)
        self.b3.setObjectName("b3")
        self.verticalLayout.addWidget(self.b3)

        #link to the 'chkbtn' method
        self.b2.clicked.connect(lambda:self.chkbtn(self.b2))
        self.b3.clicked.connect(lambda:self.chkbtn(self.b3))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "PushButton"))
        self.b2.setText(_translate("Form", "Button2"))
        self.b3.setText(_translate("Form", "Button3"))
        
    #For the toggle button, to change the caption of b1 according to its state
    def btnstate(self):
        if self.b1.isChecked():
            self.b1.setText("pressed")
        else:
            self.b1.setText("released")


    #To identify which button out of b2 and b3 has been clicked. This method and connect the same to clicked signal of b2 and b3.

    def chkbtn(self,b):
        print("caption of the pressed button : ",b.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
