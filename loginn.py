import sysfrom PyQt5 import QtGui, QtCore, QtWidgetsimport mysql.connector as mysqlDbimport nextappclass LoginGUI(QtWidgets.QMainWindow):    another_window = QtCore.pyqtSignal()        def __init__(self):        super(LoginGUI, self).__init__()        self.setGeometry(450, 150, 500, 300)        self.setWindowTitle("Login")        self.initGUI()    def initGUI(self):        self.titleLabel = QtWidgets.QLabel("Login", self)        self.titleLabel.move(200, 20)        self.titleLabel.setFont(QtGui.QFont("", 20))        self.loginLabel = QtWidgets.QLabel("Username: ", self)        self.loginLabel.move(135, 120)        self.passwordLabel = QtWidgets.QLabel("Password: ", self)        self.passwordLabel.move(135, 150)        self.loginText = QtWidgets.QPlainTextEdit("", self)        self.loginText.move(195, 120)        self.passwordText = QtWidgets.QLineEdit("", self)        self.passwordText.move(195, 150)        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)        self.loginBtn = QtWidgets.QPushButton("Sign in", self)        self.loginBtn.clicked.connect(lambda:                                 self.connectToDB(self.loginText.toPlainText(), self.passwordText.text()))        self.loginBtn.resize(self.loginBtn.sizeHint())        self.loginBtn.move(170, 250)        self.quitBtn = QtWidgets.QPushButton("Quit", self)        self.quitBtn.clicked.connect(QtWidgets.QApplication.instance().quit)        self.quitBtn.resize(self.quitBtn.sizeHint())        self.quitBtn.move(245, 250)        self.show()    def connectToDB(self, username, password):        mydb = mysqlDb.connect(             host="localhost",             user="muenza",             passwd="jpmzcastab29",             database="login"                 )        cursor = mydb.cursor()        query = "SELECT username, password FROM multiplywindows"        cursor.execute(query)        result = cursor.fetchone()        print(result)        if username == "james" and password == "12345":            self.another_window.emit()class MainGui(QtWidgets.QMainWindow):    another_window = QtCore.pyqtSignal()    def __init__(self):        super(MainGui, self).__init__()        self.setGeometry(730, 350, 600, 400)        self.setWindowTitle('Inside')    def maingui(self):        self.another_window.emit()class Controller:    def __init__(self):        pass    def show_login(self):        self.loginn = LoginGUI()        self.loginn.another_window.connect(self.show_maingui)        self.loginn.show()    def show_maingui(self):        self.window = QtWidgets.QMainWindow()        self.maingui = nextapp.Ui_MainWindow()        self.loginn.close()        self.maingui.setupUi(self.window)        self.window.show()def main():    app = QtWidgets.QApplication(sys.argv)    controller = Controller()    controller.show_login()    sys.exit(app.exec_())if __name__ == '__main__':    main()