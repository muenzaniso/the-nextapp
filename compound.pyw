# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compound.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(269, 178)


        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 35, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 7, 4, 2, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 6, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 8, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 8, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 2, 1, 3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3.addLayout(self.verticalLayout_3, 3, 0, 6, 1)
        self.spinBox_2 = QtGui.QDoubleSpinBox(Dialog)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout_3.addWidget(self.spinBox_2, 5, 3, 1, 2)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 4, 1, 1, 1)
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_3.addWidget(self.spinBox, 4, 3, 1, 2)
        self.fontComboBox = QtGui.QComboBox(Dialog)
        self.fontComboBox.setObjectName(_fromUtf8("ComboBox"))
        intlist = ['{} year(s)'.format(i) for i  in range(0, 100)]
        self.fontComboBox.addItems(intlist)
        self.gridLayout_3.addWidget(self.fontComboBox, 6, 3, 1, 2)

        self.spinBox.setMaximum(10000000)

        # shows the number of items on the status bar
        num_items = self.fontComboBox.count()
        print(num_items)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # connects the 'QSpinBox.valueChanged()' signal with its respective slot
        self.spinBox.valueChanged[int].connect(self.qspinbox_valuechanged)
        self.spinBox_2.valueChanged.connect(self.qspinbox_valuechanged)

        self.spinBox.valueChanged[u'QString'].connect(self.qspinbox_valuechanged)
        self.spinBox_2.valueChanged[u'QString'].connect(self.qspinbox_valuechanged)

        # 'currentIndexChanged()' signal
        self.fontComboBox.currentIndexChanged['int'].connect(self.qspinbox_valuechanged)
        print(self.spinBox.value())

        self.spinBox.setPrefix("$")
        self.spinBox_2.setSuffix("%")


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Years:", None))
        self.label_2.setText(_translate("Dialog", "Rate:", None))
        self.label_4.setText(_translate("Dialog", "Amount", None))
        self.label.setText(_translate("Dialog", "Principal:", None))

    def qspinbox_valuechanged(self, value):
        print(u'The value of the QSpinBox has changed: {} (type: {})'.format(value, type(value)))
        self.ratee = self.spinBox_2.cleanText()
        self.principal = self.spinBox.cleanText()
        self.years = self.fontComboBox.currentIndex()
        print(self.years)
        if isinstance(value, int):
            print(self.ratee)

        #elif isinstance(value, QtCore.QtString):
        #    print(u'String')

        rat = (1 + float(self.ratee))**self.years
        print(rat)
        result = int(self.principal)* rat
        print(result)
        self.label_5.setText("$" + str(result))




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

