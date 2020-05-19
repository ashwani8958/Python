# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combo.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 162)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t1 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t1.setFont(font)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.b1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.additem)
        self.horizontalLayout.addWidget(self.b1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.combo1 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo1.sizePolicy().hasHeightForWidth())
        self.combo1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.combo1.setFont(font)
        self.combo1.setObjectName("combo1")
        self.combo1.addItems(['C', 'C++', 'Java', 'Python'])
        self.horizontalLayout_2.addWidget(self.combo1)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.b2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.rmitem)
        self.horizontalLayout_2.addWidget(self.b2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.t2 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t2.setFont(font)
        self.t2.setObjectName("t2")
        self.verticalLayout.addWidget(self.t2)
        self.t2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "Add"))
        self.b2.setText(_translate("Form", "Remove"))
    def rmitem(self):
        indx=self.combo1.currentIndex()
        item=self.combo1.currentText()
        self.t2.setText(item+" is removed from combobox")
        self.combo1.removeItem(indx)
    def additem(self):
        self.combo1.addItem(self.t1.text())
        self.t2.setText(self.t1.text()+" is added to combobox")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

