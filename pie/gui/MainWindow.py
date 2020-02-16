# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 811)
        MainWindow.setMinimumSize(QtCore.QSize(765, 811))
        MainWindow.setMaximumSize(QtCore.QSize(765, 811))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainHorizontalLayout = QtWidgets.QHBoxLayout()
        self.mainHorizontalLayout.setObjectName("mainHorizontalLayout")
        self.leftSideVerticalLayout = QtWidgets.QVBoxLayout()
        self.leftSideVerticalLayout.setObjectName("leftSideVerticalLayout")
        self.logTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logTextEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.logTextEdit.setFont(font)
        self.logTextEdit.setMouseTracking(False)
        self.logTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.leftSideVerticalLayout.addWidget(self.logTextEdit)
        self.clearLogButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearLogButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.clearLogButton.setObjectName("clearLogButton")
        self.leftSideVerticalLayout.addWidget(self.clearLogButton)
        self.mainHorizontalLayout.addLayout(self.leftSideVerticalLayout)
        self.rightSideVLayout = QtWidgets.QVBoxLayout()
        self.rightSideVLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.rightSideVLayout.setObjectName("rightSideVLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab_widget.setObjectName("tab_widget")
        self.config_tab = QtWidgets.QWidget()
        self.config_tab.setObjectName("config_tab")
        self.layoutWidget = QtWidgets.QWidget(self.config_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 361, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelHome_System = QtWidgets.QLabel(self.layoutWidget)
        self.labelHome_System.setMaximumSize(QtCore.QSize(120, 16777215))
        self.labelHome_System.setObjectName("labelHome_System")
        self.gridLayout.addWidget(self.labelHome_System, 0, 0, 1, 1)
        self.lineEditHome_System = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHome_System.sizePolicy().hasHeightForWidth())
        self.lineEditHome_System.setSizePolicy(sizePolicy)
        self.lineEditHome_System.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEditHome_System.setObjectName("lineEditHome_System")
        self.gridLayout.addWidget(self.lineEditHome_System, 0, 1, 1, 1)
        self.pushButtonSet_Home = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSet_Home.setObjectName("pushButtonSet_Home")
        self.gridLayout.addWidget(self.pushButtonSet_Home, 0, 2, 1, 1)
        self.watchedChannelsGroupBox = QtWidgets.QGroupBox(self.config_tab)
        self.watchedChannelsGroupBox.setGeometry(QtCore.QRect(-1, 170, 361, 330))
        self.watchedChannelsGroupBox.setMinimumSize(QtCore.QSize(350, 330))
        self.watchedChannelsGroupBox.setMaximumSize(QtCore.QSize(16777215, 330))
        self.watchedChannelsGroupBox.setObjectName("watchedChannelsGroupBox")
        self.channelListWidget = QtWidgets.QListWidget(self.watchedChannelsGroupBox)
        self.channelListWidget.setGeometry(QtCore.QRect(10, 80, 341, 200))
        self.channelListWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.channelListWidget.setUniformItemSizes(True)
        self.channelListWidget.setSelectionRectVisible(True)
        self.channelListWidget.setObjectName("channelListWidget")
        self.removeChannelButton = QtWidgets.QPushButton(self.watchedChannelsGroupBox)
        self.removeChannelButton.setGeometry(QtCore.QRect(210, 280, 141, 34))
        self.removeChannelButton.setObjectName("removeChannelButton")
        self.addChannelAddButton = QtWidgets.QPushButton(self.watchedChannelsGroupBox)
        self.addChannelAddButton.setGeometry(QtCore.QRect(260, 40, 91, 34))
        self.addChannelAddButton.setObjectName("addChannelAddButton")
        self.labeldotimperium = QtWidgets.QLabel(self.watchedChannelsGroupBox)
        self.labeldotimperium.setGeometry(QtCore.QRect(170, 50, 81, 22))
        self.labeldotimperium.setObjectName("labeldotimperium")
        self.lineEditChannelAdd = QtWidgets.QLineEdit(self.watchedChannelsGroupBox)
        self.lineEditChannelAdd.setGeometry(QtCore.QRect(10, 40, 161, 36))
        self.lineEditChannelAdd.setObjectName("lineEditChannelAdd")
        self.layoutWidget1 = QtWidgets.QWidget(self.config_tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 80, 361, 79))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.alertLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.alertLayout.setContentsMargins(0, 0, 0, 0)
        self.alertLayout.setObjectName("alertLayout")
        self.labelAlertWhen = QtWidgets.QLabel(self.layoutWidget1)
        self.labelAlertWhen.setMaximumSize(QtCore.QSize(300, 20))
        self.labelAlertWhen.setObjectName("labelAlertWhen")
        self.alertLayout.addWidget(self.labelAlertWhen)
        self.horizontalSlider_AlertJumps = QtWidgets.QSlider(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.horizontalSlider_AlertJumps.setFont(font)
        self.horizontalSlider_AlertJumps.setMinimum(1)
        self.horizontalSlider_AlertJumps.setMaximum(5)
        self.horizontalSlider_AlertJumps.setPageStep(1)
        self.horizontalSlider_AlertJumps.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_AlertJumps.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_AlertJumps.setTickInterval(1)
        self.horizontalSlider_AlertJumps.setObjectName("horizontalSlider_AlertJumps")
        self.alertLayout.addWidget(self.horizontalSlider_AlertJumps)
        self.label_alertjumps = QtWidgets.QLabel(self.layoutWidget1)
        self.label_alertjumps.setText("")
        self.label_alertjumps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_alertjumps.setObjectName("label_alertjumps")
        self.alertLayout.addWidget(self.label_alertjumps)
        self.tab_widget.addTab(self.config_tab, "")
        self.advancedtab = QtWidgets.QWidget()
        self.advancedtab.setObjectName("advancedtab")
        self.layoutWidget_2 = QtWidgets.QWidget(self.advancedtab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 361, 111))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelEveLogLocation_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelEveLogLocation_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.labelEveLogLocation_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelEveLogLocation_2.setObjectName("labelEveLogLocation_2")
        self.gridLayout_2.addWidget(self.labelEveLogLocation_2, 0, 0, 1, 1)
        self.pushButtonChoose_Eve_Log_Location = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButtonChoose_Eve_Log_Location.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonChoose_Eve_Log_Location.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonChoose_Eve_Log_Location.setObjectName("pushButtonChoose_Eve_Log_Location")
        self.gridLayout_2.addWidget(self.pushButtonChoose_Eve_Log_Location, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.pushButtonChoose_alarm_Location = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButtonChoose_alarm_Location.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonChoose_alarm_Location.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonChoose_alarm_Location.setObjectName("pushButtonChoose_alarm_Location")
        self.gridLayout_2.addWidget(self.pushButtonChoose_alarm_Location, 1, 2, 1, 1)
        self.lineEdit_alarm = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_alarm.setReadOnly(True)
        self.lineEdit_alarm.setObjectName("lineEdit_alarm")
        self.gridLayout_2.addWidget(self.lineEdit_alarm, 1, 1, 1, 1)
        self.lineEditEve_Log_Location = QtWidgets.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditEve_Log_Location.sizePolicy().hasHeightForWidth())
        self.lineEditEve_Log_Location.setSizePolicy(sizePolicy)
        self.lineEditEve_Log_Location.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditEve_Log_Location.setStyleSheet("")
        self.lineEditEve_Log_Location.setReadOnly(True)
        self.lineEditEve_Log_Location.setObjectName("lineEditEve_Log_Location")
        self.gridLayout_2.addWidget(self.lineEditEve_Log_Location, 0, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.advancedtab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 140, 192, 92))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkbox_displayalerts = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkbox_displayalerts.setObjectName("checkbox_displayalerts")
        self.verticalLayout.addWidget(self.checkbox_displayalerts)
        self.checkBox_displayclear = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_displayclear.setObjectName("checkBox_displayclear")
        self.verticalLayout.addWidget(self.checkBox_displayclear)
        self.checkBox_displayall = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_displayall.setObjectName("checkBox_displayall")
        self.verticalLayout.addWidget(self.checkBox_displayall)
        self.label_6 = QtWidgets.QLabel(self.advancedtab)
        self.label_6.setGeometry(QtCore.QRect(60, 140, 91, 22))
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.advancedtab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 250, 197, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_filterclear = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_filterclear.setObjectName("checkBox_filterclear")
        self.verticalLayout_2.addWidget(self.checkBox_filterclear)
        self.checkBox_filterstatus = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_filterstatus.setObjectName("checkBox_filterstatus")
        self.verticalLayout_2.addWidget(self.checkBox_filterstatus)
        self.label_9 = QtWidgets.QLabel(self.advancedtab)
        self.label_9.setGeometry(QtCore.QRect(50, 250, 101, 22))
        self.label_9.setObjectName("label_9")
        self.tab_widget.addTab(self.advancedtab, "")
        self.zabout_tab = QtWidgets.QWidget()
        self.zabout_tab.setObjectName("zabout_tab")
        self.label = QtWidgets.QLabel(self.zabout_tab)
        self.label.setGeometry(QtCore.QRect(0, 40, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.zabout_tab)
        self.label_2.setGeometry(QtCore.QRect(110, 200, 141, 22))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.zabout_tab)
        self.label_3.setGeometry(QtCore.QRect(146, 160, 71, 22))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.zabout_tab)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 301, 301))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pie/pie.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.zabout_tab)
        self.label_7.setGeometry(QtCore.QRect(0, 80, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.zabout_tab)
        self.label_8.setGeometry(QtCore.QRect(0, 100, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tab_widget.addTab(self.zabout_tab, "")
        self.rightSideVLayout.addWidget(self.tab_widget)
        self.mainHorizontalLayout.addLayout(self.rightSideVLayout)
        self.horizontalLayout.addLayout(self.mainHorizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditHome_System, self.pushButtonSet_Home)
        MainWindow.setTabOrder(self.pushButtonSet_Home, self.horizontalSlider_AlertJumps)
        MainWindow.setTabOrder(self.horizontalSlider_AlertJumps, self.lineEditChannelAdd)
        MainWindow.setTabOrder(self.lineEditChannelAdd, self.addChannelAddButton)
        MainWindow.setTabOrder(self.addChannelAddButton, self.channelListWidget)
        MainWindow.setTabOrder(self.channelListWidget, self.removeChannelButton)
        MainWindow.setTabOrder(self.removeChannelButton, self.clearLogButton)
        MainWindow.setTabOrder(self.clearLogButton, self.lineEditEve_Log_Location)
        MainWindow.setTabOrder(self.lineEditEve_Log_Location, self.pushButtonChoose_Eve_Log_Location)
        MainWindow.setTabOrder(self.pushButtonChoose_Eve_Log_Location, self.lineEdit_alarm)
        MainWindow.setTabOrder(self.lineEdit_alarm, self.pushButtonChoose_alarm_Location)
        MainWindow.setTabOrder(self.pushButtonChoose_alarm_Location, self.checkbox_displayalerts)
        MainWindow.setTabOrder(self.checkbox_displayalerts, self.checkBox_displayclear)
        MainWindow.setTabOrder(self.checkBox_displayclear, self.checkBox_displayall)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "P.I.E. v0.9b"))
        self.clearLogButton.setText(_translate("MainWindow", "Clear Log"))
        self.labelHome_System.setText(_translate("MainWindow", "Home system:"))
        self.pushButtonSet_Home.setText(_translate("MainWindow", "Set Home"))
        self.watchedChannelsGroupBox.setTitle(_translate("MainWindow", "Watched channels"))
        self.removeChannelButton.setText(_translate("MainWindow", "Remove Channel"))
        self.addChannelAddButton.setText(_translate("MainWindow", "Add"))
        self.labeldotimperium.setText(_translate("MainWindow", ".imperium"))
        self.labelAlertWhen.setText(_translate("MainWindow", "Alert when within jumps:"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.config_tab), _translate("MainWindow", "Config"))
        self.labelEveLogLocation_2.setText(_translate("MainWindow", "Eve logs:"))
        self.pushButtonChoose_Eve_Log_Location.setText(_translate("MainWindow", "Choose..."))
        self.label_5.setText(_translate("MainWindow", "Alarm:"))
        self.pushButtonChoose_alarm_Location.setText(_translate("MainWindow", "Choose..."))
        self.checkbox_displayalerts.setText(_translate("MainWindow", "display alert details"))
        self.checkBox_displayclear.setText(_translate("MainWindow", "display clear messages"))
        self.checkBox_displayall.setText(_translate("MainWindow", "display all messages"))
        self.label_6.setText(_translate("MainWindow", "Log options:"))
        self.checkBox_filterclear.setText(_translate("MainWindow", "ignore clear messages"))
        self.checkBox_filterstatus.setText(_translate("MainWindow", "ignore status messages"))
        self.label_9.setText(_translate("MainWindow", "Filter options:"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.advancedtab), _translate("MainWindow", "Advanced"))
        self.label.setText(_translate("MainWindow", "P. I. E."))
        self.label_2.setText(_translate("MainWindow", "by Swizzles Saissore"))
        self.label_3.setText(_translate("MainWindow", "v0.9b"))
        self.label_7.setText(_translate("MainWindow", "for"))
        self.label_8.setText(_translate("MainWindow", "Eve"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.zabout_tab), _translate("MainWindow", "About"))
import images_rc
