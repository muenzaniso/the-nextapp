import  numberformatdlgfrom PyQt4 import QtCorefrom PyQt4 import QtGuidef setNumberFomat1(self):    dialog = numberformatdlg.NumberFormatDlg(self.format, self)    if dialog.exec_():        self.format = dialog.numberFomat()        self.refreshTable()