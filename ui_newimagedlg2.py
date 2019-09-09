# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newimagedlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewImageDlg(object):
    def setupUi(self, NewImageDlg):
        NewImageDlg.setObjectName(_fromUtf8("NewImageDlg"))
        NewImageDlg.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(NewImageDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_3 = QtGui.QPushButton(NewImageDlg)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 5, 0, 1, 1)
        self.label_2 = QtGui.QLabel(NewImageDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(NewImageDlg)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.label = QtGui.QLabel(NewImageDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.widthSpinBox = QtGui.QSpinBox(NewImageDlg)
        self.widthSpinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.widthSpinBox, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(NewImageDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.fontComboBox = QtGui.QFontComboBox(NewImageDlg)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.gridLayout.addWidget(self.fontComboBox, 2, 2, 1, 2)
        self.colorLabel = QtGui.QLabel(NewImageDlg)
        self.colorLabel.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.colorLabel, 3, 0, 1, 1)
        self.brushComboBox = QtGui.QComboBox(NewImageDlg)
        self.brushComboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.brushComboBox, 3, 2, 1, 1)
        self.colorButton = QtGui.QPushButton(NewImageDlg)
        self.colorButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.colorButton, 3, 3, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(NewImageDlg)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.label_2.setBuddy(self.spinBox_2)
        self.label.setBuddy(self.widthSpinBox)
        self.label_3.setBuddy(self.fontComboBox)

        self.retranslateUi(NewImageDlg)
        #QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_2.close)
        QtCore.QMetaObject.connectSlotsByName(NewImageDlg)

    def retranslateUi(self, NewImageDlg):
        NewImageDlg.setWindowTitle(_translate("NewImageDlg", "Image Chooser - New Image", None))
        self.pushButton_3.setText(_translate("NewImageDlg", "Ok", None))
        self.label_2.setText(_translate("NewImageDlg", "Height", None))
        self.label.setText(_translate("NewImageDlg", "Width", None))
        self.label_3.setText(_translate("NewImageDlg", "Brush pattern", None))
        self.colorLabel.setText(_translate("NewImageDlg", "Color", None))
        self.colorButton.setText(_translate("NewImageDlg", "ColorButton", None))
        self.pushButton_2.setText(_translate("NewImageDlg", "Cancel", None))
        self.pushButton_2.clicked.connect(QtGui.QApplication.instance().quit)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewImageDlg = QtGui.QDialog()
    ui = Ui_NewImageDlg()
    ui.setupUi(NewImageDlg)
    NewImageDlg.show()
    sys.exit(app.exec_())

