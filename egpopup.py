import sys
from PyQt4 import QtGui
import  newimagedlg

class Image(newimagedlg.NewImageDlg):
    def popup(self):
        dialog = newimagedlg
        print("Its a dialog")
        return dialog


app = QtGui.QApplication(sys.argv)
form = Image()
form.show()
app.exec_()