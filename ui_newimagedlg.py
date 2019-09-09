0# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newimagedlg2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

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
        self.colorLabel = QtGui.QLabel(NewImageDlg)
        self.colorLabel.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.colorLabel, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(NewImageDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(NewImageDlg)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 4, 3, 1, 1)
        self.colorButton = QtGui.QPushButton(NewImageDlg)
        self.colorButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.colorButton, 3, 3, 1, 1)
        self.widthSpinBox = QtGui.QSpinBox(NewImageDlg)
        self.widthSpinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.widthSpinBox, 0, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(NewImageDlg)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 4, 1, 1)
        self.label_2 = QtGui.QLabel(NewImageDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(NewImageDlg)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)
        #spacerItem = QtGui.QSpacerItem(149, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.brushComboBox = QtGui.QComboBox(NewImageDlg)
        self.brushComboBox.setObjectName(_fromUtf8("brushComboBox"))
        self.gridLayout.addWidget(self.brushComboBox, 2, 2, 1, 1)
        self.label = QtGui.QLabel(NewImageDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2.setBuddy(self.spinBox_2)
        self.label.setBuddy(self.widthSpinBox)



        self.retranslateUi(NewImageDlg)
        self.pushButton_2.clicked.connect(NewImageDlg.accept)
        self.pushButton_3.clicked.connect(NewImageDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(NewImageDlg)

    def retranslateUi(self, Ui_NewImageDlg):
        Ui_NewImageDlg.setWindowTitle(_translate("Ui_NewImageDlg", "Image Chooser - New Image", None))
        self.colorLabel.setText(_translate("Ui_NewImageDlg", "Color", None))
        self.label_3.setText(_translate("Ui_NewImageDlg", "Bush Pattern", None))
        self.pushButton_2.setText(_translate("Ui_NewImageDlg", "Ok", None))
        self.colorButton.setText(_translate("Ui_NewImageDlg", "Color", None))
        self.pushButton_3.setText(_translate("Ui_NewImageDlg", "Cancel", None))
        self.label_2.setText(_translate("Ui_NewImageDlg", "Height", None))
        self.label.setText(_translate("Ui_NewImageDlg", "Width", None))

    def accepted(self):
        pass

    def rejected(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewImageDlg = QtGui.QDialog()
    ui = Ui_NewImageDlg()
    ui.setupUi(NewImageDlg)
    NewImageDlg.show()
    sys.exit(app.exec_())

