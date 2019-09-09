import re

from PyQt4 import QtCore
from PyQt4 import QtGui
MAC = "qt_mac_set_native_menubar" in dir()
import findword

class FindAndReplaceDlg(QtGui.QDialog,findword.Ui_FindAndReplaceDig):

    def __init__(self, text, parent=None):
        super(FindAndReplaceDlg,self).__init__(parent)
        self.__text = text
        self.__index = 0
        self.setupUi(self)

        if not MAC:
            self.findButton.setFocusPolicy(QtCore.NoFocus)
            self.replaceButton.setFocusPolicy(QtCore.NoFocus)
            self.replaceAllButton.setFocusPolicy(QtCore.NoFocus)
            self.closeButton.setFocusPolicy(QtCore.NoFocus)
        self.updateUi()


    def on_findLineEdit_textEdited(self, text):
        self.__index = 0
        self.updateUi()

    def updateUi(self):
        enable = not self.findLineEdit.text().isEmpty
        self.findButton.setEnabled(enable)
        self.replaceButton.setEnabled(enable)
        self.replaceAllButton.setEnabled(enable)


    def text(self):
        return self.__text

    


