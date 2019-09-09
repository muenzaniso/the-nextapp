import sys
from  PyQt4 import QtGui, QtCore

class Dispense_window(QtGui.QMainWindow, QtGui.QWidget):
    count = 0
    def __init__(self, parent = None):
        super(Dispense_window, self).__init__(parent)
        self.mdi = QtGui.QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()

        file = bar.addMenu("Menu")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QtGui.QAction].connect(self.windowaction)
        self.setWindowTitle("MDI demo")

    def windowaction(self, q):

        print("triggered")


        if q.text()== "New":
            Dispense_window.count = Dispense_window.count + 1
            sub = QtGui.QMdiSubWindow()
            jp = sub.setWidget(QtGui.QTextEdit())
            sub.setWindowTitle("subwindow" + str(Dispense_window.count))
            self.mdi.addSubWindow(sub)
            sub.show()
            

        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()

        if q.text() == "Tiled":
            self.mdi.tileSubWindows()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Dispense_window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()