from PyQt5 import QtWidgets, QtCore, QtGui

TITLE, NAME, SURNAME, DOB, PHONE, ADDRESS, CITY = range(7)

class ModelFirst(QtCore.QAbstractTableModel):
    def __init__(self, todos=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        if todos is None:
            todos = [[]]
        self.todos = todos or [] # is our data store



    def data(self, index, role): # index is the position/coordinetes of data which view is requesting
        if role == QtCore.Qt.DisplayRole:  #role  is a flag indicating the type of data view is requesting
            row = index.row()
            column = index.column()
            value = self.todos[row][column]
            return value

    def rowCount(self, index): # gets number of rows in the data
        return len(self.todos)

    def columnCount(self, index):
        return  len(self.todos[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # Returns the data for the given role and section in the header with the specified orientation.
        # For horizontal headers, the section number corresponds to the column number.
        # Similarly, for vertical headers, the section number corresponds to the row number.
        if role == QtCore.Qt.TextAlignmentRole:
            if orientation == QtCore.Qt.Horizontal:
                return int(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            return int(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        if role != QtCore.Qt.DisplayRole:
            return None
        if orientation == QtCore.Qt.Horizontal:
            if section == TITLE:
                return "Title"
            elif section == NAME:
                return "Name"
            elif section == SURNAME:
                return "Surname"
            elif section == DOB:
                return "Date of Birth"
            elif section == PHONE:
                return "Phone"
            elif section == ADDRESS:
                return "Address"
            elif section == CITY:
                return "City"
        return int(section + 1)

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role=QtCore.Qt.EditRole):

        if index.isValid():
            selected_row = index.row()
            selected_column = index.column()
            self.todos[selected_row][selected_column] = value
            self.dataChanged.emit(index, index)
            return True
        else:
            return False
