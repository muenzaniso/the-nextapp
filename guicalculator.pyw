from __future__ import division
import  sys
from math import *
from PyQt4 import QtGui
from PyQt4 import QtCore

class Form(QtGui.QDialog): #by inhereting QDialog we get a gray rectangle
    def __init__(self, parent=None):# A widget that has no parnet becomes a top-levelwindow
        super(Form,self).__init__(parent)
        self.browser = QtGui.QTextBrowser()
        self.lineedit = QtGui.QLineEdit()
        self.lineedit.selectAll()
        layout = QtGui.QVBoxLayout()#used to postion widgets vertically
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()# we want to the focus to start in the QLineEdit
        self.lineedit.returnPressed.connect(self.updateUi)# wen user presses Enter in the QlineEdit the returnPressed signal is emittedand the updateUi called
        self.setWindowTitle("Calculate")

        print(sys.argv)

    def updateUi(self):
        try:
            text =self.lineedit.text()
            self.browser.append("%s = <b>%s</b>"%(text,eval(text)))# eval() to evalualte the string as  an expression

        except:
            self.browser.append("<font color=red>%s is invalid!</font"% text)

app = QtGui.QApplication(sys.argv)# create the QApplication object
form = Form()# instantiate an instance of our form
form.show()# scheduleit to be painted
app.exec()# start off th event loop


