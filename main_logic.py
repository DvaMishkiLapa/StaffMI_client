import json
import sys
from PyQt5 import QtWidgets
import main_window
import login_stack

# class responsible for the main window of working with the database
class pemi_window(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # buttons events
        self.add_worker.clicked.connect(self.add_worker_click)
        self.del_worker.clicked.connect(self.del_worker_click)
        self.save_workers.clicked.connect(self.save_workers_click)

        self.new_inproject.clicked.connect(self.new_inproject_click)
        self.del_inproject.clicked.connect(self.del_inproject_click)
        self.save_inprojects.clicked.connect(self.save_inprojects_click)

        self.add_project.clicked.connect(self.add_project_click)
        self.del_project.clicked.connect(self.del_project_click)
        self.save_projects.clicked.connect(self.save_projects_click)

        self.logout.clicked.connect(self.logout_click)
        self.logout_2.clicked.connect(self.logout_click)
        self.settings.clicked.connect(self.settings_click)
        self.settings_2.clicked.connect(self.settings_click)
        self.update_data.clicked.connect(self.update_data_click)
        self.update_data_2.clicked.connect(self.update_data_click)

    # [-_-]
    def add_worker_click(self):
        print('add_worker_click')
    def del_worker_click(self):
        print('del_worker_click')
    def save_workers_click(self):
        print('save_workers_click')

    def new_inproject_click(self):
        print('new_inproject_click')
    def del_inproject_click(self):
        print('del_inproject_click')
    def save_inprojects_click(self):
        print('save_inprojects_click')

    def add_project_click(self):
        print('add_project_click')
    def del_project_click(self):
        print('del_project_click')
    def save_projects_click(self):
        print('save_projects_click')

    def logout_click(self):
        self.last_window.show()
        self.destroy()
    def settings_click(self):
        print("settings_click")
    def update_data_click(self):
        print("update_data_click")

    # [X]
    def closeEvent(self, event):
        event.accept()
        quit()

# class responsible for the stack window
class login_stack_window(QtWidgets.QDialog, login_stack.Ui_login_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        try:
            with open('memory.json') as f:
                self.data = json.load(f)
        except IOError:
            self.data = {'user_info':{'login': '', 'pwd': ''}, 'flag': False}
            with open('memory.json') as f:
                self.data = json.load(f)

        # page_login(0) buttons events and data logic
        self.check_save_loginpwd.setChecked(bool(self.data['flag']))
        self.user, self.pwd = self.data['user_info'].values()
        self.input_login.setText(self.user)
        self.input_pwd.setText(self.pwd)
        self.login_button.clicked.connect(self.login_button_click)
        self.newlogin_button.clicked.connect(self.newlogin_button_click)
        self.newpwd_button.clicked.connect(self.newpwd_button_click)

        # page_replace_login(2) buttons events
        self.save_newlogin_button.clicked.connect(self.save_newlogin_button_click)
        self.back_login_button2.clicked.connect(self.back_login_button_click)

        # page_replace_pwd(1) buttons events
        self.save_newpwd_button.clicked.connect(self.save_newpwd_button_click)
        self.back_login_button.clicked.connect(self.back_login_button_click)

    # page_login(0) login button
    def login_button_click(self):
        flag = self.check_save_loginpwd.isChecked()
        input_login_text = self.input_login.text()
        if input_login_text == 'server_resp' or not input_login_text: # Для ответа от сервера
            self.error_loginpwd.setText('Неверный логин или пароль')
        elif flag:
            self.user = self.input_login.text()
            self.pwd = self.input_pwd.text()
            with open('memory.json', 'w') as f:
                f.write(json.dumps({'user_info':{'login': self.user, 'pwd': self.pwd}, 'flag': flag}))
            self.destroy()
            self.pemi_window = pemi_window()
            self.pemi_window.last_window = self
            self.pemi_window.show()
        else:
            with open('memory.json', 'w') as f:
                f.write(json.dumps({'user_info': {'login': '', 'pwd': ''}, 'flag': False}))
            self.input_login.setText('')
            self.input_pwd.setText('')
            self.destroy()
            self.pemi_window = pemi_window()
            self.pemi_window.last_window = self
            self.pemi_window.show()

    # page_login(0) go to the user password change window
    def newlogin_button_click(self):
        self.login_stack.setCurrentIndex(2) # page_replace_pwd

    # page_login(0) go to the user login change window
    def newpwd_button_click(self):
        self.login_stack.setCurrentIndex(1) # page_replace_login

   # page_replace_login(2) button user login changes
    def save_newlogin_button_click(self):
        old_login = self.input_oldlogin.text()
        pwd = self.input_pwd_replogin.text()
        new_login = self.input_newlogin.text()
        if old_login != new_login:
            response = {'user_unfo': {'login': old_login, 'pwd': pwd}, 'new_login': new_login}
            print(response)
        else:
            print('logins match')

    # page_replace_login(2) and page_replace_pwd(2) back button
    def back_login_button_click(self):
        self.login_stack.setCurrentIndex(0) # page_login

    # page_replace_pwd(2) button user pwd changes
    def save_newpwd_button_click(self):
        login = self.input_login_reppwd.text()
        old_pwd = self.input_oldpwd.text()
        new_pwd = self.input_newpwd.text()
        if old_pwd != new_pwd:
            response = {'user_unfo': {'login': login, 'old_pwd': old_pwd}, 'new_pwd': new_pwd}
            print(response)
        else:
            print('passwords match')

    # [X]
    def closeEvent(self, event):
        event.accept()
        quit()



def main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = login_stack_window()
    login_window.show()
    app.exec_()

if __name__ == '__main__':
    main()