from  __future__ import unicode_literals
import  sys
from PyQt5 import QtGui, QtSql, QtWidgets, QtCore
import ship

'''
def createDB():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName('sports')

    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
          QtGui.qApp.tr("Unable to establish a data connection.\n"
            "Thie eg needs SQlite support\n""Click cancel to exit."),
        QtGui.QMessageBox.Cancel)


        return False


    query = QtSql.QSqlQuery()

    query.exec_("create  table sportsmen(id int primary key, "
                "firstname varchar(20), lastname varchar(20))")

    query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")

    jp = query.exec_("from sportsmen select lastname")
    print(jp)
    print("James")

if __name__== '__main__':
    app = QtGui.QApplication(sys.argv)
    createDB()'''

MAC = True

try:
    from PyQt5.QtWidgets import qt_mac_set_native_menubar
except ImportError:
    MAC = False

def displayFlags(flagDict, flags = None):
    if not flags:
        return  None
    else:
        flagDescriptions = []
        recastFlags = int(flags)  # all flags, cast to integer
        # print "Number of elements in dict: ", len(flagDict)
        for flagInd in range(len(flagDict)):
            flagVal = flagDict.keys()[flagInd]
            if recastFlags & flagVal:
                flagDescriptions.append(flagDict.values()[flagInd])
        return flagDescriptions


class Mainform (QtWidgets.QDialog):
    def __init__(self, parent=None):
        
        super(Mainform, self).__init__()
        self.model = ship.ShipTableModel("ships.dat")
        self.setWindowTitle("Ships (delegate)")
        QtCore.QTimer.singleShot(0, self.initialLoad)

        #create convenience item view widgets
        #QListWidget
        listLabel = QtWidgets.QLabel("&List")
        self.listWidget = QtWidgets.QListWidget()
        listLabel.setBuddy(self.listWidget)

        #QTableWidget
        tableLabel = QtWidgets.QLabel("&Table")
        self.tableWidget = QtWidgets.QTableWidget()
        tableLabel.setBuddy(self.tableWidget)

        #QTreeWidget
        treeLabel = QtWidgets.QLabel("Tre&e")
        self.treeWidget = QtWidgets.QTreeWidget()
        treeLabel.setBuddy(self.treeWidget)

        addShip = QtWidgets.QPushButton("add Ship")
        removeShip = QtWidgets.QPushButton("remove Ship")
        quitButton = QtWidgets.QPushButton("quit")


        #####lAYOUT
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.addWidget(listLabel, 1, 0)
        self.gridLayout.addWidget(self.listWidget, 2, 0)

        self.gridLayout.addWidget(tableLabel, 1, 1)
        self.gridLayout.addWidget(self.tableWidget, 2, 1)

        self.gridLayout.addWidget(treeLabel, 1, 2)
        self.gridLayout.addWidget(self.treeWidget, 2, 2)

        self.gridLayout.addWidget(addShip, 3, 0)
        self.gridLayout.addWidget(removeShip,3 , 1)
        self.gridLayout.addWidget(quitButton, 3, 2)



        self.setLayout(self.gridLayout)
        #connections
        #self.tableWidget.itemChanged(QtWidgets.QTableWidgetItem).connect(self.tableItemChanged) #default of table is it is editable
        addShip.clicked.connect(self.addShip)
        removeShip.clicked.connect(self.removeShip)
        quitButton.clicked.connect(self.accept)

        # self.ships is the dictionary containing all ships  (id is key, value is other data)
        self.ships = ship.ShipContainer("ships.data")
        self.setWindowTitle("Ships (dict)")
        QtCore.QTimer.singleShot(0, self.initialLoad)  # see page 184 of text for why we do this single shot trick

    def initialLoad(self):
        if not QtCore.QFile.exists(self.model.filename):
            for chikepe in ship.generateFakeShips():
                self.ships.addShip(chikepe)
            self.ships.dirty = False
        else:
            try:
                self.ships.load()
            except IOError as e:
                QtWidgets.QMessageBox.warning(self, "Ships - Error,"
                                                    "Failed to load: {}".format(e))
        self.populateList()
        self.populateTable()
        self.tableWidget.sortItems(0)
        self.populataeTree()


    def reject(self):
        self.accept()

    def accept(self):
        if (self.model.dirty and
              QtWidgets.QMessageBox.question(self, "Ships - Save",
                        "Save unsaved changes?",
                          QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No) ==
                          QtWidgets.QMessageBox.Yes):
            try:
                self.model.save()
            except IOError as err:
                QtWidgets.QMessageBox.Warning(self, "Ships - Error",
                        "Failed to save: {0}".format(err))

        QtWidgets.QDialog.accept(self)


    def populateList(self, selectedShip=None):
        selected = None
        self.listWidget.clear()  # we begin by clearing the widget

        for ship in self.ships.inOrder():   # we iterate over every ship in e container, e inOrder() method is by our custom ShipContainer class
            item = QtWidgets.QListWidgetItem("{} of {}/{} ({:,})".format(
                ship.name, ship.owner, ship.country, ship.teu))
            self.listWidget.addItem(item)
            if selectedShip is not None and selectedShip == id(ship):
                selected = item
        if selected is not None:
            selected.setSelected(True)
            self.listWidget.setCurrentItem(selected)

    def populateTable(self, selectedShip=None):
        selected = None
        self.tableWidget.clear()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(len(self.ships))  # we set e number of rows and columns titles
        headers = ["Name", "Owner", "Country", "Description", "Teu"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row, chikepe in enumerate(self.ships):  # enumerate method adds counter to an iterable and returns it
            item = QtWidgets.QTableWidgetItem(chikepe.name)  # ship.name is set to textof item
            item.setData(QtCore.Qt.UserRole, QtCore.QVariant(id(ship)))
            if selectedShip is not None and selectedShip == id(chikepe):
                selected = item
            self.tableWidget.setItem(row, ship.NAME, item)
            self.tableWidget.setItem(row, ship.OWNER,
                        QtWidgets.QTableWidgetItem(chikepe.owner))
            self.tableWidget.setItem(row, ship.COUNTRY,
                    QtWidgets.QTableWidgetItem(chikepe.country)),
            self.tableWidget.setItem(row,ship.DESCRIPTION,
                    QtWidgets.QTableWidgetItem(chikepe.description))
            item = QtWidgets.QTableWidgetItem("{:10}".format(chikepe.teu)
                    )
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row, ship.TEU, item)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.resizeColumnsToContents()
        if selected is not None:
            selected.setSelected(True)
            self.tableWidget.setCurrentItem(selected)

    def populataeTree(self, selectedShip=None):
        selected = None
        self.treeWidget.clear()
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(["Country/Owner/Name/TEU"])
        self.treeWidget.setItemsExpandable(True)
        parentFromCountry = {}
        parentFromCountryOwner = {}

        for ship in self.ships.inCountryOwnerOrder():
            ancestor = parentFromCountry.get(ship.country)
            if ancestor is None:
                ancestor = QtWidgets.QTreeWidgetItem(self.treeWidget,
                                                     [ship.country])
                parentFromCountry[ship.country] = ancestor
            countryowner = ship.country + "/" + ship.owner
            parent = parentFromCountryOwner.get(countryowner)
            if parent is None:
                parent = QtWidgets.QTreeWidgetItem(ancestor, [ship.owner])
                parentFromCountryOwner[countryowner] = parent
            item = QtWidgets.QTreeWidgetItem(parent, [ship.name, "{:,}".format(ship.teu)])
            item.setTextAlignment(1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            if selectedShip is not None and selectedShip == id(ship):
                selected = item
            self.treeWidget.expandItem(parent)
            self.treeWidget.expandItem(ancestor)
            self.treeWidget.resizeColumnToContents(0)
            self.treeWidget.resizeColumnToContents(1)
            if selected is not None:
                selected.setSelected(True)
                self.treeWidget.setCurrentItem(selected)

    def tableItemChanged(self, item):
        ship = self.currentTableShip()
        if ship is None:
            return
        column = self.tableWidget.currentColumn()
        if column == ship.NAME:
            ship.name = item.text().trimmed() # we use trimmed to get rid of any leading and trailing whitespace
        elif column == ship.OWNER:
            ship.owner = item.text().trimmed()
        elif column == ship.COUNTRY:
            ship.country = item.text().trommed()
        elif column == ship.DESCRIPTION:
            ship.descriptio = item.text.trimmed()
        elif column == ship.TEU:
            ship.teu = item.text().toInt()[0]
        self.ships.dirty = True
        self.populateList()
        self.populateTree()

    def currentTableShip(self):
        item = self.tableWidget.item(self.tableWidget.currentRow(), 0)
        if item is None:
            return None
        return self.ships.ship(int(item.data(QtCore.Qt.UserRole)))

    def addShip(self):
        shipjp = ship.Ship(" leandro", " leandro", " leandro")
        self.ships.addShip(shipjp)
        self.populateList()
        self.populataeTree()
        self.populateTable(id(shipjp))
        self.tableWidget.setFocus()
        self.tableWidget.editItem(self.tableWidget.currentItem())

    def removeShip(self):
        shipmj = self.currentTableShip()

        if shipmj is None:
            return
        if (QtWidgets.QMessageBox.question(self, "Ships - Remove",

                                       "Remove {} of {}/{}?".format(shipmj.name, shipmj.owner, shipmj.country),

                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) ==

                QtWidgets.QMessageBox.No):
            return
        self.ships.removeShip(shipmj)

        self.populateList()

        self.populataeTree()

        self.populateTable()






















if __name__== '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Ship")
    Mainform = Mainform()
    Mainform.show()
    sys.exit(app.exec_())



