# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitledwEOarM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QDate)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1218, 625)
        MainWindow.setMinimumSize(QSize(1218, 625))
        MainWindow.setMaximumSize(QSize(1218, 1000))
        MainWindow.setBaseSize(QSize(1000, 1000))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {background:qlineargradient(spread:pad, x1:0.135591, y1:0.176, x2:1, y2:1, stop:0 rgba(0, 16, 35, 255), stop:0.397727 rgba(34, 0, 43, 255), stop:1 rgba(20, 93, 96, 255))}\n"
"\n"
"*{\n"
"font-weight: bold;\n"
"color: #fff;\n"
"font-size: 12px;\n"
"border: none;\n"
"background: none;}\n"
"\n"
"#label_4{font-size: 20px;}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu = QCustomSlideMenu(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(225, 0))
        self.left_menu.setMaximumSize(QSize(225, 16777215))
        self.left_menu.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.left_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 105))
        self.frame.setMaximumSize(QSize(16777215, 110))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 15, -1, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 70))
        self.label.setMaximumSize(QSize(150, 70))
        self.label.setBaseSize(QSize(125, 0))
        self.label.setPixmap(QPixmap(u":/images/images/Logo_Data copia.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"\n"
"#frame_2{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 100), stop:1 rgba(0, 0, 0, 100))}\n"
"\n"
" QFrame:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, 15)
        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"Qframe:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"\n"
"}\n"
"\n"
"#frame_12  {border: 1px solid  rgb(6, 194, 252, 80)}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.frame_12)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 25))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"RomanD")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/034-profits.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(22, 22))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_12, 0, Qt.AlignVCenter)

        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"#frame_14  {border: 1px solid  rgb(6, 194, 252,80)}\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_2 = QPushButton(self.frame_14)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 25))
        self.pushButton_2.setMaximumSize(QSize(16777215, 25))
        self.pushButton_2.setBaseSize(QSize(0, 0))
        self.pushButton_2.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/010-contract.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"#frame_13  {border: 1px solid  rgb(6, 194, 252,80)}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_3 = QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/167-wall-clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.pushButton_3)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"#frame_15  {border: 1px solid  rgb(6, 194, 252,80)}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_4 = QPushButton(self.frame_15)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.horizontalLayout_11.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"#frame_16  {border: 1px solid  rgb(6, 194, 252,80)}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_5 = QPushButton(self.frame_16)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)

        self.horizontalLayout_12.addWidget(self.pushButton_5)


        self.verticalLayout_3.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"#frame_17  {border: 1px solid  rgb(6, 194, 252,80)}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_6 = QPushButton(self.frame_17)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)

        self.horizontalLayout_13.addWidget(self.pushButton_6)


        self.verticalLayout_3.addWidget(self.frame_17)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.frame_8 = QFrame(self.left_menu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 150))
        self.label_2.setPixmap(QPixmap(u":/images/images/usc.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.left_menu)

        self.dashboard = QFrame(self.centralwidget)
        self.dashboard.setObjectName(u"dashboard")
        self.dashboard.setFrameShape(QFrame.StyledPanel)
        self.dashboard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dashboard)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.dashboard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 100), stop:1 rgba(0, 0, 0, 100))}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(20, 0))
        self.frame_5.setMaximumSize(QSize(100, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(80, 0))
        self.pushButton_7.setMaximumSize(QSize(100, 80))
        self.pushButton_7.setBaseSize(QSize(0, 0))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/060-align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_7, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamily(u"RomanD")
        font1.setBold(True)
        font1.setWeight(75)
        font1.setKerning(False)
        self.label_4.setFont(font1)
        self.label_4.setScaledContents(False)

        self.horizontalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(55, 0))
        self.frame_7.setMaximumSize(QSize(150, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_9 = QPushButton(self.frame_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(40, 40))
        self.pushButton_9.setMaximumSize(QSize(40, 40))
        self.pushButton_9.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/080-down-arrow-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(40, 40))
        self.pushButton_8.setMaximumSize(QSize(40, 40))
        self.pushButton_8.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/021-stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.frame_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(40, 40))
        self.pushButton_10.setMaximumSize(QSize(40, 40))
        self.pushButton_10.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(144, 0, 204, 80);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/034-cancel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_10, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.dashboard)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"\n"
"#stackedWidget{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 54), stop:1 rgba(0, 0, 0, 54))}\n"
"")
        self.predictions = QWidget()
        self.predictions.setObjectName(u"predictions")
        self.predictions.setStyleSheet(u"#predictions{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 100), stop:1 rgba(0, 0, 0, 100))}")
        self.verticalLayout_6 = QVBoxLayout(self.predictions)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_18 = QFrame(self.predictions)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_18)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setBaseSize(QSize(0, 50))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.pushButton_11 = QPushButton(self.frame_18)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)
        self.pushButton_11.setMinimumSize(QSize(125, 40))
        self.pushButton_11.setMaximumSize(QSize(150, 80))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"\n"
"}\n"
"\n"
"#pushButton_11{border: 1px solid  rgb(6, 194, 252,80)}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/145-upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.pushButton_11)


        self.verticalLayout_6.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_19 = QFrame(self.predictions)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setLineWidth(1)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_chart = QGridLayout(self.frame_21)
        self.gridLayout_chart.setObjectName(u"gridLayout_chart")

        self.horizontalLayout_14.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy2)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setLineWidth(1)
        self.verticalLayout_8 = QVBoxLayout(self.frame_20)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_22)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy3)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_23)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.frame_23)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 3)

        self.horizontalLayout_14.addWidget(self.frame_20)

        self.horizontalLayout_14.setStretch(0, 3)
        self.horizontalLayout_14.setStretch(1, 2)

        self.verticalLayout_6.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.predictions)
        self.inputs = QWidget()
        self.inputs.setObjectName(u"inputs")
        self.inputs.setStyleSheet(u"#inputs{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 100), stop:1 rgba(0, 0, 0, 100))}")
        self.verticalLayout_9 = QVBoxLayout(self.inputs)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.exit_container = QFrame(self.inputs)
        self.exit_container.setObjectName(u"exit_container")
        sizePolicy.setHeightForWidth(self.exit_container.sizePolicy().hasHeightForWidth())
        self.exit_container.setSizePolicy(sizePolicy)
        self.exit_container.setMaximumSize(QSize(16777215, 0))
        self.exit_container.setFrameShape(QFrame.StyledPanel)
        self.exit_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.exit_container)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.exit_container)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"#frame_24{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 158, 255, 131), stop:1 rgba(255, 255, 255, 19))}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_24)
        self.verticalLayout_11.setSpacing(50)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 20, -1, 20)
        self.label_6 = QLabel(self.frame_24)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)

        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_25)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(50, 25))
        self.pushButton_13.setMaximumSize(QSize(50, 25))
        self.pushButton_13.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"\n"
"}\n"
"\n"
"#pushButton_13  {border: 1px solid  rgb(6, 194, 252, 80)}")

        self.horizontalLayout_15.addWidget(self.pushButton_13, 0, Qt.AlignLeft)

        self.pushButton_12 = QPushButton(self.frame_25)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(50, 25))
        self.pushButton_12.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"\n"
"}\n"
"\n"
"#pushButton_12  {border: 1px solid  rgb(6, 194, 252, 80)}")

        self.horizontalLayout_15.addWidget(self.pushButton_12, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_25)


        self.verticalLayout_10.addWidget(self.frame_24, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.exit_container)

        self.main_container = QFrame(self.inputs)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.main_container)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.middle = QFrame(self.main_container)
        self.middle.setObjectName(u"middle")
        self.middle.setMaximumSize(QSize(16777215, 16777215))
        self.middle.setFrameShape(QFrame.StyledPanel)
        self.middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.middle)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.start_frame = QFrame(self.middle)
        self.start_frame.setObjectName(u"start_frame")
        self.start_frame.setMaximumSize(QSize(0, 16777215))
        self.start_frame.setFrameShape(QFrame.StyledPanel)
        self.start_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.start_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.start_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"#label_9{font-size:17px}")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_9)

        self.label_8 = QLabel(self.start_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_8, 0, Qt.AlignTop)

        self.pushButton_15 = QPushButton(self.start_frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(300, 30))
        self.pushButton_15.setMaximumSize(QSize(300, 16777215))
        self.pushButton_15.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(179, 37, 220, 50);\n"
"}\n"
"\n"
"\n"
"#pushButton_15{border: 1px solid  rgb(179, 37, 220, 90)}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/033-fast-forward.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setIconSize(QSize(20, 20))

        self.verticalLayout_16.addWidget(self.pushButton_15, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_17.addWidget(self.start_frame)

        self.frame_30 = QFrame(self.middle)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_30)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_30)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.MO = QWidget()
        self.MO.setObjectName(u"MO")
        self.MO.setFocusPolicy(Qt.TabFocus)
        self.horizontalLayout_18 = QHBoxLayout(self.MO)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_28 = QFrame(self.MO)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy4)
        self.frame_28.setMinimumSize(QSize(400, 0))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_28)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, -1, 0, 0)
        self.pushButton_20 = QPushButton(self.frame_28)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 0))
        self.pushButton_20.setMaximumSize(QSize(80, 35))
        font2 = QFont()
        font2.setFamily(u"SansSerif")
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}\n"
"\n"
"#pushButton_20  {border: 1px solid  rgb(6, 194, 252, 80)}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/039-shuffle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_20.setIcon(icon9)

        self.gridLayout_4.addWidget(self.pushButton_20, 4, 3, 1, 1)

        self.tableWidget_2 = QTableWidget(self.frame_28)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy2.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy2)
        self.tableWidget_2.setMinimumSize(QSize(319, 150))
        self.tableWidget_2.setMaximumSize(QSize(310, 500))
        self.tableWidget_2.setStyleSheet(u"#tableWidget_2{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 50), stop:1 rgba(0, 0, 0, 50));\n"
"border: 1px solid  rgb(6, 194, 252, 50);\n"
"gridline-color: rgb(6, 194, 252, 50);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{background-color: rgb(0, 0, 0);\n"
"border: 1px solid  rgb(6, 194, 252, 50);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(6, 194, 252, 50) \n"
"\n"
"}\n"
"\n"
"QScrollBar:vertical{border:none;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 100), stop:1 rgba(0, 0, 0, 100))}\n"
"\n"
"\n"
"QScrollBar:horizontal{\n"
"border:none;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 100), stop:1 rgba(0, 0, 0, 100))}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color:rgb(0, 0, 0);}\n"
"\n"
"")
        self.tableWidget_2.setLineWidth(3)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setAutoScroll(False)
        self.tableWidget_2.setAutoScrollMargin(0)
        self.tableWidget_2.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableWidget_2, 2, 0, 4, 3)

        self.lineEdit_2 = QLineEdit(self.frame_28)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_2.setStyleSheet(u"\n"
"\n"
"#lineEdit_2  {border: 1px solid  rgb(6, 194, 252,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 151, 255, 55), stop:1 rgba(255, 255, 255, 30))\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame_28)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(80, 0))
        self.label_11.setMaximumSize(QSize(80, 16777215))
        self.label_11.setFont(font2)

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.frame_28)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"#label_12{font-size:35px}")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 3)

        self.pushButton_21 = QPushButton(self.frame_28)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setFont(font2)
        self.pushButton_21.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}\n"
"\n"
"#pushButton_21  {border: 1px solid  rgb(6, 194, 252, 80)}")

        self.gridLayout_4.addWidget(self.pushButton_21, 3, 3, 1, 1)

        self.pushButton_22 = QPushButton(self.frame_28)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setFont(font2)
        self.pushButton_22.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}\n"
"#pushButton_22  {border: 1px solid  rgb(6, 194, 252, 80)}")

        self.gridLayout_4.addWidget(self.pushButton_22, 2, 3, 1, 1)


        self.horizontalLayout_18.addWidget(self.frame_28)

        self.frame_31 = QFrame(self.MO)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy2.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy2)
        self.frame_31.setMinimumSize(QSize(500, 0))
        self.frame_31.setMaximumSize(QSize(500, 16777215))
        self.frame_31.setStyleSheet(u"")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_31)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.horizontalLayout_18.addWidget(self.frame_31)

        self.stackedWidget_2.addWidget(self.MO)
        self.MP = QWidget()
        self.MP.setObjectName(u"MP")
        self.verticalLayout_17 = QVBoxLayout(self.MP)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_27 = QFrame(self.MP)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_33 = QFrame(self.frame_29)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(400, 0))
        self.frame_33.setMaximumSize(QSize(300, 16777215))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_33)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.frame_33)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"#lineEdit_4 {border: 1px solid  rgb(6, 194, 252,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 151, 255, 55), stop:1 rgba(255, 255, 255, 30))\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 3, 1, 1)

        self.lineEdit = QLineEdit(self.frame_33)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(50, 16777215))
        self.lineEdit.setStyleSheet(u"#lineEdit {border: 1px solid  rgb(6, 194, 252,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 151, 255, 55), stop:1 rgba(255, 255, 255, 30))\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.lineEdit, 2, 3, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_33)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(75, 0))
        self.pushButton_16.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}\n"
"#pushButton_16  {border: 1px solid  rgb(6, 194, 252, 80)}")

        self.gridLayout_3.addWidget(self.pushButton_16, 4, 6, 1, 1, Qt.AlignLeft)

        self.tableWidget = QTableWidget(self.frame_33)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(319, 0))
        self.tableWidget.setMaximumSize(QSize(318, 16777215))
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.tableWidget.setStyleSheet(u"#tableWidget{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 50), stop:1 rgba(0, 0, 0, 50));\n"
"border: 1px solid  rgb(6, 194, 252, 50);\n"
"gridline-color: rgb(6, 194, 252, 50);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{background-color: rgb(0, 0, 0);\n"
"border: 1px solid  rgb(6, 194, 252, 50);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(6, 194, 252, 50) \n"
"\n"
"}\n"
"\n"
"QScrollBar:vertical{border:none;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 100), stop:1 rgba(0, 0, 0, 100))}\n"
"\n"
"\n"
"QScrollBar:horizontal{\n"
"border:none;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0340909 rgba(0, 0, 0, 100), stop:1 rgba(0, 0, 0, 100))}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color:rgb(0, 0, 0);}\n"
"")
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tableWidget, 3, 0, 4, 6)

        self.pushButton_17 = QPushButton(self.frame_33)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(75, 35))
        self.pushButton_17.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}\n"
"#pushButton_17  {border: 1px solid  rgb(6, 194, 252, 80)}")
        self.pushButton_17.setIcon(icon9)

        self.gridLayout_3.addWidget(self.pushButton_17, 5, 6, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.frame_33)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(200, 50))
        self.label_7.setMaximumSize(QSize(100, 16777215))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"#label_7{font-size:35px}")
        self.label_7.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 6)

        self.pushButton_14 = QPushButton(self.frame_33)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(75, 0))
        self.pushButton_14.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}\n"
"#pushButton_14  {border: 1px solid  rgb(6, 194, 252, 80)}")

        self.gridLayout_3.addWidget(self.pushButton_14, 3, 6, 1, 1, Qt.AlignLeft)

        self.label_19 = QLabel(self.frame_33)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(250, 0))
        self.label_19.setMaximumSize(QSize(300, 16777215))
        self.label_19.setFont(font2)
        self.label_19.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frame_33)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(125, 0))
        self.label_10.setMaximumSize(QSize(50, 16777215))
        self.label_10.setFont(font2)

        self.gridLayout_3.addWidget(self.label_10, 2, 1, 1, 1)


        self.horizontalLayout_20.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_29)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_34)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(50, -1, -1, -1)
        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy2.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy2)
        self.frame_36.setMinimumSize(QSize(430, 225))
        self.frame_36.setAutoFillBackground(False)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_36)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_14.addWidget(self.frame_36)

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_15 = QLabel(self.frame_35)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.horizontalLayout_21.addWidget(self.label_15, 0, Qt.AlignLeft)

        self.label_16 = QLabel(self.frame_35)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"QLabel{font-size:25px}")
        self.label_16.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_16, 0, Qt.AlignLeft)

        self.label_17 = QLabel(self.frame_35)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"\n"
"#nxt  {border: 1px solid  rgb(6, 194, 252,80);\n"
"\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.label_17, 0, Qt.AlignRight)

        self.label_18 = QLabel(self.frame_35)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setAutoFillBackground(False)
        self.label_18.setStyleSheet(u"#label_18{font-size:25px}")

        self.horizontalLayout_21.addWidget(self.label_18, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_35)

        self.verticalLayout_14.setStretch(1, 1)

        self.horizontalLayout_20.addWidget(self.frame_34)


        self.horizontalLayout_19.addWidget(self.frame_29)

        self.frame_32 = QFrame(self.frame_27)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_32)


        self.verticalLayout_17.addWidget(self.frame_27)

        self.stackedWidget_2.addWidget(self.MP)
        self.SUM = QWidget()
        self.SUM.setObjectName(u"SUM")
        self.horizontalLayout_22 = QHBoxLayout(self.SUM)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_37 = QFrame(self.SUM)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_38)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_20 = QLabel(self.frame_38)
        self.label_20.setObjectName(u"label_20")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"#label_20{font-size: 30px}")

        self.verticalLayout_20.addWidget(self.label_20, 0, Qt.AlignTop)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy2.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy2)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_40)
        self.gridLayout_7.setObjectName(u"gridLayout_7")

        self.verticalLayout_20.addWidget(self.frame_40)


        self.horizontalLayout_23.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_39)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_21 = QLabel(self.frame_39)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"#label_21{font-size:30px}")

        self.verticalLayout_21.addWidget(self.label_21, 0, Qt.AlignTop)

        self.frame_41 = QFrame(self.frame_39)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy2.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy2)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_41)
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.verticalLayout_21.addWidget(self.frame_41)


        self.horizontalLayout_23.addWidget(self.frame_39)


        self.horizontalLayout_22.addWidget(self.frame_37)

        self.stackedWidget_2.addWidget(self.SUM)

        self.verticalLayout_15.addWidget(self.stackedWidget_2)


        self.horizontalLayout_17.addWidget(self.frame_30)


        self.verticalLayout_12.addWidget(self.middle)

        self.footer = QFrame(self.main_container)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 16777215))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.footer)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_26 = QFrame(self.footer)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.prev = QPushButton(self.frame_26)
        self.prev.setObjectName(u"prev")
        self.prev.setMinimumSize(QSize(200, 30))
        self.prev.setMaximumSize(QSize(100, 30))
        self.prev.setBaseSize(QSize(0, 0))
        self.prev.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"}\n"
"\n"
"#prev  {border: 1px solid  rgb(6, 194, 252,80);\n"
"\n"
"}\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/115-left-arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.prev.setIcon(icon10)
        self.prev.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.prev, 0, Qt.AlignRight)

        self.nxt = QPushButton(self.frame_26)
        self.nxt.setObjectName(u"nxt")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.nxt.sizePolicy().hasHeightForWidth())
        self.nxt.setSizePolicy(sizePolicy5)
        self.nxt.setMinimumSize(QSize(200, 30))
        self.nxt.setMaximumSize(QSize(100, 30))
        self.nxt.setStyleSheet(u"QPushButton:hover\n"
"{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 151, 255, 55), stop:1 rgba(255, 255, 255, 30))\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"#nxt  {border: 1px solid  rgb(6, 194, 252,80);\n"
"\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/083-chevron.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nxt.setIcon(icon11)
        self.nxt.setIconSize(QSize(20, 20))

        self.horizontalLayout_16.addWidget(self.nxt, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_26)


        self.verticalLayout_12.addWidget(self.footer)


        self.verticalLayout_9.addWidget(self.main_container)

        self.stackedWidget.addWidget(self.inputs)
        self.Time = QWidget()
        self.Time.setObjectName(u"Time")
        self.horizontalLayout_24 = QHBoxLayout(self.Time)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_42 = QFrame(self.Time)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_42)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy)
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.calendarWidget = QCalendarWidget(self.frame_44)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 110, 391, 271))
        font4 = QFont()
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setWeight(75)
        font4.setStrikeOut(False)
        font4.setKerning(False)
        self.calendarWidget.setFont(font4)
        self.calendarWidget.setStyleSheet(u"color :black;\n"
"background-color:#BFDBFA;")
        self.calendarWidget.setSelectedDate(QDate(2021, 10, 1))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.label_22 = QLabel(self.frame_44)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 450, 50))
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy6)
        self.label_22.setMinimumSize(QSize(450, 50))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"font-size:30px")
        self.label_22.setScaledContents(True)
        self.label_26 = QLabel(self.frame_44)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 60, 400, 20))
        self.label_26.setMinimumSize(QSize(0, 20))
        self.label_26.setMaximumSize(QSize(16777215, 20))
        self.label_27 = QLabel(self.frame_44)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 80, 400, 20))
        self.label_27.setMinimumSize(QSize(0, 20))
        self.label_27.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_22.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_18 = QPushButton(self.frame_45)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(100, 25))
        self.pushButton_18.setMaximumSize(QSize(135, 25))
        self.pushButton_18.setBaseSize(QSize(0, 0))
        self.pushButton_18.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"\n"
"}\n"
"\n"
"#pushButton_18  {border: 1px solid  rgb(6, 194, 252, 80)}")

        self.horizontalLayout_26.addWidget(self.pushButton_18)

        self.label_23 = QLabel(self.frame_45)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_26.addWidget(self.label_23)

        self.pushButton_19 = QPushButton(self.frame_45)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(100, 0))
        self.pushButton_19.setMaximumSize(QSize(135, 25))
        self.pushButton_19.setBaseSize(QSize(0, 0))
        self.pushButton_19.setStyleSheet(u"QPushButton:hover\n"
"{background-color: rgb(6, 194, 252, 50);\n"
"\n"
"}\n"
"\n"
"#pushButton_19  {border: 1px solid  rgb(6, 194, 252, 80)}")

        self.horizontalLayout_26.addWidget(self.pushButton_19)

        self.label_25 = QLabel(self.frame_45)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_26.addWidget(self.label_25)


        self.verticalLayout_22.addWidget(self.frame_45, 0, Qt.AlignBottom)


        self.horizontalLayout_24.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.Time)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_43)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_24 = QLabel(self.frame_46)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font-size:15px")

        self.horizontalLayout_25.addWidget(self.label_24, 0, Qt.AlignLeft)

        self.comboBox = QComboBox(self.frame_46)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 0))
        self.comboBox.setMaximumSize(QSize(150, 16777215))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color:#BFDBFA;\n"
"color:black;")
        self.comboBox.setEditable(False)
        self.comboBox.setFrame(True)

        self.horizontalLayout_25.addWidget(self.comboBox)


        self.verticalLayout_23.addWidget(self.frame_46, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy)
        self.frame_47.setMinimumSize(QSize(0, 400))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_47)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.verticalLayout_23.addWidget(self.frame_47)


        self.horizontalLayout_24.addWidget(self.frame_43, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.Time)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_9 = QFrame(self.dashboard)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 0, 47, 13))

        self.horizontalLayout_7.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.size_grid = QFrame(self.frame_11)
        self.size_grid.setObjectName(u"size_grid")
        self.size_grid.setGeometry(QRect(20, 10, 120, 80))
        self.size_grid.setFrameShape(QFrame.StyledPanel)
        self.size_grid.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_11)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.dashboard)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PREDICCIONES", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"DATOS DE ENTRADA", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"TIEMPO", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_2.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.pushButton_9.setText("")
        self.pushButton_8.setText("")
        self.pushButton_10.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MODELO DE PREDICCIONES", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"CARGAR EXCEL", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Are you sure you want to exit?", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"DATAS DE ENTRADA", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Click abajo para comenzar!", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u" Comenzar", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Puesto", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Salario", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Prestaciones:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Mano De Obra", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Insertar", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cantidad/Batch", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Costo Q/u", None));
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Insertar", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Capacidad de produccion (cuello de botella):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Unidades por Batch:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Costo/Unidad:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Costo/Hora:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"----", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Resumen de Costos/Hora", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Requerimiento de Producci\u00f3n", None))
        self.prev.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.nxt.setText(QCoreApplication.translate("MainWindow", u"Next ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Disponibiliad de Tiempo", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"1. Seleccione la fecha inicial  y luego click en \"Tiempo Inicial\" ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"2. Seleccione la fecha final  y luego click en \"Tiempo final\" ", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Tiempo Inicial:", None))
        self.label_23.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Tiempo Final:", None))
        self.label_25.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Seleccione la jornada:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Jornada Diurna", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Jornada Diurna Especial", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Jornada Diurna", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

