# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextapp.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtGui, QtCore , QtWidgets
import  frontwidget1
import firstpage
import newimagedlg
import ui_newimagedlg
import resourcenextapp
import entrypage

print("Life goes on")

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
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowIcon(QtGui.QIcon("nextappimages/windowicon.jpg"))
        MainWindow.resize(1400, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuViem = QtWidgets.QMenu(self.menubar)
        self.menuViem.setObjectName(_fromUtf8("menuViem"))
        self.menuEdit_2 = QtWidgets.QMenu(self.menubar)
        self.menuEdit_2.setObjectName(_fromUtf8("menuEdit_2"))
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.showMessage("Ready", 5000)
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)

        #Actions

        newFileAction = self.createAction("&New File", self.newFile,
                                          QtGui.QKeySequence.New, "file", "create a file")
        quitFileAction = self.createAction("&Exit", self.close, "Ctrl + Q",
                                           "fileexit", "Close the application")
        printFileAction = self.createAction("&Print", self.printFile,
                                            QtGui.QKeySequence.Print, "printfile", "Print the image")

        '''Add filemenuactions'''

        self.fileMenuActions = (newFileAction, quitFileAction, printFileAction)

        ''' Add editmenuactions'''
        editUndoAction = self.createAction("Undo", self.undo, "Ctrl + Z",
                                          "undo-icon", "Revert to previous action")
        editRedoAction = self.createAction("Redo", self.redo, "Ctrl + Shift + Z",
                                           "redo-icon", "")
        snapeShotAction = self.createAction("SnapeShot", self.snapeshot, "",
                                            "snape-icon", "Take a Snapshot")


        fileText = "file area"
        self.menuFile.setToolTip(fileText)
        self.menuFile.setStatusTip(fileText)
        self.newFileAction = QtWidgets.QAction(MainWindow)
        self.newFileAction.setIcon(QtGui.QIcon("nextappimages/dispence1.jpg"))
        self.newFileAction.setObjectName(_fromUtf8("newFileAction"))
        self.newFileAction.setShortcut("Ctrl+N")
        self.newFileAction.setStatusTip("Open new file")
        self.printFileAction = QtWidgets.QAction(MainWindow)
        self.printFileAction.setIcon(QtGui.QIcon("nextappimages/printer.png"))
        self.printFileAction.setObjectName(_fromUtf8("printFileAction"))
        self.printFileAction.setShortcut("Ctrl+P")
        self.printFileAction.setStatusTip("Reprint")
        self.quotation =  QtWidgets.QAction(MainWindow)
        self.quotation.setObjectName(_fromUtf8("quotation"))
        self.quotation.setIcon(QtGui.QIcon("nextappimages/quote.png"))
        self.quotation.setShortcut("Ctrl+F4")
        self.quotation.setStatusTip("Quotation")
        self.quitFileAction = QtWidgets.QAction(MainWindow)
        self.quitFileAction.setIcon(QtGui.QIcon("nextappimages/close.png"))
        self.quitFileAction.setObjectName(_fromUtf8("quitFileAction"))
        self.quitFileAction.setShortcut("Ctrl+Q")
        self.quitFileAction.setStatusTip("Quit Application")
        self.editUndoAction = QtWidgets.QAction(MainWindow)
        self.editUndoAction.setObjectName(_fromUtf8("editUndoAction"))
        self.editRedoAction = QtWidgets.QAction(MainWindow)
        self.editRedoAction.setObjectName(_fromUtf8("editRedoAction"))
        self.snapShotAction = QtWidgets.QAction(MainWindow)
        self.snapShotAction.setIcon(QtGui.QIcon("nextappimages/snapeshot.jpg"))
        self.snapShotAction.setObjectName(_fromUtf8("snapShotAction"))
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuViem.menuAction())
        self.menubar.addAction(self.menuEdit_2.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        #Add actions to menu
        self.menuFile.addAction(self.newFileAction)
        self.menuFile.addAction(self.printFileAction)
        self.menuFile.addAction(self.quitFileAction)
        self.menuEdit_2.addAction(self.editUndoAction)
        self.menuEdit_2.addAction(self.editRedoAction)
        self.menuEdit_2.addAction(self.quotation)
        self.menuEdit_2.addAction(self.snapShotAction)
        """Add toolbar actions"""
        self.toolBar.addAction(self.newFileAction)
        self.toolBar.addAction(self.printFileAction)
        self.toolBar.addAction(self.snapShotAction)
        self.toolBar.addAction(self.quotation)


        """ add triggers"""
        self.newFileAction.triggered.connect(self.newFile)
        self.quitFileAction.triggered.connect(self.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Nextapp", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Home", None))
        self.menuViem.setTitle(_translate("MainWindow", "View", None))
        self.menuEdit_2.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.editUndoAction.setText(_translate("MainWindow", "Undo", None))
        self.newFileAction.setText(_translate("MainWindow", "New File", None))
        self.printFileAction.setText(_translate("MainWindow", "Reprint", None))
        self.quitFileAction.setText(_translate("MainWindow", "Quit", None))
        self.editRedoAction.setText(_translate("MainWindow","Redo", None))
        self.snapShotAction.setText(_translate("MainWindow", "SnapShot", None))
        self.quotation.setText(_translate("Mainwindow", "Quotation",None))





    """Creation of a helper method to fast track action creation"""
    def createAction(self, text, slot=None, shortcut=None,
                     icon=None, tip=None, signal="triggered"):
        action = QtWidgets.QAction(icon)
        if icon is not None:
            action.setIcon(QtGui.QIcon(":/{0}jpg".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            getattr(action, signal).connect(slot)
        return action

    def newFile(self):
        self.form = QtWidgets.QWidget()
        #self.front = frontwidget1.Ui_Form()
        #self.front.setupUi(self.form)
        #self.form.show()
        self.firstpg = firstpage.Controller()
        self.firstpg.show_entry()



        print("Opening New Dialog")

    def close(self):
        sys.exit()

    def printFile(self):
        pass

    def undo(self):
        pass
    def redo(self):
        pass
    def snapeshot(self):
        pass
'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''

