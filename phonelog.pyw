from entrypage import phiri
from entrypage import Ui_Dialog
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtSql
import psycopg2

print(phiri)
class PhoneLogDlg(QtGui.QDialog):
    FIRST , PREV, NEXT, LAST = range(4)


    def __init__(self, parent=None):
        super(PhoneLogDlg, self).__init__(parent)
        DATETIME_FORMAT = "yyyy-MM-dd hh:mm"
        self.setGeometry(400, 100, 300, 200)
        self.setWindowTitle("Phone Log")

        callerLabel = QtGui.QLabel("&Caller")
        self.callerEdit = QtGui.QLineEdit()
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(3)
        self.grid.addWidget(callerLabel, 1,0)
        self.grid.addWidget(self.callerEdit,1, 1, 1, 4)
        callerLabel.setBuddy(self.callerEdit)
        today = QtCore.QDate.currentDate()
        startLabel = QtGui.QLabel("&Start:")
        self.startDateTime = QtGui.QDateTimeEdit()
        self.grid.addWidget(startLabel, 2, 0)
        self.grid.addWidget(self.startDateTime, 2, 1)
        startLabel.setBuddy(self.startDateTime)
        self.startDateTime.setDateRange(today, today)
        self.startDateTime.setDisplayFormat(DATETIME_FORMAT)
        endLabel = QtGui.QLabel("&End:")
        self.endDateTime = QtGui.QDateTimeEdit()
        self.grid.addWidget(endLabel,2 ,2)
        self.grid.addWidget(self.endDateTime,2, 3)
        endLabel.setBuddy(self.endDateTime)
        self.endDateTime.setDisplayFormat(DATETIME_FORMAT)
        topicLabel = QtGui.QLabel("&Topic:")
        self.topicEdit = QtGui.QLineEdit()
        topicLabel.setBuddy(self.topicEdit)
        self.grid.addWidget(topicLabel,3, 0)
        self.grid.addWidget(self.topicEdit,3, 1, 1, 4)
        firstButton = QtGui.QPushButton()
        firstButton.setIcon(QtGui.QIcon("/first.png"))
        self.grid.addWidget(firstButton,4 ,0)
        secondButton = QtGui.QPushButton()
        secondButton.setIcon(QtGui.QIcon("/2nd.png"))
        self.grid.addWidget(secondButton, 4, 1)
        thirdButton = QtGui.QPushButton()
        thirdButton.setIcon(QtGui.QIcon("/3rd.png"))
        self.grid.addWidget(thirdButton, 4, 2)
        forthButton = QtGui.QPushButton()
        forthButton.setIcon(QtGui.QIcon("/4th.png"))
        self.grid.addWidget(forthButton, 4, 3)
        addButton = QtGui.QPushButton()
        addButton.setText("&add")
        addButton.setIcon(QtGui.QIcon("/add.png"))
        self.grid.addWidget(addButton,1,5)
        deleteButton = QtGui.QPushButton()
        deleteButton.setText("&delete")
        deleteButton.setIcon(QtGui.QIcon("/delete.png"))
        self.grid.addWidget(deleteButton, 2, 5)
        quitButton = QtGui.QPushButton()
        quitButton.setText("&quit")
        quitButton.setIcon(QtGui.QIcon("/quit.png"))
        self.grid.addWidget(quitButton, 4, 5)
        self.setLayout(self.grid)

        ####Model

        self.model = QtSql.QSqlTableModel(self)#create a QSqlTableModel
        self.model.setTable("calls")#tell the model which table it is to work on
        self.model.setSort(Ui_Dialog.STARTTIME, QtCore.Qt.AscendingOrder)#choose to apply a sort order to e table
        self.model.select()#call select() to make it populate itself with data

        self.mapper = QtGui.QDataWidgetMapper(self)#LINK WIDGETS AND A MODEL
        self.mapper.setSubmitPolicy(not QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.callerEdit, Ui_Dialog.CALLER)
        self.mapper.addMapping(self.startDateTime, Ui_Dialog.STARTTIME)
        self.mapper.addMapping(self.endDateTime, Ui_Dialog.ENDTIME)
        self.mapper.addMapping(self.topicEdit, Ui_Dialog.ENDTIME)
        self.mapper.toFirst()

        firstButton.clicked.connect(lambda: self.saveRecord(PhoneLogDlg.FIRST))#
        secondButton.clicked.connect(lambda: self.saveRecord(PhoneLogDlg.PREV))
        thirdButton.clicked.connect(lambda: self.saveRecord(PhoneLogDlg.NEXT))
        forthButton.clicked.connect(lambda: self.saveRecord(PhoneLogDlg.LAST))
        addButton.clicked.connect(self.addRecord)
        deleteButton.clicked.connect(self.deleteRecord)
        quitButton.clicked.connect(self.accept)


    def accept(self):
        self.mapper.submit()
        QtGui.QDialog.accept(self)

    def saveRecord(self, where):
        row = self.mapper.currentIndex()
        self.mapper.submit()
        if where == PhoneLogDlg.FIRST:
            row = 0
        elif where == PhoneLogDlg.PREV:
            row = 0 if row <= 1 else row-1
        elif where == PhoneLogDlg.NEXT:
            row += 1
            if row >= self.model.rowCount():
                row = self.model.rowCount()-1
        elif where == PhoneLogDlg.LAST:
            row = self.model.rowCount() -1
        self.mapper.setCurrentIndex(row)

    def addRecord(self):
        row = self.model.rowCount()


    def deleteRecord(self):
        caller = self.callerEdit.text()



if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = PhoneLogDlg()
    form.show()
    app.exec_()