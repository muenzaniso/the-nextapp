import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import ship

MAC = "qt_mac_set_native_menubar" in dir()

class MainForm(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super (MainForm, self).__init__(parent)

        self.model = ship.ShipTableModel("ships.dat")
        tableLabel1 =QtWidgets.QLabel("Table &1")
        self.tableView1  = QtWidgets.QTableView()
        tableLabel1.setBuddy(self.tableView1)
        self.tableView1.setModel(self.model)
        tableLabel2 =QtWidgets.QLabel("Table &2")
        self.tableView2 = QtWidgets.QTableView()
        tableLabel2.setBuddy(self.tableView2)
        self.tableView2.setModel(self.model)

        addShipButton = QtWidgets.QPushButton("&Add Ship")
        removeShipButton = QtWidgets.QPushButton("&Remove Ship")
        quitButton = QtWidgets.QPushButton("&Quit")

        if not MAC:
            addShipButton.setFocusPolicy(QtCore.Qt.NoFocus)
            removeShipButton.setFocusPolicy(QtCore.Qt.NoFocus)
            quitButton.setFocusPolicy(QtCore.Qt.NoFocus)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(tableLabel1)
        vBox.addWidget(self.tableView1)
        widget = QtWidgets.QWidget()
        widget.setLayout(vBox)
        splitter.addWidget(widget)

        vBox1 = QtWidgets.QVBoxLayout()
        vBox1.addWidget(tableLabel2)
        vBox1.addWidget(self.tableView2)
        widget1 = QtWidgets.QWidget()
        widget1.setLayout(vBox1)
        splitter.addWidget(widget1)

        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(addShipButton)
        buttonLayout.addWidget(removeShipButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(quitButton)

        # Combine splitter and buttons into one layout

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(splitter)
        layout.addLayout(vBox)
        layout.addLayout(vBox1)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

        # connections
        for tableView in (self.tableView1, self.tableView2):
            header = tableView.horizontalHeader()#wen we use the custom model we must handle sorting ourselve
            header.clicked.connect(self.sortTable)
        addShipButton.clicked.connect(self.addShip)
        removeShipButton.clicked.connect(self.removeShip)
        removeShipButton.clicked.connect(self.accept)
        self.setWindowTitle("Ships (model)")

    def accept(self):
        if self.model.dirty and \
            QtWidgets.QMessageBox.question(self, "Ships - Save?",
                                "Save un saved changes?",
                                QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes:
            try:

                self.model.save()
            except IOError as e:

                QtWidgets.QMessageBox.warning(self, "Ships- Error",
                                          "Failed to save: {}".format(e))

            QtWidgets.QDialog.accept()

    def sortTable(self, section):
        if section in (ship.OWNER, ship.COUNTRY):
            self.model.sortByCountryOwner()
        else:
            self.model.sortByName()
        self.resizeColumns()

    def resizeColumns(self):
        for tableView in (self.tableView1, self.tableView2):
            for column in (ship.NAME, ship.OWNER, ship.COUNTRY,
                           ship.TEU):
                tableView.resizeColumnToContents(column)


    def addShip(self):
        row = self.model.rowCount()
        self.model.insertRows(row)
        index = self.model.index(row, 0)
        tableView = self.tableView1
        if self.tableView2.hasFocus():
            tableView = self.tableView2
        tableView.setFocus()
        tableView.setCurrentIndex(index)
        tableView.edit(index)

    def removeShip(self):
        tableView = self.tableView1
        if self.tableView2.hasFocus():
            tableView = self.tableView2
        index = tableView.currentIndex()
        if not index.isValid():
            return
        row = index.row()
        name = self.model.data(
            self.model.index(row,ship.NAME)).toString()
        owner = self.model.data(
            self.model.index(row, ship.OWNER)).toString()
        country = self.model.data(
            self.model.index(row, ship.COUNTRY)).toString()
        if (QtWidgets.QMessageBox.question(self, "Ships - Remove",
            "Remove {} of {}/{}?".format(name,owner,country),
            QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No) ==
            QtWidgets.QMessageBox.No):
            return
        self.model.removeRows(row)
        self.resizeColumns()

if __name__== '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Ship")
    Mainform = MainForm()
    Mainform.show()
    sys.exit(app.exec_())


