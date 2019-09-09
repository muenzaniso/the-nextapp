from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class myListWidget(QtGui.QListWidget):

   def Clicked(self,item):
      QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
		
def main():
   items = ["James", "Muenzaniso", "Phiri", "Zatha"]
   for jp in items:
      print (jp)
   app = QApplication(sys.argv)
   listWidget = myListWidget()
	
   #Resize width and height
   listWidget.resize(300,120)
   for item in items:
      listWidget.addItem(item)
   listWidget.addItem("Item 2");
   listWidget.addItem("Item 3");
   listWidget.addItem("Item 4");
	
   listWidget.setWindowTitle('PyQT QListwidget Demo')
   listWidget.itemClicked.connect(listWidget.Clicked)
   
   listWidget.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
