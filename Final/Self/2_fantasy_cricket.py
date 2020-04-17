# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1_fantasy_cricket.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

cricket = sqlite3.connect('FantasyCricket.db')
curscricket = cricket.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_yourSelection = QtWidgets.QLabel(self.centralwidget)
        self.label_yourSelection.setObjectName("label_yourSelection")
        self.verticalLayout.addWidget(self.label_yourSelection)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_BAT = QtWidgets.QLabel(self.centralwidget)
        self.label_BAT.setObjectName("label_BAT")
        self.horizontalLayout_3.addWidget(self.label_BAT)
        self.lineEdit_BAT = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_BAT.setObjectName("lineEdit_BAT")
        self.horizontalLayout_3.addWidget(self.lineEdit_BAT)
        ############## MAKING LINE EDIT READ ONLY FIELD #######################
        self.lineEdit_BAT.setReadOnly(True)
        #######################################################################
        self.label_BOW = QtWidgets.QLabel(self.centralwidget)
        self.label_BOW.setObjectName("label_BOW")
        self.horizontalLayout_3.addWidget(self.label_BOW)
        self.lineEdit_BOW = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_BOW.setObjectName("lineEdit_BOW")
        self.horizontalLayout_3.addWidget(self.lineEdit_BOW)
        ############## MAKING LINE EDIT READ ONLY FIELD #######################
        self.lineEdit_BOW.setReadOnly(True)
        #######################################################################
        self.label_AR = QtWidgets.QLabel(self.centralwidget)
        self.label_AR.setObjectName("label_AR")
        self.horizontalLayout_3.addWidget(self.label_AR)
        self.lineEdit_AR = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_AR.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_AR.setFont(font)
        self.lineEdit_AR.setObjectName("lineEdit_AR")
        self.horizontalLayout_3.addWidget(self.lineEdit_AR)
        ############## MAKING LINE EDIT READ ONLY FIELD #######################
        self.lineEdit_AR.setReadOnly(True)
        #######################################################################
        self.label_WR = QtWidgets.QLabel(self.centralwidget)
        self.label_WR.setObjectName("label_WR")
        self.horizontalLayout_3.addWidget(self.label_WR)
        self.lineEdit_WK = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_WK.setObjectName("lineEdit_WK")
        self.horizontalLayout_3.addWidget(self.lineEdit_WK)
        ############## MAKING LINE EDIT READ ONLY FIELD #######################
        self.lineEdit_WK.setReadOnly(True)
        #######################################################################
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_ptAvailable = QtWidgets.QLabel(self.centralwidget)
        self.label_ptAvailable.setObjectName("label_ptAvailable")
        self.horizontalLayout_5.addWidget(self.label_ptAvailable)
        self.lineEdit_ptAvailable = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ptAvailable.setObjectName("lineEdit_ptAvailable")
        self.horizontalLayout_5.addWidget(self.lineEdit_ptAvailable)
        ############## MAKING LINE EDIT READ ONLY FIELD #######################
        self.lineEdit_ptAvailable.setReadOnly(True)
        #######################################################################
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_BAT = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_BAT.setObjectName("radioButton_BAT")
        self.horizontalLayout_4.addWidget(self.radioButton_BAT)
        self.radioButton_BOW = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_BOW.setObjectName("radioButton_BOW")
        self.horizontalLayout_4.addWidget(self.radioButton_BOW)
        self.radioButton_AR = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_AR.setObjectName("radioButton_AR")
        self.horizontalLayout_4.addWidget(self.radioButton_AR)
        self.radioButton_WK = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_WK.setObjectName("radioButton_WK")
        self.horizontalLayout_4.addWidget(self.radioButton_WK)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.listWidget_availablePlayer = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_availablePlayer.setObjectName("listWidget_availablePlayer")
        self.verticalLayout_2.addWidget(self.listWidget_availablePlayer)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_ptUsed = QtWidgets.QLabel(self.centralwidget)
        self.label_ptUsed.setObjectName("label_ptUsed")
        self.horizontalLayout_6.addWidget(self.label_ptUsed)
        self.lineEdit_ptUsed = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ptUsed.setObjectName("lineEdit_ptUsed")
        self.horizontalLayout_6.addWidget(self.lineEdit_ptUsed)
        ############## MAKING LINE EDIT READ ONLY FIELD #######################
        self.lineEdit_ptUsed.setReadOnly(True)
        #######################################################################
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_TeamName = QtWidgets.QLabel(self.centralwidget)
        self.label_TeamName.setObjectName("label_TeamName")
        self.horizontalLayout_7.addWidget(self.label_TeamName)
        self.lineEdit_TeamName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_TeamName.setObjectName("lineEdit_TeamName")
        self.horizontalLayout_7.addWidget(self.lineEdit_TeamName)
        ############## MAKING LINE EDIT READ ONLY FIELD #######################
        self.lineEdit_TeamName.setReadOnly(True)
        #######################################################################
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.listWidget_selectedPlayer = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_selectedPlayer.setObjectName("listWidget_selectedPlayer")
        self.verticalLayout_3.addWidget(self.listWidget_selectedPlayer)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        self.menuManage_Team.setObjectName("menuManage_Team")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuManage_Team.addAction(self.actionNew_Team)
        self.menuManage_Team.addAction(self.actionOPEN_Team)
        self.menuManage_Team.addAction(self.actionSAVE_Team)
        self.menuManage_Team.addAction(self.actionEVALUATE_Team)
        self.menuManage_Team.addAction(self.actionExit)
        self.menubar.addAction(self.menuManage_Team.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ############################ Variables ################################
        self.bat = 0
        self.bow = 0
        self.ar = 0
        self.wk = 0
        self.total = 1000
        self.used = 0
        self.role = ''

        ##################### Binding the method to call #######################
        self.menuManage_Team.triggered[QtWidgets.QAction].connect(self.menuaction)
        self.radioButton_BAT.toggled.connect(lambda:self.check(True))
        self.radioButton_BOW.toggled.connect(lambda:self.check(True))
        self.radioButton_AR.toggled.connect(lambda:self.check(True))
        self.radioButton_WK.toggled.connect(lambda:self.check(True))
        self.listWidget_availablePlayer.itemDoubleClicked.connect(self.addtoSelectedPlayer)
        self.listWidget_selectedPlayer.itemDoubleClicked.connect(self.addtoAvailablePlayer)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_yourSelection.setText(_translate("MainWindow", "Your Selections"))
        self.label_BAT.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.label_BOW.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.label_AR.setText(_translate("MainWindow", "All Rounders(AR)"))
        self.label_WR.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.label_ptAvailable.setText(_translate("MainWindow", "Point Available"))
        self.radioButton_BAT.setText(_translate("MainWindow", "BAT"))
        self.radioButton_BOW.setText(_translate("MainWindow", "BOW"))
        self.radioButton_AR.setText(_translate("MainWindow", "AR"))
        self.radioButton_WK.setText(_translate("MainWindow", "WK"))
        self.label_ptUsed.setText(_translate("MainWindow", "Point used"))
        self.label_TeamName.setText(_translate("MainWindow", "Team Name"))
        self.menuManage_Team.setTitle(_translate("MainWindow", "Manage Team"))
        self.actionNew_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


    ###########################################################################
    ################### USER DEFINED METHOD STARTING ##########################
    ###########################################################################

    ####################### 1. Menu section Method ############################
    def menuaction(self, action):
        txt = action.text()

        if txt == "NEW Team":
            self.bat = 0
            self.bow = 0
            self.ar = 0
            self.wk = 0
            self.total = 1000
            self.used = 0
            self.listWidget_availablePlayer.clear()
            self.listWidget_selectedPlayer.clear()
            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")
            if ok:
                self.lineEdit_TeamName.setText(str(text))

            self.populate()

        if txt == "SAVE Team":
            counts = self.listWidget_selectedPlayer.count()
            if counts == 11:
                team  = ''
                for count in range(counts):
                    team += self.listWidget_selectedPlayer.item(count).text()
                    if count < counts:
                        team += ','
                self.saveteam(self.lineEdit_TeamName.text(), team, self.used)

            else:
                self.showmsgbox("Number of should be equal to 11")


        if txt == "OPEN Team":
            self.bat = 0
            self.bow = 0
            self.ar = 0
            self.wk = 0
            self.listWidget_selectedPlayer.clear()
            self.listWidget_availablePlayer.clear()
            self.openteam()

        if txt == "EVALUATE Team":
            from evaluate import Ui_Form
            self.window = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.window)
            self.window.show()

    #################### End of Menu Section method ###########################


    ##################################### 2. Radio Button check method ###############################################
    def check(self, flag): #Flag is used, as method is called only for checking the role that time method fill will not be called
        if self.radioButton_BAT.isChecked():
            self.role = 'BAT'
        if self.radioButton_BOW.isChecked():
            self.role = 'BOW'
        if self.radioButton_AR.isChecked():
            self.role = 'AR'
        if self.radioButton_WK.isChecked():
            self.role = 'WK'

        if flag == True:
            self.fill(self.role) #call the Method to fill the list based on the role
    ##################################### End of Radio Button Check Method ##########################################

    ################################## 3. Fill the list based on the role of the players ############################
    def fill(self, role):
        # If no team name is mentioned then prompt the user to enter team Name
        # or open Saved team
        if self.lineEdit_TeamName.text() == "":
            self.showmsgbox("Enter name of team")
            return

        self.listWidget_availablePlayer.clear() #Clear the list

        #Populate the list based on the radio button selected
        sql = "SELECT Player FROM Stats WHERE CTG = '"+role+"';"
        players = curscricket.execute(sql)
        for player in players:
            self.listWidget_availablePlayer.addItem(player[0])
    ###################################### End of Fill Method ###################################################

    ######################################## 4. Add to Selected player Method ####################################
    def addtoSelectedPlayer(self, item):
        #check role of the each player based on the radio button selected
        self.check(False)
        flag = self.chkCriteria(self.role, item)

        if True:
            self.listWidget_availablePlayer.takeItem(self.listWidget_availablePlayer.row(item))
            self.listWidget_selectedPlayer.addItem(item.text())
            self.populate()
    ######################################### End ADD to selected player METHOD ##################################

    ################################## 5. Add to Available player Method ##########################################
    def addtoAvailablePlayer(self, item):
        #To find the name of the player clicked
        self.listWidget_selectedPlayer.takeItem(self.listWidget_selectedPlayer.row(item))

        sql = "SELECT Player, Value, Ctg FROM Stats WHERE Player = '"+item.text()+"';"
        details = curscricket.execute(sql)
        detail = details.fetchone()
        self.total += int(detail[1])
        self.used -= int(detail[1])

        role = str(detail[2])
        if role == "BAT":
            self.bat -= 1
            if self.radioButton_BAT.isChecked():
                self.listWidget_availablePlayer.addItem(item.text())
        if role == "BOW":
            self.bow -= 1
            if self.radioButton_BOW.isChecked():
                self.listWidget_availablePlayer.addItem(item.text())
        if role == "AR":
            self.ar -= 1
            if self.radioButton_AR.isChecked():
                self.listWidget_availablePlayer.addItem(item.text())
        if role == "WK":
            self.wk -= 1
            if self.radioButton_WK.isChecked():
                self.listWidget_availablePlayer.addItem(item.text())
        self.populate()
    ###################################### End ADD to Available player METHOD #####################################

    ########################################### 6. Populate METHOD #################################################
    def populate(self):
        self.lineEdit_BAT.setText(str(self.bat))
        self.lineEdit_BOW.setText(str(self.bow))
        self.lineEdit_AR.setText(str(self.ar))
        self.lineEdit_WK.setText(str(self.wk))
        self.lineEdit_ptAvailable.setText(str(self.total))
        self.lineEdit_ptUsed.setText(str(self.used))
    ############################################## end populate method ################################################

    ######################################### 7. Check Criteria of slection of players ################################
    def chkCriteria(self, role, player):
        errormsg = ""
        if role == 'BAT' and self.bat >= 5:
            errormsg = "BATSMEN can't be more than 5"
        if role == 'BOW' and self.bow >= 5:
            errormsg = "BOWLERS can't be more than 5"
        if role == "AR" and self.ar >= 3:
            errormsg = "Allrounders can't be more than 3"
        if role == "WK" and self.wk > 1:
            errormsg = "Wicketkeeper can't be more the 1"

        if errormsg != "":
            self.showmsgbox(errormsg)
            return False

        if (self.total <= 0) or (self.used >= 1000):
            errormsg = "You Have Exhausted your Points"
            self.showmsgbox(errormsg)
            return False

        if role == "BAT":
            self.bat += 1
        if role == "BOW":
            self.bow += 1
        if role == "AR":
            self.ar += 1
        if role == "WK":
            self.wk += 1


        sql = "SELECT Value FROM Stats WHERE Player = '"+player.text()+"';"
        values = curscricket.execute(sql)
        value = values.fetchone()
        self.total -= int(value[0])
        self.used += int(value[0])
        return True


    ########################################## End of Criteria of selection of players ################################

    ################################################ 8. SAVE TEAM METHOD ###############################################
    def saveteam(self, teamname, teammember, ptvalue):
        sql = "INSERT INTO Teams (Name, Players, Value) VALUES('"+teamname+"', '"+teammember+"', '"+str(ptvalue)+"');"

        try:
            curscricket.execute(sql)
            cricket.commit()
            self.showmsgbox("Team Saved Succesfully")
        except:
            cricket.rollback()
            self.showmsgbox("Unable to save the Team")
    ############################################### END SAVE TEAM METHOD ###############################################

    ############################################## 9. OPEN TEAM METHOD #################################################
    def openteam(self):
        sql = "SELECT Name from Teams;"
        values = curscricket.execute(sql)
        teams  = list()

        for value in values:
            teams.append(value[0])

        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Fantasy Cricket","Choose A Team",teams,0,False)
        if ok and team:
            self.lineEdit_TeamName.setText(team)

        sql1 = "SELECT Players, Value FROM Teams WHERE Name = '"+team+"';"
        values = curscricket.execute(sql1)
        value = curscricket.fetchone()

        Players = value[0].split(',')

        self.listWidget_selectedPlayer.addItems(Players)
        self.used = value[1]

        self.total = 1000 - value[1]

        counts = self.listWidget_selectedPlayer.count()

        for count in range(counts - 1):
            player = self.listWidget_selectedPlayer.item(count).text()

            sql3 = "SELECT Ctg FROM Stats WHERE Player = '"+player+"';"
            curscricket.execute(sql3)
            roles = curscricket.fetchone()

            role = roles[0]

            if role == 'BAT':
                self.bat += 1
            if role == 'BOW':
                self.bow += 1
            if role == 'AR':
                self.ar += 1
            if role == 'WK':
                self.wk += 1

            self.populate()


    ############################################### END OPEN TEAM METHOD ###############################################

    ############################## MESSAGE BOX ################################
    def showmsgbox(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Fantasy Cricket")
        ret=Dialog.exec()
    ############################## MESSAGE BOX ################################


    ###########################################################################
    ################### USER DEFINED METHOD END ##########################
    ###########################################################################




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
