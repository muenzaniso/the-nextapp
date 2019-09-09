import sys
from PyQt5 import QtGui, QtCore , QtWidgets

#http://stackoverflow.com/questions/36675609/how-can-i-create-multi-page-applications-in-pyqt4/36676917

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        widget1 = QtWidgets.QLabel("Page 1")
        widget2 = QtWidgets.QLabel("Page 2")

        btn1 = QtWidgets.QPushButton("Page 1")
        btn1.setCheckable(True)
        btn1.setChecked(True)
        btn1.toggled.connect(widget1.setShown)
        btn2 = QtWidgets.QPushButton("Page 2")
        btn2.setCheckable(True)
        btn2.setChecked(True)
        btn2.toggled.connect(widget2.setShown)

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(widget1)
        vlayout.addWidget(widget2)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(btn1)
        hlayout.addWidget(btn2)
        vlayout.addLayout(hlayout)

        widget = QtWidgets.QWidget()
        widget.setLayout(vlayout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())