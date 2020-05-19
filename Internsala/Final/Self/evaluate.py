# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3_evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import re

curscricket = sqlite3.connect('FantasyCricket.db')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(603, 509)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_teams = QtWidgets.QComboBox(Form)
        self.comboBox_teams.setObjectName("comboBox_teams")
        self.horizontalLayout.addWidget(self.comboBox_teams)

        ################################### ADDING TEAM TO THE comboBox_teams ##################################
        sql = "SELECT Name FROM TEAMS;"
        teams = curscricket.execute(sql)
        for team in teams:
            self.comboBox_teams.addItem(team[0])
        ########################################################################################################

        self.comboBox_match = QtWidgets.QComboBox(Form)
        self.comboBox_match.setObjectName("comboBox_match")
        self.horizontalLayout.addWidget(self.comboBox_match)
        self.verticalLayout.addLayout(self.horizontalLayout)

        ################################ ADDING MATCHS TO THE comboBox_match ###################################
        sql2 = "select name from sqlite_master where type = 'table';"
        tables = curscricket.execute(sql2)
        for table in tables:
            if re.match('^[M|m]atch.*', table[0]):#table name should start from Match/match
                self.comboBox_match.addItem(table[0])
        ########################################################################################################

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_players = QtWidgets.QLabel(Form)
        self.label_players.setObjectName("label_players")
        self.horizontalLayout_2.addWidget(self.label_players)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_point = QtWidgets.QLabel(Form)
        self.label_point.setObjectName("label_point")
        self.horizontalLayout_2.addWidget(self.label_point)
        self.lineEdit_totalScore = QtWidgets.QLineEdit(Form)
        self.lineEdit_totalScore.setObjectName("lineEdit_totalScore")
        self.horizontalLayout_2.addWidget(self.lineEdit_totalScore)
        ############## MAKING LINE EDIT READ ONLY FIELD #######################
        self.lineEdit_totalScore.setReadOnly(True)
        #######################################################################
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget_players = QtWidgets.QListWidget(Form)
        self.listWidget_players.setObjectName("listWidget_players")
        self.verticalLayout_3.addWidget(self.listWidget_players)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_score = QtWidgets.QListWidget(Form)
        self.listWidget_score.setObjectName("listWidget_score")
        self.verticalLayout_2.addWidget(self.listWidget_score)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

##################### Binding the method to call #######################
        self.pushButton.clicked.connect(self.evaluate)
        self.comboBox_teams.activated.connect(self.changeteam)
        self.comboBox_match.activated.connect(lambda:self.calculatescore(True))





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Evaluate the Performance of your Fantasy Team"))
        self.label_players.setText(_translate("Form", "Players"))
        self.label_point.setText(_translate("Form", "Point"))
        self.pushButton.setText(_translate("Form", "Calculate Score"))

    ################################################################################################################
    ############################################ USER DEFINED METHOD ###############################################
    ################################################################################################################

############################ 1. CHANGE THE PLAYER IN THE listWidget_players WHEN NEW TEAM IS SELECTED IN comboBox_teams ########################
    def changeteam(self):

        self.listWidget_players.clear()
        self.lineEdit_totalScore.clear()
        team = self.comboBox_teams.currentText()


        sql = "SELECT players FROM Teams WHERE Name = '"+team+"';"
        names = curscricket.execute(sql)
        name = names.fetchone()
        players = name[0].split(',')
        self.listWidget_players.addItems(players)
############################  CHANGE THE PLAYER IN THE listWidget_players WHEN NEW TEAM IS SELECTED IN comboBox_teams ########################

################# 2. CALCULATE AND FILL SCORE OF EACH PLAYER IN listWidget_score WHEN NEW MATCH IS SELECTED IN comboBox_match ##################
    def calculatescore(self, Flag):
        if Flag == True:
            self.listWidget_score.clear()
            self.lineEdit_totalScore.clear()
        team_total = 0
        team = self.comboBox_teams.currentText()
        match = self.comboBox_match.currentText()
        for i in range(self.listWidget_players.count() - 1):
            total, batscore, bowlscore, fieldscore = 0, 0, 0, 0
            player_name = self.listWidget_players.item(i).text()
            sql = "SELECT * FROM '"+match+"' WHERE Player = '"+player_name+"';"
            data = curscricket.execute(sql)
            value = data.fetchone()
            ####################### calculate batscore ############################
            batscore = int(value[1]/2)
            if batscore >= 50 and batscore <= 100:
                batscore += 5
            if batscore > 100:
                batscore += 10

            #calculate strike rate
            if value[1] > 0:
                strike_rate = value[1]/value[2]
                if strike_rate >= 80 and strike_rate <= 100:
                    batscore += 2
                if strike_rate > 100:
                     batscore += 4

            #Extra score for four and six
            if value[3] > 0:
                batscore += (value[3] * 1)
            if value[4] > 0:
                batscore += (value[4] * 2)
            ####################### calculate batscore ############################


            ####################### calculate bowlscore ############################
            bowlscore = int(value[8] * 10)
            if value[8] >= 3 and value[8] <= 5:
                bowlscore += 5
            if value[8] > 5:
                bowlscore += 10

            #calculate economy of the bowlers
            if value[7] > 0:
                eco_rate = 6 * (value[7]/value[5])
                if eco_rate <= 2:
                    bowlscore += 10
                if eco_rate > 2 and eco_rate <= 3.5:
                    bowlscore += 7
                if eco_rate > 3.5 and eco_rate <= 4.5:
                    bowlscore += 4
            ####################### calculate bowlscore ############################

            ####################### calculate fieldscore ############################
            fieldscore = (value[9] + value[10] + value[11]) * 10
            ####################### calculate fieldscore ############################

            total = batscore + bowlscore + fieldscore

            if Flag == True:
                self.listWidget_score.addItem(str(total))

            team_total = team_total + total

        return team_total

################# END CALCULATE AND FILL SCORE OF EACH PLAYER IN listWidget_score WHEN NEW MATCH IS SELECTED IN comboBox_match #####################

############################################## 3. METHOD CONNECTED TO PUSHBUTTON ################################################################
    def evaluate(self):
        team_total = 0
        team_total = self.calculatescore(False)
        self.lineEdit_totalScore.setText(str(team_total))
##############################################  METHOD CONNECTED TO PUSHBUTTON ################################################################

    ################################################################################################################
    ############################################ END OF USER DEFINED METHOD ########################################
    ################################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
