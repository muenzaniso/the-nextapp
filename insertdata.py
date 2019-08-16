import  sys
from PyQt5 import QtWidgets, QtCore, QtGui, QtSql
import mysql.connector as mysqlDb



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Inseert data"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):

        self.lineedit1 = QtWidgets.QLineEdit(self)
        self.lineedit1.setPlaceholderText("Please Enter Your Name")
        self.lineedit1.setGeometry(200,100,200,30)

        self.lineedit2 = QtWidgets.QLineEdit(self)
        self.lineedit2.setPlaceholderText("Please Enter Your Email")
        self.lineedit2.setGeometry(200, 150, 200, 30)

        self.lineedit3 = QtWidgets.QLineEdit(self)
        self.lineedit3.setPlaceholderText("Please Enter Your Phone Number")
        self.lineedit3.setGeometry(200, 200, 200, 30)

        self.button = QtWidgets.QPushButton("Insert Data", self)
        self.button.setGeometry(200,250, 100, 30)

        self.button.clicked.connect(self.insertData)

        self.setWindowIcon(QtGui.QIcon("fuck.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

    def insertData(self):
        '''db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(" Mi database")
        db.open()
        if not db.open():
            QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Cannot open database"),
                                           QtWidgets.qApp.tr("Unable to establish a database connection \n"
                                                             "This example needs SQLite support. Please read "
                                                             "the Qt SQL driver documentation for information "
                                                             "how to build it.\n\n" "Click Cancel to exit."),
                                           QtWidgets.QMessageBox.Cancel)
            sys.exit(1)

        query = QtSql.QSqlQuery()
        query.exec_("INSERT INTO adata(name,email,phone)"
                    " VALUES('%s','%s','%s')" % (''.join(self.lineedit1.text()),
                                             ''.join(self.lineedit2.text()),
                                             ''.join(self.lineedit3.text())))

        QtWidgets.QMessageBox.about(self,'Connection', 'Data Inserted Successfully')
        query.exec_()'''
        mydb = mysqlDb.connect(
            host="localhost",
            user="muenza",
            passwd="jpmzcastab29"
        )
        print(mydb)

        ## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'

        cursor = mydb.cursor()

        #cursor.execute("CREATE DATABASE credentials")

        cursor.execute("SHOW DATABASES")
        ## 'fetchall()' method fetches all the rows from the last executed statement
        databases = cursor.fetchall()  ## it returns a list of all databases present


        print(databases)

        mydb = mysqlDb.connect(
            host="localhost",
            user="muenza",
            passwd="jpmzcastab29",
            database="credentials"
        )
        print(mydb)
        cursor = mydb.cursor()

        ## creating a table called 'users' in the 'credentials' database
        #cursor.execute("CREATE TABLE users (name VARCHAR(255), mail VARCHAR(255), foneNo INTEGER(30))")

        cursor.execute("SHOW TABLES")

        tables = cursor.fetchall()  ## it returns list of tables present in the database
        print(tables)
        ## showing all the tables one by one

        for table in tables:
            print(table)

        ## defining the Query
        query = "INSERT INTO users (name, mail, foneNo) VALUES (%s, %s, %s)"
        ## storing values in a variable
        values = (self.lineedit1.text(), self.lineedit2.text(), self.lineedit3.text())

        ## executing the query with values
        cursor.execute(query, values)

        ## to make final output we have to run the 'commit()' method of the database object
        mydb.commit()

        print(cursor.rowcount, "record inserted")
        self.lineedit1.clear()
        self.lineedit2.clear()
        self.lineedit3.clear()

    def keyPressEvent(self, event):

        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()


if  __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
