import json
import sys
from PyQt5 import QtWidgets
import login_dialog
import replace_login_logic
# import replace_pass_logic

class login_ui(QtWidgets.QDialog, login_dialog.Ui_login_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.last_window = self

        # НЕ РАБОТАЕТ :(
        data = {}
        try:
            f = open('memory.json', 'r')
            data = json.loads(f.read())
            f.close()
        except IOError:
            f = open('memory.json', 'w')
            f.write(json.dumps({'user_info':{'login': '', 'pwd': ''}, 'flag': False}))
            f.close()

        self.check_save_loginpwd.setChecked(bool(data['flag']))
        self.user, self.pwd = dict.values(data['user_info'])

        if self.user or self.pwd:
            self.input_login.setText(self.user)
            self.input_pwd.setText(self.pwd)


        self.login_button.clicked.connect(self.login_button_click)
        self.newlogin_button.clicked.connect(self.newlogin_button_click)
        self.newpwd_button.clicked.connect(self.newpwd_button_click)

        # self.setWindowModality(Qt.WindowModal)

    def login_button_click(self):
        flag = self.check_save_loginpwd.isChecked()
        
        input_login_text = self.input_login.text()
        if input_login_text == 'server_resp' or not input_login_text: #Для ответа от сервара
            self.error_loginpwd.setText('Неверный логин или пароль')
        elif flag:
            f = open('memory.json', 'w')
            self.user = self.input_login.text()
            self.pwd = self.input_pwd.text()
            f.write(json.dumps({'user_info':{'login': self.user, 'pwd': self.pwd}, 'flag': flag}))
            f.close()
            # self.last_window.setVisible(True)
            self.destroy()
            self.last_window.show()
            print('сейвил')
        else:
            f = open('memory.json', 'w')
            f.write(json.dumps({'user_info': {'login': '', 'pwd': ''}, 'flag': False}))
            f.close()
            self.last_window.show()
            # self.last_window.setVisible(True)
            self.destroy()
            # print('Не сейвил')
        

    def newlogin_button_click(self):
        print('newlogin_button_click')
        # # self.hide()
        # newlogin_window = replace_login_logic.replace_login_ui()
        # newlogin_window.last_window = self
        # self.destroy()
        # newlogin_window.show()
        

    def newpwd_button_click(self):
        print('newpwd_button_click')


    def closeEvent(self, event):
        event.accept()
        quit()
        # reply = QtWidgets.QMessageBox.question(self, 'Message',
        #     "Are you sure to quit?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        # if reply == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        #     quit()
        # else:
        #     event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = login_ui()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
