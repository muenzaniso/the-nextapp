from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    '''def initUI(self):
        self.label = QLabel("",self)
        self.label.move(100, 100)

        self.button = QPushButton("click", self)
        self.button.move(100,50)
        self.button.clicked.connect(self.on_click)

        self.setGeometry(500, 150, 200, 200)
        self.show()'''

    def initUI(self):
        '''Display the x and y coordinates of a mouse pointer in a label widget'''
        grid = QGridLayout()

        x = 0
        y = 0
        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def on_click(self):
        self.label.setText("Hello")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.on_click()

    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())