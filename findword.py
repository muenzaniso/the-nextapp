# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findword.ui'
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

class Ui_FindAndReplaceDig(object):
    def setupUi(self, FindAndReplaceDig):
        FindAndReplaceDig.setObjectName(_fromUtf8("FindAndReplaceDig"))
        FindAndReplaceDig.resize(324, 234)
        self.gridLayout = QtGui.QGridLayout(FindAndReplaceDig)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.findLineEdit = QtGui.QLineEdit(FindAndReplaceDig)
        self.findLineEdit.setObjectName(_fromUtf8("findLineEdit"))
        self.gridLayout.addWidget(self.findLineEdit, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(FindAndReplaceDig)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.replaceLineEdit = QtGui.QLineEdit(FindAndReplaceDig)
        self.replaceLineEdit.setObjectName(_fromUtf8("replaceLineEdit"))
        self.gridLayout.addWidget(self.replaceLineEdit, 3, 1, 1, 1)
        self.syntaxComboBox = QtGui.QComboBox(FindAndReplaceDig)
        self.syntaxComboBox.setObjectName(_fromUtf8("syntaxComboBox"))
        self.syntaxComboBox.addItem(_fromUtf8(""))
        self.syntaxComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.syntaxComboBox, 9, 1, 1, 1)
        self.line = QtGui.QFrame(FindAndReplaceDig)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 4, 1, 1)
        self.label = QtGui.QLabel(FindAndReplaceDig)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addLayout(self.verticalLayout, 10, 6, 1, 1)
        self.label_2 = QtGui.QLabel(FindAndReplaceDig)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.caseCheckBox = QtGui.QCheckBox(FindAndReplaceDig)
        self.caseCheckBox.setObjectName(_fromUtf8("caseCheckBox"))
        self.gridLayout.addWidget(self.caseCheckBox, 4, 0, 1, 1)
        self.replaceAllButton = QtGui.QPushButton(FindAndReplaceDig)
        self.replaceAllButton.setObjectName(_fromUtf8("replaceAllButton"))
        self.gridLayout.addWidget(self.replaceAllButton, 4, 6, 1, 1)
        self.findButton = QtGui.QPushButton(FindAndReplaceDig)
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.gridLayout.addWidget(self.findButton, 2, 6, 1, 1)
        self.closeButton = QtGui.QPushButton(FindAndReplaceDig)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 12, 6, 1, 1)
        self.replaceButton = QtGui.QPushButton(FindAndReplaceDig)
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.gridLayout.addWidget(self.replaceButton, 3, 6, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout.addLayout(self.gridLayout_4, 16, 6, 1, 1)
        self.wholeCheckBox = QtGui.QCheckBox(FindAndReplaceDig)
        self.wholeCheckBox.setChecked(True)
        self.wholeCheckBox.setObjectName(_fromUtf8("wholeCheckBox"))
        self.gridLayout.addWidget(self.wholeCheckBox, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout.addLayout(self.horizontalLayout_2, 12, 0, 1, 1)
        self.label_3.setBuddy(self.syntaxComboBox)
        self.label.setBuddy(self.findLineEdit)
        self.label_2.setBuddy(self.replaceLineEdit)

        self.retranslateUi(FindAndReplaceDig)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeButton.close)
        QtCore.QMetaObject.connectSlotsByName(FindAndReplaceDig)
        FindAndReplaceDig.setTabOrder(self.findLineEdit, self.replaceLineEdit)
        FindAndReplaceDig.setTabOrder(self.replaceLineEdit, self.wholeCheckBox)
        FindAndReplaceDig.setTabOrder(self.wholeCheckBox, self.syntaxComboBox)
        FindAndReplaceDig.setTabOrder(self.syntaxComboBox, self.findButton)
        FindAndReplaceDig.setTabOrder(self.findButton, self.replaceButton)
        FindAndReplaceDig.setTabOrder(self.replaceButton, self.replaceAllButton)
        FindAndReplaceDig.setTabOrder(self.replaceAllButton, self.closeButton)
        FindAndReplaceDig.setTabOrder(self.closeButton, self.caseCheckBox)

    def retranslateUi(self, FindAndReplaceDig):
        FindAndReplaceDig.setWindowTitle(_translate("FindAndReplaceDig", "Find and Replace", None))
        self.label_3.setText(_translate("FindAndReplaceDig", "&Syntax", None))
        self.syntaxComboBox.setItemText(0, _translate("FindAndReplaceDig", "Literal text", None))
        self.syntaxComboBox.setItemText(1, _translate("FindAndReplaceDig", "Regular expression", None))
        self.label.setText(_translate("FindAndReplaceDig", "Find &what", None))
        self.label_2.setText(_translate("FindAndReplaceDig", "Replace &with", None))
        self.caseCheckBox.setText(_translate("FindAndReplaceDig", "&Case sensitive", None))
        self.replaceAllButton.setText(_translate("FindAndReplaceDig", "Replace &All", None))
        self.findButton.setText(_translate("FindAndReplaceDig", "&Find", None))
        self.closeButton.setText(_translate("FindAndReplaceDig", "Close", None))
        self.replaceButton.setText(_translate("FindAndReplaceDig", "&Replace", None))
        self.wholeCheckBox.setText(_translate("FindAndReplaceDig", "W&hole words", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FindAndReplaceDig = QtGui.QDialog()
    ui = Ui_FindAndReplaceDig()
    ui.setupUi(FindAndReplaceDig)
    FindAndReplaceDig.show()
    sys.exit(app.exec_())

