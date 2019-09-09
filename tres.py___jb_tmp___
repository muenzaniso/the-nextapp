import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from layout4 import Example



class Window(QtGui.QMainWindow,QtGui.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Jimobho!")
        self.setWindowIcon(QtGui.QIcon('12.png'))


        # menu
        ''''First, we define the label itself for the menu object.
        Next, we set a shortcut to that menu item if we want.
        Then we set a status tip informational message.
        Then finally we define what we want to do if clicked.'''
        
        extractAction = QtGui.QAction("&Ngatibudei fast team!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        extractAction1 = QtGui.QAction("&Save!!!", self)
        extractAction1.setShortcut("Ctrl+S")
        extractAction1.setStatusTip('Save data')
        #extractAction1.triggered.connect(self.save_data)

        self.statusBar()
        

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(extractAction1)
        
        self.home()
        
    def home(self):

        jp2 = QtGui.QLabel("Andro", self)
        jp2.move(35, 40)

        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(180, 80)

        btn1 = QtGui.QPushButton("Dispense", self)
        btn1.clicked.connect(self.open_newwindow)
        btn1.resize(btn1.sizeHint())
        btn1.move(100, 80)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 150)

        #Toolbar
        extractAction = QtGui.QAction(QtGui.QIcon('pills.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")

        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        # self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

       # fontColor = QtGui.QAction('Font bg Color', self)
       # fontColor.triggered.connect(self.color_picker)

        #self.toolBar.addAction(fontColor)
        #checkbox

        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)
        # depending on what you want the default to be.
        # checkBox.toggle()


        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 240, 250, 20)

        self.btn = QtGui.QPushButton('Download', self)
        self.btn.move(200, 270)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Windows Vista", self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.move(400, 70)

        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)


        self.show()

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Are you sure you want to quit!',
                                            "App still open?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Closing....")
            sys.exit()
        else:

            pass



    def open_newwindow(self):
       ''' text, ok = QtGui.QInputDialog.getText(self, 'Pharmacist',
                                              'Enter your name')


        if ok:
            self.le.setText(str(text))'''

       Example()



def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
