# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainUFTjFg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(
            u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(220, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(
            u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_left_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(3)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.End_x_input = QLineEdit(self.frame_left_menu)
        self.End_x_input.setObjectName(u"End_x_input")
        self.End_x_input.setMaximumSize(QSize(215, 25))
        self.End_x_input.setStyleSheet(
            u"background-color: rgb(255, 255, 255);")
        self.End_x_input.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.End_x_input, 7, 0, 1, 1)

        self.label = QLabel(self.frame_left_menu)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 45))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                 "border-color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(3)
        self.label.setIndent(-1)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.error_domain = QLabel(self.frame_left_menu)
        self.error_domain.setObjectName(u"error_domain")
        self.error_domain.setMaximumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.error_domain, 8, 0, 1, 1)

        self.Submit = QPushButton(self.frame_left_menu)
        self.Submit.setObjectName(u"Submit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(
            self.Submit.sizePolicy().hasHeightForWidth())
        self.Submit.setSizePolicy(sizePolicy1)
        self.Submit.setMinimumSize(QSize(0, 40))
        self.Submit.setStyleSheet(u"QPushButton {\n"
                                  " 	color: rgb(255, 255, 255);\n"
                                  "	background-color: rgb(35, 35, 35);\n"
                                  "	border: 0px solid;\n"
                                  "}\n"
                                  "QPushButton:hover {\n"
                                  "	background-color: rgb(85, 170, 255);\n"
                                  "}")

        self.gridLayout.addWidget(self.Submit, 12, 0, 1, 1)

        self.Start_x_input = QLineEdit(self.frame_left_menu)
        self.Start_x_input.setObjectName(u"Start_x_input")
        self.Start_x_input.setMaximumSize(QSize(215, 25))
        self.Start_x_input.setStyleSheet(
            u"background-color: rgb(255, 255, 255);")
        self.Start_x_input.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Start_x_input, 5, 0, 1, 1)

        self.label_4 = QLabel(self.frame_left_menu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 43))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setMargin(3)

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.Equation_input = QLineEdit(self.frame_left_menu)
        self.Equation_input.setObjectName(u"Equation_input")
        self.Equation_input.setMaximumSize(QSize(215, 25))
        self.Equation_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "")
        self.Equation_input.setFrame(True)
        self.Equation_input.setCursorPosition(0)
        self.Equation_input.setAlignment(Qt.AlignCenter)
        self.Equation_input.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.Equation_input, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame_left_menu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 45))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(3)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.Excepted_x_input = QLineEdit(self.frame_left_menu)
        self.Excepted_x_input.setObjectName(u"Excepted_x_input")
        self.Excepted_x_input.setMaximumSize(QSize(215, 25))
        self.Excepted_x_input.setStyleSheet(
            u"background-color: rgb(255, 255, 255);")
        self.Excepted_x_input.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Excepted_x_input, 10, 0, 1, 1)

        self.error_equation = QLabel(self.frame_left_menu)
        self.error_equation.setObjectName(u"error_equation")
        self.error_equation.setMaximumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.error_equation, 3, 0, 1, 1)

        self.error_except = QLabel(self.frame_left_menu)
        self.error_except.setObjectName(u"error_except")

        self.gridLayout.addWidget(self.error_except, 11, 0, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_top_menus)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Matplotlip_Image = QFrame(self.frame_pages)
        self.Matplotlip_Image.setObjectName(u"Matplotlip_Image")
        self.Matplotlip_Image.setFrameShape(QFrame.StyledPanel)
        self.Matplotlip_Image.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.Matplotlip_Image)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate(
            "MainWindow", u"TOGGLE", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"start x", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Equation", None))
        self.error_domain.setText("")
        self.Submit.setText(QCoreApplication.translate(
            "MainWindow", u"Submit", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Excepted x", None))
        self.Equation_input.setInputMask("")
        self.Equation_input.setText("")
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"End X", None))
        self.error_equation.setText("")
        self.error_except.setText("")
    # retranslateUi
