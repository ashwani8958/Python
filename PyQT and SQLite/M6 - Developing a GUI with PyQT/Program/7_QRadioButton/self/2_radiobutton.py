# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1_radiobutton.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 193)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.verticalLayout.addWidget(self.t1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.r1 = QtWidgets.QRadioButton(Form)
        self.r1.setCheckable(True)
        self.r1.setObjectName("r1")
        self.horizontalLayout.addWidget(self.r1)
        self.r2 = QtWidgets.QRadioButton(Form)
        self.r2.setCheckable(True)
        self.r2.setObjectName("r2")
        self.horizontalLayout.addWidget(self.r2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #connect this method to radio buttons.
        self.r1.toggled.connect(self.checkstate)
        self.r2.toggled.connect(self.checkstate) 


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.r1.setText(_translate("Form", "RadioButton"))
        self.r2.setText(_translate("Form", "RadioButton"))

    def checkstate(self):
        state1 = 'OFF'
        state2 = 'OFF'
        
        if self.r1.isChecked() == True:#isChecked() method is used to check the status of the button
            state1='ON'
        else:
            state1 = 'OFF'
        if self.r2.isChecked() == True:
            state2 = 'ON'
        else:
            state2 = 'OFF'

        #write the status of the radio buttons on the text line
        self.t1.setText("Button1 is {} Button2 is {}".format(state1,state2)) 
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
