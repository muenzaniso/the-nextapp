import sys
from PyQt5 import QtGui, QtCore, QtWidgets


class Example(QtWidgets.QWidget):

    def __init__(self):
        super(Example,self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Absolute")

        self.initUI()

    def initUI(self):

        jp1 = QtWidgets.QLabel("Jimobho", self)
        jp1.move(15,10)

        jp2 = QtWidgets.QLabel("Andro", self)
        jp2.move(35,40)

        jp3 = QtWidgets.QLabel("Alana", self)
        jp3.move(55,70)

        jp4 = QtWidgets.QLabel("Tarie", self)
        jp4.move(75,100)


        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
