import sys
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget,QApplication

class Example(QWidget):

    def __init__(self):
        super(Example,self).__init__()

        self.initUI()

    

    def initUI(self):

        okButton = QPushButton("Bhoo",self)
        cancelButton = QPushButton("Ayewa",self)

        hbox = QHBoxLayout() #We create a horizontal box layout and add a stretch factor and both buttons. The stretch adds a stretchable space before the two buttons. This will push them to the right of the window.
        hbox.addStretch(1)#To create the necessary layout, we put a horizontal layout into a vertical one. The stretch factor in the vertical box will push the horizontal box with the buttons to the bottom of the window
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


def main():
    app =QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()