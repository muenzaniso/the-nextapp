import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Form(QtGui.QDialog):


    def __init__(self, parent=None):
        super(Form, self).__init__(parent)


        dial = QtGui.QDial()
        dial.setNotchesVisible(True)
        spinbox = QtGui.QSpinBox()

        layout = QtGui.QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        dial.valueChanged.connect(spinbox.setValue)#valueChanged signals are emmiteted by QDial widget with new values and the setValue slots take in the values
        spinbox.valueChanged.connect(dial.setValue)


app = QtGui.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()




