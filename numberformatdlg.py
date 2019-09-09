from PyQt4 import QtGui
from PyQt4 import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class NumberFormatDlg(QtGui.QDialog):

    def __init__(self, format, parent=None):
        super(NumberFormatDlg, self).__init__()

        thousandsLabel = QtGui.QLabel("&Thusands separator")
        self.thousandsEdit = QtGui.QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        decimalMarkerLabel = QtGui.QLabel("Decimal &marker")
        self.decimalMarkerEdit = QtGui.QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        decimalPlacesLabel = QtGui.QLabel("&Decimal places")
        self.decimalPlacesSpinBox = QtGui.QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
        self.redNegativesCheckBox = QtGui.QCheckBox("&Red negative numbers")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok| QtGui.QDialogButtonBox.Cancel)

        self.format = format.copy()

        grid = QtGui.QGridLayout()
        grid.addWidget(thousandsLabel, 0, 0)
        grid.addWidget(self.thousandsEdit, 0, 1)
        grid.addWidget(decimalMarkerLabel, 1, 0)
        grid.addWidget(self.decimalMarkerEdit, 1, 1)
        grid.addWidget(decimalPlacesLabel, 2, 0)
        grid.addWidget(self.decimalPlacesSpinBox,2, 1)
        grid.addWidget(self.redNegativesCheckBox,3, 0, 1, 2)
        grid.addWidget(buttonBox, 4, 0,1,2)
        self.setLayout(grid)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        applybutton = buttonBox.button(QtGui.QDialogButtonBox.Apply)
        applybutton.clicked.connect(self.applyChanges)

        self.setWindowTitle("Set Number Format (Modal)")

        def numberFormat(self):
            return self.format