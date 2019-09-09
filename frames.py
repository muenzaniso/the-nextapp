from PyQt5 import QtGui, QtWidgets, QtCore


class First(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.agree = QtWidgets.QPushButton("Agree", self)
        self.agree.move(180, 400)
        self.button2 = QtWidgets.QPushButton("Disagree", self)
        self.button2.move(270, 400)


class Second(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.btn = QtWidgets.QPushButton("previous", self)
        self.btn.move(100, 350)
        self.greet = QtWidgets.QLabel('second', self)
        self.greet.move(100, 250)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(400, 450)
        self.ToolTab = Second(self)
        self.ToolTab.btn.clicked.connect(self.start_first)
        self.Window = First(self)
        self.Window.agree.clicked.connect(self.start_second)
        self.stack = QtWidgets.QStackedWidget(self)
        self.stack.addWidget(self.ToolTab)
        self.stack.addWidget(self.Window)
        self.setCentralWidget(self.stack)
        self.show()

    def start_second(self):

        self.setWindowTitle('second')
        self.stack.setCurrentIndex(0)

    def start_first(self):

        self.setWindowTitle('first')
        self.stack.setCurrentIndex(1)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
