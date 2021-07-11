# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1040)
        MainWindow.setStyleSheet("\n"
"\n"
"background-color:rgb(35, 35, 35);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 0, 1021, 921))
        self.scrollArea_3.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(25, 25, 25);\n"
"color:white;\n"
"height: 130px;\n"
"font-size: 20px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QScrollArea\n"
"{\n"
"border:none\n"
"}\n"
"\n"
"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1021, 921))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 1001, 754))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.det = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.det.setObjectName("det")
        self.gridLayout_3.addWidget(self.det, 6, 2, 1, 1)
        self.matrix = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.matrix.setObjectName("matrix")
        self.gridLayout_3.addWidget(self.matrix, 3, 3, 1, 1)
        self.plus = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.plus.setObjectName("plus")
        self.gridLayout_3.addWidget(self.plus, 2, 3, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: white")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radioButton_2, 1, 3, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: white")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_3.addWidget(self.radioButton, 0, 3, 1, 1)
        self.transpose = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.transpose.setObjectName("transpose")
        self.gridLayout_3.addWidget(self.transpose, 6, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.gridLayoutWidget_3)
        self.tabWidget_2.setStyleSheet("QLineEdit\n"
"{\n"
"height: 150px;\n"
"background-color: black;\n"
"color: white;\n"
"border: none;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QTabWidget\n"
"{\n"
"border:none\n"
"}\n"
"\n"
"QTabWidget::pane\n"
"{\n"
"border:none\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"background-color:rgb(40, 40, 40);\n"
"color: silver;\n"
"min-width:374px;\n"
"min-height:35px;\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"background-color:rgb(50, 50, 50);\n"
"color: white;\n"
"font-weight:bold;\n"
"font-size: 14px\n"
"}\n"
"\n"
"")
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("")
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 751, 611))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_7.addWidget(self.lineEdit_20, 2, 1, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_7.addWidget(self.lineEdit_21, 1, 1, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_7.addWidget(self.lineEdit_22, 2, 0, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_7.addWidget(self.lineEdit_23, 1, 2, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_7.addWidget(self.lineEdit_24, 0, 2, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_7.addWidget(self.lineEdit_25, 0, 1, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_7.addWidget(self.lineEdit_26, 0, 0, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_27.setStyleSheet("")
        self.lineEdit_27.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_7.addWidget(self.lineEdit_27, 2, 2, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_28.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_7.addWidget(self.lineEdit_28, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 751, 611))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_29.setStyleSheet("")
        self.lineEdit_29.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_8.addWidget(self.lineEdit_29, 2, 2, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_30.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_8.addWidget(self.lineEdit_30, 1, 2, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_8.addWidget(self.lineEdit_31, 2, 0, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_8.addWidget(self.lineEdit_32, 2, 1, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_8.addWidget(self.lineEdit_33, 1, 1, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_34.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_8.addWidget(self.lineEdit_34, 0, 1, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_35.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_8.addWidget(self.lineEdit_35, 0, 2, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_36.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_8.addWidget(self.lineEdit_36, 0, 0, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_37.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout_8.addWidget(self.lineEdit_37, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 6, 3)
        self.length = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.length.setObjectName("length")
        self.gridLayout_3.addWidget(self.length, 6, 3, 1, 1)
        self.scalar = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.scalar.setObjectName("scalar")
        self.gridLayout_3.addWidget(self.scalar, 5, 3, 1, 1)
        self.vector = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.vector.setObjectName("vector")
        self.gridLayout_3.addWidget(self.vector, 4, 3, 1, 1)
        self.inverse = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.inverse.setObjectName("inverse")
        self.gridLayout_3.addWidget(self.inverse, 6, 1, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_19.setGeometry(QtCore.QRect(10, 780, 1001, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setStyleSheet("background-color: black;\n"
"color: white")
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(1040, 90, 591, 681))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 679))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 571, 661))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color:white;\n"
"text-align: center;")
        self.tableWidget.setLineWidth(5)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1050, 30, 571, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1180, 20, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: none;\n"
"color:white;\n"
"background-color: rgb(25, 25, 25)")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget_2, self.lineEdit_26)
        MainWindow.setTabOrder(self.lineEdit_26, self.lineEdit_25)
        MainWindow.setTabOrder(self.lineEdit_25, self.lineEdit_24)
        MainWindow.setTabOrder(self.lineEdit_24, self.lineEdit_28)
        MainWindow.setTabOrder(self.lineEdit_28, self.lineEdit_21)
        MainWindow.setTabOrder(self.lineEdit_21, self.lineEdit_23)
        MainWindow.setTabOrder(self.lineEdit_23, self.lineEdit_22)
        MainWindow.setTabOrder(self.lineEdit_22, self.lineEdit_20)
        MainWindow.setTabOrder(self.lineEdit_20, self.lineEdit_27)
        MainWindow.setTabOrder(self.lineEdit_27, self.lineEdit_36)
        MainWindow.setTabOrder(self.lineEdit_36, self.lineEdit_34)
        MainWindow.setTabOrder(self.lineEdit_34, self.lineEdit_35)
        MainWindow.setTabOrder(self.lineEdit_35, self.lineEdit_37)
        MainWindow.setTabOrder(self.lineEdit_37, self.lineEdit_33)
        MainWindow.setTabOrder(self.lineEdit_33, self.lineEdit_30)
        MainWindow.setTabOrder(self.lineEdit_30, self.lineEdit_31)
        MainWindow.setTabOrder(self.lineEdit_31, self.lineEdit_32)
        MainWindow.setTabOrder(self.lineEdit_32, self.lineEdit_29)
        MainWindow.setTabOrder(self.lineEdit_29, self.scrollArea_3)
        MainWindow.setTabOrder(self.scrollArea_3, self.matrix)
        MainWindow.setTabOrder(self.matrix, self.vector)
        MainWindow.setTabOrder(self.vector, self.transpose)
        MainWindow.setTabOrder(self.transpose, self.inverse)
        MainWindow.setTabOrder(self.inverse, self.det)
        MainWindow.setTabOrder(self.det, self.plus)
        MainWindow.setTabOrder(self.plus, self.length)
        MainWindow.setTabOrder(self.length, self.scalar)
        MainWindow.setTabOrder(self.scalar, self.lineEdit_19)
        MainWindow.setTabOrder(self.lineEdit_19, self.scrollArea)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.det.setText(_translate("MainWindow", "Найти определитель"))
        self.matrix.setText(_translate("MainWindow", "Перемножить матрицы"))
        self.plus.setText(_translate("MainWindow", "Сложить"))
        self.radioButton_2.setText(_translate("MainWindow", "Вектора"))
        self.radioButton.setText(_translate("MainWindow", "Матрицы"))
        self.transpose.setText(_translate("MainWindow", "Транспонировать"))
        self.lineEdit_20.setText(_translate("MainWindow", "36"))
        self.lineEdit_21.setText(_translate("MainWindow", "57"))
        self.lineEdit_22.setText(_translate("MainWindow", "658"))
        self.lineEdit_23.setText(_translate("MainWindow", "574"))
        self.lineEdit_24.setText(_translate("MainWindow", "43"))
        self.lineEdit_25.setText(_translate("MainWindow", "23"))
        self.lineEdit_26.setText(_translate("MainWindow", "235"))
        self.lineEdit_27.setText(_translate("MainWindow", "745"))
        self.lineEdit_28.setText(_translate("MainWindow", "57"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Форма 1"))
        self.lineEdit_29.setText(_translate("MainWindow", "140"))
        self.lineEdit_30.setText(_translate("MainWindow", "45"))
        self.lineEdit_31.setText(_translate("MainWindow", "124"))
        self.lineEdit_32.setText(_translate("MainWindow", "787"))
        self.lineEdit_33.setText(_translate("MainWindow", "68"))
        self.lineEdit_34.setText(_translate("MainWindow", "41"))
        self.lineEdit_35.setText(_translate("MainWindow", "24"))
        self.lineEdit_36.setText(_translate("MainWindow", "75"))
        self.lineEdit_37.setText(_translate("MainWindow", "425"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Форма 2"))
        self.length.setText(_translate("MainWindow", "Найти длину"))
        self.scalar.setText(_translate("MainWindow", "Перемножить скалярно"))
        self.vector.setText(_translate("MainWindow", "Перемножить вектора"))
        self.inverse.setText(_translate("MainWindow", "Обратить"))
        self.lineEdit_19.setText(_translate("MainWindow", "124"))
        self.label_2.setText(_translate("MainWindow", "Округлить до          знаков после запятой"))
        self.lineEdit.setText(_translate("MainWindow", "5"))
