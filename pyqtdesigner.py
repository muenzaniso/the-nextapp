# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lulalula.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.please = QtGui.QPushButton(self.centralwidget)
        self.please.setObjectName(_fromUtf8("please"))
        self.gridLayout.addWidget(self.please, 0, 3, 1, 1)
        self.bonyoNyo = QtGui.QCheckBox(self.centralwidget)
        self.bonyoNyo.setObjectName(_fromUtf8("bonyoNyo"))
        self.gridLayout.addWidget(self.bonyoNyo, 0, 2, 1, 1)
        self.why = QtGui.QPushButton(self.centralwidget)
        self.why.setObjectName(_fromUtf8("why"))
        self.gridLayout.addWidget(self.why, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.somboNyo = QtGui.QPushButton(self.centralwidget)
        self.somboNyo.setObjectName(_fromUtf8("somboNyo"))
        self.verticalLayout.addWidget(self.somboNyo)
        self.lulaLula = QtGui.QPushButton(self.centralwidget)
        self.lulaLula.setObjectName(_fromUtf8("lulaLula"))
        self.verticalLayout.addWidget(self.lulaLula)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Broncho", None))
        self.please.setText(_translate("MainWindow", "please", None))
        self.bonyoNyo.setText(_translate("MainWindow", "bonyonyo", None))
        self.why.setText(_translate("MainWindow", "why", None))
        self.somboNyo.setText(_translate("MainWindow", "lulalula", None))
        self.lulaLula.setText(_translate("MainWindow", "sombonyo", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSave.setText(_translate("MainWindow", "save", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionNew.setText(_translate("MainWindow", "new", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

