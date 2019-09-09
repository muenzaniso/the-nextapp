# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_PenPropertiesDlg(object):

    def setupUi(self, Dialog):
        PenPropertiesDlg.setObjectName(_fromUtf8("PenPropertiesDlg"))
        PenPropertiesDlg.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(PenPropertiesDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 6, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 1, 1, 6)
        spacerItem = QtGui.QSpacerItem(173, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 3, 1, 2)
        self.spinBox = QtGui.QSpinBox(PenPropertiesDlg)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 1, 3, 1, 1)
        self.checkBox = QtGui.QCheckBox(PenPropertiesDlg)
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 1, 4, 1, 1)
        self.label = QtGui.QLabel(PenPropertiesDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(PenPropertiesDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        self.comboBox = QtGui.QComboBox(PenPropertiesDlg)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.gridLayout.addWidget(self.comboBox, 2, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(PenPropertiesDlg)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(PenPropertiesDlg)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)

        self.label.setBuddy(self.spinBox)
        self.spinBox.setRange(0, 24)

        self.label_2.setBuddy(self.comboBox)

        self.retranslateUi(PenPropertiesDlg)
        QtCore.QMetaObject.connectSlotsByName(PenPropertiesDlg)

    def retranslateUi(self, Dialog):
        PenPropertiesDlg.setWindowTitle(_translate("PenPropertiesDlg", "Pen Properties", None))
        self.checkBox.setText(_translate("PenPropertiesDlg", "beleveld edges", None))
        self.label.setText(_translate("PenPropertiesDlg", "&Width", None))
        self.label_2.setText(_translate("PenPropertiesDlg", "Style", None))
        self.comboBox.setItemText(0, _translate("PenPropertiesDlg", "Solid", None))
        self.comboBox.setItemText(1, _translate("PenPropertiesDlg", "Dashed", None))
        self.comboBox.setItemText(2, _translate("PenPropertiesDlg", "Dotted", None))
        self.comboBox.setItemText(3, _translate("PenPropertiesDlg", "DashDotted", None))
        self.comboBox.setItemText(4, _translate("PenPropertiesDlg", "DashDotDotted", None))
        self.pushButton.setText(_translate("PenPropertiesDlg", "OK", None))
        self.pushButton_2.setText(_translate("PenPropertiesDlg", "Close", None))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def setPenProperties(self):
        dialog = Ui_PenPropertiesDlg
        dialog.self.spinBox.setValue(self.width)
        dialog.self.checkBox.setChecked(self.beveled)
        dialog.self.comboBox.setCurrentIndex(
            dialog.comboBox.findText(self.style))
        if dialog.exec_():
            self.width = dialog.self.sp

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PenPropertiesDlg = QtGui.QDialog()
    ui = Ui_PenPropertiesDlg()
    ui.setupUi(PenPropertiesDlg)
    PenPropertiesDlg.show()
    sys.exit(app.exec_())


