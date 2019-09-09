import sys
'''from PyQt4 import QtGui,QtCore #QtCore to bring funcionality to the buttons


class Window(QtGui.QMainWindow):

    def __init__(self):   #will create a gui window
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Jimobho!")
        self.setWindowIcon(QtGui.QIcon('12.png'))
        self.home()

    def home(self):  #creates a button
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100,100)
        btn.move(100,100)
        self.show()

def run():  
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()'''
import sys
from PyQt4 import QtCore, QtGui
from mainGui import Ui_main
import one


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.ui.oneBtn.clicked.connect(one.One(self).show)
        self.ui.getBtn.clicked.connect(self._get)
        self.ui.sendBtn.clicked.connect(self._send)

    def _get(self):
        print()

    def _send(self):
        one.One.ui.edit.setText('blah')


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

