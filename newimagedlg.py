from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import ui_newimagedlg

__version__ = "1.0.0"

class NewImageDlg(QtWidgets.QDialog, ui_newimagedlg.Ui_NewImageDlg):

    def __init__(self, parent=None):
        '''A super () fxn takes a class & returns e class's base class'''
        super(NewImageDlg, self).__init__(parent)
        self.setupUi(self)

        self.color = QtCore.Qt.red
        for value, text in (
                (QtCore.Qt.SolidPattern, "Solid"),
                (QtCore.Qt.Dense1Pattern, "Dense #1"),
                (QtCore.Qt.Dense2Pattern, "Dense #2"),
                (QtCore.Qt.Dense3Pattern, "Dense #3"),
                (QtCore.Qt.Dense4Pattern, "Dense #4"),
                (QtCore.Qt.Dense5Pattern, "Dense #5"),
                (QtCore.Qt.Dense6Pattern, "Dense #6"),
                (QtCore.Qt.Dense7Pattern, "Dense #7"),
                (QtCore.Qt.HorPattern, "Horizontal"),
                (QtCore.Qt.VerPattern, "Vertical"),
                (QtCore.Qt.CrossPattern, "Cross"),
                (QtCore.Qt.BDiagPattern, "Backward Diagonal"),
                (QtCore.Qt.FDiagPattern, "Forward Diagonal"),
                (QtCore.Qt.DiagCrossPattern, "Diagonal Cross")):
            self.brushComboBox.addItem(text, value)

        self.colorButton.clicked.connect(self.getColor)
        self.brushComboBox.activated.connect(self.setColor)

        self.setColor()
        self.widthSpinBox.setFocus()


    def getColor(self):
        color = QtGui.QColorDialog.getColor(QtCore.Qt.black, self)
        if color.isValid():
            self.color = color
            self.setColor()


    def setColor(self):
        pixmap = self._makePixmap(60, 30)
        self.colorLabel.setPixmap(pixmap)


    def image(self):
        pixmap = self._makePixmap(self.widthSpinBox.value(),
                                  self.heightSpinBox.value())
        return QtGui.QPixmap.toImage(pixmap)


    def _makePixmap(self, width, height):
        pixmap = QtGui.QPixmap(width, height)
        style = self.brushComboBox.itemData(
                self.brushComboBox.currentIndex())
        brush = QtGui.QBrush(self.color, QtCore.Qt.BrushStyle(style))
        painter = QtGui.QPainter(pixmap)
        painter.fillRect(pixmap.rect(), QtCore.Qt.white)
        painter.fillRect(pixmap.rect(), brush)
        return pixmap


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = NewImageDlg()
    form.show()
    app.exec_()