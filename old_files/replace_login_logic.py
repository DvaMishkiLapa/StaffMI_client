import json
import sys
from PyQt5 import QtWidgets
import replace_login

class replace_login_ui(QtWidgets.QDialog, replace_login.Ui_replace_login_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.last_window = self
        self.save_newlogin_button.clicked.connect(self.save_newlogin_button_click)
        self.back_button.clicked.connect(self.back_button_click)
        print('Смена')
        print(self)

    def save_newlogin_button_click(self):
        print('save_newlogin_button_click')

    def back_button_click(self):
        self.destroy()
        self.last_window.show()
        
    

    def closeEvent(self, event):
        event.accept()
        quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = replace_login_ui()
    window.exec_()
    app.exec_()

if __name__ == '__main__':
    main()
