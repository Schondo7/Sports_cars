# Form implementation generated from reading ui file 'sportscars.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sportscars(object):
    def setupUi(self, Sportscars):
        Sportscars.setObjectName("Sportscars")
        Sportscars.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=Sportscars)
        self.centralwidget.setObjectName("centralwidget")
        self.Color = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Color.setGeometry(QtCore.QRect(80, 80, 151, 24))
        self.Color.setObjectName("Color")
        self.RacingStripe = QtWidgets.QComboBox(parent=self.centralwidget)
        self.RacingStripe.setGeometry(QtCore.QRect(320, 80, 141, 24))
        self.RacingStripe.setObjectName("RacingStripe")
        self.Car = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Car.setGeometry(QtCore.QRect(550, 80, 131, 24))
        self.Car.setObjectName("Car")
        self.Submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(310, 140, 75, 24))
        self.Submit.setObjectName("Submit")
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(170, 190, 361, 291))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 31, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 50, 41, 16))
        self.label_3.setObjectName("label_3")
        Sportscars.setCentralWidget(self.centralwidget)
        self.SportsCarColor = QtWidgets.QStatusBar(parent=Sportscars)
        self.SportsCarColor.setObjectName("SportsCarColor")
        Sportscars.setStatusBar(self.SportsCarColor)

        self.retranslateUi(Sportscars)
        QtCore.QMetaObject.connectSlotsByName(Sportscars)

    def retranslateUi(self, Sportscars):
        _translate = QtCore.QCoreApplication.translate
        Sportscars.setWindowTitle(_translate("Sportscars", "Sports Cars Colors"))
        self.Submit.setText(_translate("Sportscars", "Submit"))
        self.label.setText(_translate("Sportscars", "Color"))
        self.label_2.setText(_translate("Sportscars", "Racing Stripes"))
        self.label_3.setText(_translate("Sportscars", "Car"))
