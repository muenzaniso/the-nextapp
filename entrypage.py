# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrypage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


import psycopg2
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
import mysql.connector as mysqldb



phiri = 2
'''conn = psycopg2.connect(
    database = "mi database",
    user = "postgres",
    password = "jpmzcastab",
    host = "localhost",
    port = "5432"
)
cur = conn.cursor()'''

####database
db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("Mi database")
db.open()
if not db.open():
    QtWidgets.QMessageBox.critical(None, QtWidgets.qApp.tr("Cannot open database"),
                              QtWidgets.qApp.tr("Unable to establish a database connection \n"
                                            "This example needs SQLite support. Please read "
                                            "the Qt SQL driver documentation for information "
                                            "how to build it.\n\n" "Click Cancel to exit."),
                               QtWidgets.QMessageBox.Cancel)
    import sys
    sys.exit(1)

else:
    print("shit happens")


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

try:
    from PyQt4.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QtCore.QString = type("")

class Ui_Dialog(object):
    james = 1
    def setupUi(self, MainWindow):
        Dialog.setObjectName(_fromUtf8("Mainindow"))
        Dialog.resize(600, 550)

        self.filename = None
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout.addLayout(self.verticalLayout_2, 10, 6, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addLayout(self.verticalLayout, 6, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setObjectName(_fromUtf8("exit"))
        self.gridLayout.addWidget(self.exit, 10, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout.addWidget(self.lineEdit_6, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 5, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 2, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 4, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout.addWidget(self.lineEdit_9, 3, 5, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 5, 4, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 5, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout.addWidget(self.lineEdit_7, 5, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 10, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 10, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 6, 1, 1)
        """List View"""
        listLabel = QtWidgets.QLabel("&Name")
        self.listWidget = QtWidgets.QListWidget()
        listLabel.setBuddy(self.listWidget)
        self.gridLayout.addWidget(listLabel,11,1,1,1)
        self.gridLayout.addWidget(self.listWidget,12,1)
        self.model = QtGui.QStandardItemModel()


        """Tableview"""
        tableLabel = QtWidgets.QLabel("&Name")
        self.tableWidget = QtWidgets.QTableWidget()
        tableLabel.setBuddy(self.tableWidget)
        self.gridLayout.addWidget(tableLabel, 11, 2)
        self.gridLayout.addWidget(self.tableWidget,12,2)



        for inputiline in (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),
                           self.lineEdit_5.text(), self.lineEdit_6.text(),
                           self.lineEdit_7.text()):
            print(inputiline)
        parent1 = QtGui.QStandardItem()
        self.model.appendRow(parent1)


        self.label_3.setBuddy(self.lineEdit_3)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_8.setBuddy(self.comboBox_2)
        self.label_4.setBuddy(self.lineEdit_4)
        self.label.setBuddy(self.lineEdit)
        self.label_6.setBuddy(self.lineEdit_6)
        self.label_7.setBuddy(self.comboBox)
        self.label_9.setBuddy(self.lineEdit_9)
        self.label_5.setBuddy(self.lineEdit_5)
        self.label_10.setBuddy(self.lineEdit_7)

        self.exit.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.insertData)

        """Capturing data from input"""

        for inputiline in (self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
                           self.lineEdit_5, self.lineEdit_6,
                           self.lineEdit_7):
            inputiline.selectAll()
            #self.treeView.addTopLevelItems("inputiline")

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButton_3.close)
        #QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("destroyed()")), self.pushButton_3.click)
        #QtCore.QObject.connect(self.treeView, QtCore.SIGNAL(_fromUtf8("destroyed(QObject*)")), self.treeView.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def insertData(self):

        '''query = QtSql.QSqlQuery()

        query.exec_("""CREATE TABLE client_details (
                             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                              name VARCHAR(40) NOT NULL,
                              surname VARCHAR(60) NOT NULL,
                              address  VARCHAR(60) NOT NULL,
                              id_no VARCHAR(20) NOT NULL,
                              title VARCHAR(10) NOT NULL,
                              medical_aid VARCHAR(40) NOT NULL,
                              medical_pack VARCHAR(40) NOT NULL,
                              medical_aid_no VARCHAR(40) NOT NULL,
                              dob DATE NOT NULL)""")'''

        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        address = self.lineEdit_3.text()
        phone_no = self.lineEdit_4.text()
        id_no = self.lineEdit_5.text()
        title = self.lineEdit_6.text()
        medical_aid = self.comboBox
        medical_package = self.comboBox_2
        medicalaid_no = self.lineEdit_9.text()
        date_of_birth = self.lineEdit_7.text()
        if date_of_birth == "":
            date_of_birth="2000/01/01"



        '''query = QtSql.QSqlQuery(db)
        sql = query.exec_("INSERT INTO client_details (name) VALUES ('{0})".format(

            name))
        print(sql)
        query.exec_()
        #query.prepare("INSERT INTO client_details (name, surname, address,"
        #              " phone_no, id_no, title, medical_aid, medicalaid_no, "
        #              "date_of_birth) VALUES (?,?,?,?,?,?,?,?,?)")
        #query.addBindValue(str(name))
        #query.addBindValue(surname)
        #query.addBindValue(address)
        #query.addBindValue(phone_no)
        #query.addBindValue(id_no)
        #query.addBindValue(title)
        #query.addBindValue(medical_aid)
        #query.addBindValue(medical_package)
        #query.addBindValue(medicalaid_no)
        #query.addBindValue(date_of_birth)
        #query.exec_()
        #print(query.addBindValue(name))
        #print("Alana")


    driver = QtSql.QSqlDatabase.database().driver()#Used to check if database supports varios features such as tranctions and BLOBs
    if driver.hasFeature(QtSql.QSqlDriver.Transactions):
        print("Can commit and rollback")'''
        mydbcl = mysqldb.connect(
            host="localhost",
            user="muenza",
            passwd="jpmzcastab29",
            database="mi database"
        )
        print(mydbcl)
        cursor = mydbcl.cursor()
        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())

        query = "INSERT INTO client_details(name,surname,address,id_no,title, phone," \
                "medical_aid_no,dob) VALUES (%s, %s, %s, %s, %s, %s,%s,%s ) "
        values = (name, surname, address, id_no, title, phone_no, medicalaid_no, date_of_birth)

        cursor.execute(query, values)
        mydbcl.commit()
        self.populateList()
        self.populateTable()






    def populateList(self, selectedClient=None):
        self.mydbcl = mysqldb.connect(
            host="localhost",
            user="muenza",
            passwd="jpmzcastab29",
            database="mi database"
        )
        print(self.mydbcl)
        cursor = self.mydbcl.cursor()
        selected = None
        self.listWidget.clear() # we begin by clearing the widget
        results = "SELECT name, surname, phone, dob FROM client_details;"
        cursor.execute(results)
        records = cursor.fetchall()
        for record in records:
            print(record)
            item = QtWidgets.QListWidgetItem("{} of {}/{} {})".format(
                record[0], record[1], record[2], record[3]))
            self.listWidget.addItem(item)
                
    def populateTable(self, selectedClient=None):
        print(self.mydbcl)
        cursor = self.mydbcl.cursor()
        selected = None
        self.tableWidget.clear()  # we begin by clearing the widget
        results = "SELECT name, surname, phone, dob FROM client_details ORDER BY id DESC;"
        cursor.execute(results)
        records = cursor.fetchmany()
        selected = None
        self.tableWidget.clear()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(len(records)) #nof rows
        headers = ["Name", "Surname", "Phone", "Date of Birth"]
        self.tableWidget.setColumnCount(len(headers)) #no of columns
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row,record in enumerate(records):
            print(record)

            item = QtWidgets.QTableWidgetItem(record[0])
            item.setData(QtCore.Qt.UserRole, id(record))
            if selectedClient is not None and selectedClient == id(record):
                selected = item
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(record[0])) #add individual cells
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(record[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(record[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("{}".format(record[3])))
            item.setTextAlignment(QtCore.Qt.AlignCenter)

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.resizeColumnToContents(1)




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Enter details", None))
        self.exit.setText(_translate("Dialog", "Exit", None))
        self.label_3.setText(_translate("Dialog", "Address", None))
        self.label_2.setText(_translate("Dialog", "Surname:", None))
        self.label_8.setText(_translate("Dialog", "Medical Package", None))
        self.label_4.setText(_translate("Dialog", "Phone Number", None))
        self.label.setText(_translate("Dialog", "Name:", None))
        self.label_6.setText(_translate("Dialog", "Title:", None))
        self.label_7.setText(_translate("Dialog", "Medical Aid", None))
        self.label_9.setText(_translate("Dialog", "Medical Aid Number", None))
        self.label_5.setText(_translate("Dialog", "Id Number:", None))
        self.label_10.setText(_translate("Dialog", "Date of birth", None))
        self.pushButton.setText(_translate("Dialog", "Save/Update", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel/Remove", None))

    def close(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

