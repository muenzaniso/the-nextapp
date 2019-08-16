import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QLineEdit, QTableView, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from pagedispense import Ui_MainWindow


class FirstPage(QWidget):
    switch_window = pyqtSignal()
    def __init__(self, parent=None):
        super(FirstPage, self).__init__(parent)
        self.setWindowTitle("Enter Details")
        #self.setGeometry(300, 250, 500, 350)
        self .setFixedSize(800,500)

        self.initGui()

    def initGui(self):


        name_label = QLabel('Name',self)
        surname_label =QLabel('Surname', self)
        title_label = QLabel('Title', self)
        address_label = QLabel('Address', self)
        city_label = QLabel('City', self)
        phone_label = QLabel('Phone', self)
        med_aid_label = QLabel('Medical Aid', self)
        med_aidno_label = QLabel('Medical Aid No', self)
        med_aidnopack_label = QLabel('Medical Aid Pack', self)
        birth_label = QLabel('Date of Birth', self)


        self.name_edit = QLineEdit('', self)
        self.surname_edit = QLineEdit('', self)
        self.title_edit = QLineEdit('', self)
        self.address_edit =QLineEdit('', self)
        self.city_edit = QLineEdit('', self)
        self.phone_edit = QLineEdit('', self)
        self.med_aid_edit =QLineEdit('', self)
        self.med_aidno_edit = QLineEdit('', self)
        self.med_aidnopack_edit = QLineEdit('', self)
        self.birth_edit = QLineEdit('', self)

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(name_label, 1, 0)
        grid.addWidget(self.name_edit, 1, 1)
        grid.addWidget(surname_label, 1, 2)
        grid.addWidget(self.surname_edit, 1, 3)
        grid.addWidget(title_label, 1, 4)
        grid.addWidget(self.title_edit, 1, 5)

        grid.addWidget(address_label, 2, 0)
        grid.addWidget(self.address_edit, 2, 1)
        grid.addWidget(city_label, 2, 2)
        grid.addWidget(self.city_edit, 2, 3)
        grid.addWidget(phone_label ,2, 4)
        grid.addWidget(self.phone_edit, 2, 5)

        grid.addWidget(med_aid_label, 3, 0)
        grid.addWidget(self.med_aid_edit, 3, 1 )
        grid.addWidget(med_aidno_label, 3, 2)
        grid.addWidget(self.med_aidno_edit, 3, 3)
        grid.addWidget(med_aidnopack_label, 3, 4)
        grid.addWidget(self.med_aidnopack_edit, 3, 5)

        grid.addWidget(birth_label, 4, 2)
        grid.addWidget(self.birth_edit, 4, 3)

        table_view = QTableView()
        grid.addWidget(table_view, 5, 0, 5, 0)


        save_btn = QPushButton('Save', self)
        next_btn = QPushButton('Next', self)
        back_btn = QPushButton('Back', self)
        cancel_btn = QPushButton('Cancel', self)
        settings_btn = QPushButton('Settings', self)
        help_btn = QPushButton('Help', self)

        next_btn.clicked.connect(self.entry)
        grid.addWidget(save_btn, 10, 0)
        grid.addWidget(next_btn, 10, 1)
        grid.addWidget(back_btn, 10, 2)
        grid.addWidget(cancel_btn, 10, 3)
        grid.addWidget(settings_btn, 10, 4)
        grid.addWidget(help_btn, 10, 5)


        self.setLayout(grid)

    def entry(self):
        self.switch_window.emit()


'''class Dispense(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super(Dispense, self).__init__(parent)
        self.setWindowTitle("Dispense")
        # self.setGeometry(300, 250, 500, 350)
        self.setFixedSize(800, 500)

        Ui_MainWindow()
        self.main_window = MainWindow()
        self.main_window.show()
        self.main_window.pushButton.clicked(self.main_window.goback)'''


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_windoww = pyqtSignal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goback)

    def goback(self):
        self.switch_windoww.emit()


class Controller:

    def __init__(self):
        pass

    def show_entry(self):
        self.entry = FirstPage()
        self.entry.switch_window.connect(self.show_dispense)
        self.entry.show()

    def show_dispense(self):
        self.dispense = MainWindow()
        if self.entry.name_edit.text() == "" :
            QMessageBox.warning(None, '', "Enter at least Name ")
            return self.entry
        if self.entry.surname_edit.text() == "":
            QMessageBox.warning(None, '', "Enter at least Surname ")
            return self.entry
        self.dispense.switch_windoww.connect(self.show_reentry)
        james = self.entry.name_edit.text()
        zatha = self.entry.surname_edit.text()
        titl = self.entry.title_edit.text()
        fone = self.entry.phone_edit.text()
        self.dispense.name_linedit.setText(james)
        self.dispense.surname_linedit.setText(zatha)
        self.dispense.lineEdit_4.setText(fone)
        self.dispense.lineEdit_8.setText(titl)
        self.entry.hide()
        self.dispense.show()

    def show_reentry(self):
        self.reentry = FirstPage()
        self.dispense.hide()
        self.entry.show()


def main():

    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_entry()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
