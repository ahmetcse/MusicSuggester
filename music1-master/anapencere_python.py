# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/yakar/Desktop/music1-master-master/music1-master/anapencere.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 652)
        MainWindow.setMaximumSize(QtCore.QSize(1212, 652))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.searchButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.searchButton.setStyleSheet("image: url(:/icons/icons/search.ico);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.searchButton.setText("")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.songWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.songWidget.setStyleSheet("")
        self.songWidget.setObjectName("songWidget")
        self.verticalLayout.addWidget(self.songWidget)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(390, 290, 291, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.view_area = QtWidgets.QLabel(self.gridLayoutWidget)
        self.view_area.setMaximumSize(QtCore.QSize(158, 36))
        self.view_area.setText("")
        self.view_area.setAlignment(QtCore.Qt.AlignCenter)
        self.view_area.setObjectName("view_area")
        self.gridLayout.addWidget(self.view_area, 1, 0, 1, 1)
        self.view_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.view_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_label.setObjectName("view_label")
        self.gridLayout.addWidget(self.view_label, 0, 0, 1, 1)
        self.comment_area = QtWidgets.QLabel(self.gridLayoutWidget)
        self.comment_area.setMaximumSize(QtCore.QSize(158, 36))
        self.comment_area.setText("")
        self.comment_area.setAlignment(QtCore.Qt.AlignCenter)
        self.comment_area.setObjectName("comment_area")
        self.gridLayout.addWidget(self.comment_area, 1, 1, 1, 1)
        self.comment_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.comment_label.setAlignment(QtCore.Qt.AlignCenter)
        self.comment_label.setObjectName("comment_label")
        self.gridLayout.addWidget(self.comment_label, 0, 1, 1, 1)
        self.likes_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.likes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.likes_label.setObjectName("likes_label")
        self.gridLayout.addWidget(self.likes_label, 2, 0, 1, 1)
        self.like_area = QtWidgets.QLabel(self.gridLayoutWidget)
        self.like_area.setMaximumSize(QtCore.QSize(158, 36))
        self.like_area.setText("")
        self.like_area.setAlignment(QtCore.Qt.AlignCenter)
        self.like_area.setObjectName("like_area")
        self.gridLayout.addWidget(self.like_area, 3, 0, 1, 1)
        self.repost_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.repost_label.setAlignment(QtCore.Qt.AlignCenter)
        self.repost_label.setObjectName("repost_label")
        self.gridLayout.addWidget(self.repost_label, 2, 1, 1, 1)
        self.respost_area = QtWidgets.QLabel(self.gridLayoutWidget)
        self.respost_area.setMaximumSize(QtCore.QSize(158, 36))
        self.respost_area.setText("")
        self.respost_area.setAlignment(QtCore.Qt.AlignCenter)
        self.respost_area.setObjectName("respost_area")
        self.gridLayout.addWidget(self.respost_area, 3, 1, 1, 1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(280, 10, 481, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.graphLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.graphLayout.setContentsMargins(0, 0, 0, 0)
        self.graphLayout.setObjectName("graphLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.view_label.setText(_translate("MainWindow", "Views"))
        self.comment_label.setText(_translate("MainWindow", "Comment Count"))
        self.likes_label.setText(_translate("MainWindow", "Likes"))
        self.repost_label.setText(_translate("MainWindow", "Reposts"))

import resource_rc