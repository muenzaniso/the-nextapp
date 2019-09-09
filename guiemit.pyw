import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class TaxRate(QtCore.QObject):

    def __init__(self, parent=None):
        super(TaxRate, self).__init__(parent)
        self.__rate = 17.5


    def rate(self):
        return self.__rate

    def setRate(self, rate):
        if rate != self.__rate:
            self.__rate = rate
            self.emit("rateChanged",self.__rate)


    def rateChanged(value):
        print("TaxRate changed to %.2f%%" % value)


app = QtGui.QApplication(sys.argv)
tax = TaxRate()
tax.show()
app.exec_()
