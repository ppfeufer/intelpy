# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 790)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(759, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pieico/goodpie2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainHorizontalLayout = QtWidgets.QHBoxLayout()
        self.mainHorizontalLayout.setObjectName("mainHorizontalLayout")
        self.leftSideVerticalLayout = QtWidgets.QVBoxLayout()
        self.leftSideVerticalLayout.setSpacing(10)
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
        self.rightSideVLayout.setSpacing(10)
        self.rightSideVLayout.setObjectName("rightSideVLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setMinimumSize(QtCore.QSize(370, 0))
        self.tab_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab_widget.setObjectName("tab_widget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.layoutWidget = QtWidgets.QWidget(self.main_tab)
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
        self.layoutWidget1 = QtWidgets.QWidget(self.main_tab)
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
        self.horizontalSlider_AlertJumps.setMaximum(8)
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
        self.groupBox = QtWidgets.QGroupBox(self.main_tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 160, 361, 551))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 35, 341, 352))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_recentalert1 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_recentalert1.sizePolicy().hasHeightForWidth())
        self.label_recentalert1.setSizePolicy(sizePolicy)
        self.label_recentalert1.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_recentalert1.setFont(font)
        self.label_recentalert1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_recentalert1.setWordWrap(False)
        self.label_recentalert1.setOpenExternalLinks(True)
        self.label_recentalert1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_recentalert1.setObjectName("label_recentalert1")
        self.verticalLayout_4.addWidget(self.label_recentalert1)
        self.label_recentalert2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_recentalert2.sizePolicy().hasHeightForWidth())
        self.label_recentalert2.setSizePolicy(sizePolicy)
        self.label_recentalert2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_recentalert2.setFont(font)
        self.label_recentalert2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_recentalert2.setWordWrap(False)
        self.label_recentalert2.setOpenExternalLinks(True)
        self.label_recentalert2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_recentalert2.setObjectName("label_recentalert2")
        self.verticalLayout_4.addWidget(self.label_recentalert2)
        self.label_recentalert3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_recentalert3.sizePolicy().hasHeightForWidth())
        self.label_recentalert3.setSizePolicy(sizePolicy)
        self.label_recentalert3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_recentalert3.setFont(font)
        self.label_recentalert3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_recentalert3.setWordWrap(False)
        self.label_recentalert3.setOpenExternalLinks(True)
        self.label_recentalert3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_recentalert3.setObjectName("label_recentalert3")
        self.verticalLayout_4.addWidget(self.label_recentalert3)
        self.label_recentalert4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_recentalert4.sizePolicy().hasHeightForWidth())
        self.label_recentalert4.setSizePolicy(sizePolicy)
        self.label_recentalert4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_recentalert4.setFont(font)
        self.label_recentalert4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_recentalert4.setWordWrap(False)
        self.label_recentalert4.setOpenExternalLinks(True)
        self.label_recentalert4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_recentalert4.setObjectName("label_recentalert4")
        self.verticalLayout_4.addWidget(self.label_recentalert4)
        self.label_recentalert5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_recentalert5.sizePolicy().hasHeightForWidth())
        self.label_recentalert5.setSizePolicy(sizePolicy)
        self.label_recentalert5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_recentalert5.setFont(font)
        self.label_recentalert5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_recentalert5.setWordWrap(False)
        self.label_recentalert5.setOpenExternalLinks(True)
        self.label_recentalert5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_recentalert5.setObjectName("label_recentalert5")
        self.verticalLayout_4.addWidget(self.label_recentalert5)
        self.tab_widget.addTab(self.main_tab, "")
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 520, 192, 92))
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
        self.label_6.setGeometry(QtCore.QRect(60, 520, 91, 22))
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.advancedtab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 630, 197, 61))
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
        self.label_9.setGeometry(QtCore.QRect(50, 630, 101, 22))
        self.label_9.setObjectName("label_9")
        self.watchedChannelsGroupBox = QtWidgets.QGroupBox(self.advancedtab)
        self.watchedChannelsGroupBox.setGeometry(QtCore.QRect(0, 120, 361, 330))
        self.watchedChannelsGroupBox.setMinimumSize(QtCore.QSize(350, 330))
        self.watchedChannelsGroupBox.setMaximumSize(QtCore.QSize(16777215, 330))
        self.watchedChannelsGroupBox.setObjectName("watchedChannelsGroupBox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.watchedChannelsGroupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 30, 341, 291))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditChannelAdd = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditChannelAdd.setObjectName("lineEditChannelAdd")
        self.horizontalLayout_2.addWidget(self.lineEditChannelAdd)
        self.addChannelAddButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.addChannelAddButton.setObjectName("addChannelAddButton")
        self.horizontalLayout_2.addWidget(self.addChannelAddButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.channelListWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_4)
        self.channelListWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.channelListWidget.setUniformItemSizes(True)
        self.channelListWidget.setSelectionRectVisible(True)
        self.channelListWidget.setObjectName("channelListWidget")
        self.horizontalLayout_3.addWidget(self.channelListWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.removeChannelButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.removeChannelButton.setObjectName("removeChannelButton")
        self.verticalLayout_3.addWidget(self.removeChannelButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.advancedtab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 470, 180, 38))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 10))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spinBox_recentalerttimeout = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_recentalerttimeout.sizePolicy().hasHeightForWidth())
        self.spinBox_recentalerttimeout.setSizePolicy(sizePolicy)
        self.spinBox_recentalerttimeout.setMaximumSize(QtCore.QSize(16777215, 30))
        self.spinBox_recentalerttimeout.setMinimum(1)
        self.spinBox_recentalerttimeout.setMaximum(20)
        self.spinBox_recentalerttimeout.setObjectName("spinBox_recentalerttimeout")
        self.horizontalLayout_5.addWidget(self.spinBox_recentalerttimeout)
        self.tab_widget.addTab(self.advancedtab, "")
        self.zabout_tab = QtWidgets.QWidget()
        self.zabout_tab.setObjectName("zabout_tab")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.zabout_tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(60, 30, 252, 321))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(250, 140))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/piebig/goodpie2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.checkBoxDarkMode = QtWidgets.QCheckBox(self.zabout_tab)
        self.checkBoxDarkMode.setGeometry(QtCore.QRect(0, 690, 441, 21))
        self.checkBoxDarkMode.setToolTip("")
        self.checkBoxDarkMode.setObjectName("checkBoxDarkMode")
        self.tab_widget.addTab(self.zabout_tab, "")
        self.rightSideVLayout.addWidget(self.tab_widget)
        self.mainHorizontalLayout.addLayout(self.rightSideVLayout)
        self.horizontalLayout.addLayout(self.mainHorizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.eve_statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eve_statusbar.setFont(font)
        self.eve_statusbar.setObjectName("eve_statusbar")
        MainWindow.setStatusBar(self.eve_statusbar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionLook_up_zKill = QtWidgets.QAction(MainWindow)
        self.actionLook_up_zKill.setObjectName("actionLook_up_zKill")

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditHome_System, self.pushButtonSet_Home)
        MainWindow.setTabOrder(self.pushButtonSet_Home, self.horizontalSlider_AlertJumps)
        MainWindow.setTabOrder(self.horizontalSlider_AlertJumps, self.clearLogButton)
        MainWindow.setTabOrder(self.clearLogButton, self.lineEditEve_Log_Location)
        MainWindow.setTabOrder(self.lineEditEve_Log_Location, self.pushButtonChoose_Eve_Log_Location)
        MainWindow.setTabOrder(self.pushButtonChoose_Eve_Log_Location, self.lineEdit_alarm)
        MainWindow.setTabOrder(self.lineEdit_alarm, self.pushButtonChoose_alarm_Location)
        MainWindow.setTabOrder(self.pushButtonChoose_alarm_Location, self.addChannelAddButton)
        MainWindow.setTabOrder(self.addChannelAddButton, self.channelListWidget)
        MainWindow.setTabOrder(self.channelListWidget, self.spinBox_recentalerttimeout)
        MainWindow.setTabOrder(self.spinBox_recentalerttimeout, self.checkbox_displayalerts)
        MainWindow.setTabOrder(self.checkbox_displayalerts, self.checkBox_displayclear)
        MainWindow.setTabOrder(self.checkBox_displayclear, self.checkBox_displayall)
        MainWindow.setTabOrder(self.checkBox_displayall, self.checkBox_filterclear)
        MainWindow.setTabOrder(self.checkBox_filterclear, self.checkBox_filterstatus)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IntelPy"))
        self.clearLogButton.setText(_translate("MainWindow", "Clear Log"))
        self.labelHome_System.setText(_translate("MainWindow", "Home system:"))
        self.pushButtonSet_Home.setText(_translate("MainWindow", "Set Home"))
        self.labelAlertWhen.setText(_translate("MainWindow", "Alert when within jumps:"))
        self.groupBox.setTitle(_translate("MainWindow", "Recent Alerts"))
        self.label_recentalert1.setText(_translate("MainWindow", "Alert1"))
        self.label_recentalert2.setText(_translate("MainWindow", "Alert2"))
        self.label_recentalert3.setText(_translate("MainWindow", "Alert3"))
        self.label_recentalert4.setText(_translate("MainWindow", "Alert4"))
        self.label_recentalert5.setText(_translate("MainWindow", "Alert5"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.main_tab), _translate("MainWindow", "Main"))
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
        self.watchedChannelsGroupBox.setTitle(_translate("MainWindow", "Watched channels"))
        self.addChannelAddButton.setText(_translate("MainWindow", "Add"))
        self.removeChannelButton.setText(_translate("MainWindow", "Remove Channel"))
        self.label_7.setText(_translate("MainWindow", "Alert timeout:"))
        self.spinBox_recentalerttimeout.setSuffix(_translate("MainWindow", "min"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.advancedtab), _translate("MainWindow", "Config"))
        self.label.setText(_translate("MainWindow", "IntelPy"))
        self.label_3.setText(_translate("MainWindow", "v1.1"))
        self.label_2.setText(_translate("MainWindow", "by Swizzles Saissore"))
        self.checkBoxDarkMode.setText(_translate("MainWindow", "Dark mode (restart required)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.zabout_tab), _translate("MainWindow", "About"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setToolTip(_translate("MainWindow", "Copy text"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionLook_up_zKill.setText(_translate("MainWindow", "Look up zKill"))
        self.actionLook_up_zKill.setToolTip(_translate("MainWindow", "Look up on zKillboard"))
import images_rc
