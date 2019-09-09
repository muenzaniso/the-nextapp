import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class PaletteListModel(QtCore.QAbstractListModel):

    def __init__(self, color=[], parent=None):
        QtCore.QAbstractListModel.__init__(self,parent)
        self.color = color

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str("Palette")
            else:
                return "color"

    def rowCount(self, parent):
        return len(self.color)

    def data(self, index, role):

        if role == QtCore.Qt.EditRole:
            return self.color[index.row()].name()

        if role == QtCore.Qt.ToolTipRole:
            return "Hex Code: " + self.color[index.row()].name()

        if role == QtCore.Qt.DecorationRole:

             row = index.row()
             value = self.color[row]

             pixmap = QtGui.QPixmap(26, 26)
             pixmap.fill(value)

             icon = QtGui.QIcon(pixmap)

             return icon



        if role == QtCore.Qt.DisplayRole:

            row = index.row()
            value = self.color[row]
            return value.name()

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role=QtCore.Qt.EditRole):

        if role == QtCore.Qt.EditRole:
            row = index.row()
            color = QtGui.QColor(value)

            if color.isValid():
                self.color[row] = color
                self.dataChanged.emit(index, index)

                return True

        return False

    def insertRows(self, position, rows, parent):
        self.beginInsertRows(QtCore.QModelIndex(), position, position+rows-1)

        for i in range(rows):
            self.color.insert(position, QtGui.QColor("#000000"))

        self.endInsertRows()

        return  True


    def removeRows(self, position, row, parent):
        self.beginRemoveRows()

        self.endRemoveRows()

if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("plastique")

    # ALL OUR VIEWS
    listView = QtWidgets.QListView()
    listView.show()

    treeView = QtWidgets.QTreeView()
    treeView.show()

    combobox = QtWidgets.QComboBox()
    combobox.show()

    tableView = QtWidgets.QTableView()
    tableView.show()

    red = QtGui.QColor(255,0,0)
    green = QtGui.QColor(0,255,0)
    blue = QtGui.QColor(0,0,255)
    anocolor = QtGui.QColor(1,257,89)

    model = PaletteListModel([red, green,blue, anocolor])

    listView.setModel(model)
    treeView.setModel(model)
    combobox.setModel(model)
    tableView.setModel(model)

    model.insertRows(2, 5, QtCore.QModelIndex())

    sys.exit(app.exec())