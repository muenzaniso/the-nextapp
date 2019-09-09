import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(10, 230, 500, 300)
window.setWindowTitle("Jimobho")

window.show()