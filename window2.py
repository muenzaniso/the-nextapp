import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        widget1 = QtWidgets.QDockWidget("Page 1")
        widget1.setWidget(QtWidgets.QLabel("Page 1"))
        widget2 = QtWidgets.QDockWidget("Page 2")
        widget2.setWidget(QtWidgets.QLabel("Page 2"))
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, widget1)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, widget2)

        btn1 = QtWidgets.QPushButton("Page 1")
        btn1.setCheckable(True)
        btn1.setChecked(True)
        btn1.toggled.connect(widget1.setShown)
        widget1.visibilityChanged.connect(btn1.setChecked)
        btn2 = QtWigets.QPushButton("Page 2")
        btn2.setCheckable(True)
        btn2.setChecked(True)
        btn2.toggled.connect(widget2.setShown)
        widget2.visibilityChanged.connect(btn2.setChecked)

        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(btn1)
        hlayout.addWidget(btn2)

        widget = QtWidgets.QWidget()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
