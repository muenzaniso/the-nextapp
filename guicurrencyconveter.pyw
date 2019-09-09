import sys
import urllib # will grab a file over the internet
from PyQt4 import QtGui
from PyQt4 import QtCore

class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)#initialise form using super()

        date = self.getdata()# method gets the exchange rates
        rates = sorted(self.rates.keys())#Take the sorted copy of the dictionary's keys

        dateLabel = QtGui.QLabel(date)
        self.fromComboBox = QtGui.QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QtGui.QDoubleSpinBox()# handles floating-point values
        self.fromSpinBox.setRange(0.01, 10000000.00)# good practice to always set a spinbox's  range before setting its value
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QtGui.QComboBox()
        self.toComboBox.addItems(rates)
        dial = QtGui.QDial()
        dial.setNotchesVisible(True)
        self.toLabel = QtGui.QLabel("1.00")

        grid = QtGui.QGridLayout()
        grid.addWidget(dateLabel,0,0)
        grid.addWidget(self.fromComboBox,1,0)
        grid.addWidget(self.fromSpinBox,1,1)
        grid.addWidget(self.toComboBox,2,0)
        grid.addWidget(self.toLabel,2,1)
        grid.addWidget(dial,2,2)
        self.setLayout(grid)

        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        self.toComboBox.currentIndexChanged.connect(self.updateUi)
        self.fromSpinBox.valueChanged.connect(self.updateUi)
        self.setWindowTitle("Currency")

    def updateUi(self):
        to = self.toComboBox.currentText()
        from_ = self.fromComboBox.currentText()
        amount = (self.rates[from_]/ self.rates[to])* self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" % amount)

    def getdata(self): # idea taken from the python Cookbook
        self.rates = {}
        try:
            date = "Unknown"
            fh = urllib.urlopen("https://www.bankofcanada.ca/valet/observations/FXCADUSD/csv")

            for line in fh:
                if not line or line.startswith(("#", "Closing")):
                    continue
                fields = line.split(",")

                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[(fields[0])] = value
                    except ValueError:
                        pass

            return "Exchange Rates Date: " + date
        except Exception:
            return "Failed to download:\n"



app = QtGui.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
