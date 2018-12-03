import json
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

import main_window
import login_stack
import add_inproject_dialog
import add_new_user_dialog
import db_api


# class responsible for the main window of working with the database
class pemiWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, api):
        super().__init__()
        self.setupUi(self)

        self.api = api
        self.rows_to_delete = []
        self.rows_were_changed = []
        # self.list_row_wc =[] # Сохранения данных других страниц

        self.update_workers()
        self.update_projects()

        # buttons events
        self.add_worker.clicked.connect(self.add_worker_click)
        self.del_worker.clicked.connect(self.del_worker_click)
        self.save_workers.clicked.connect(self.save_workers_click)
        self.workers_table.doubleClicked.connect(self.changed_cell)

        self.new_inproject.clicked.connect(self.new_inproject_click)
        self.new_inproject.clicked.connect(self.current_projects_table.scrollToBottom)
        self.del_inproject.clicked.connect(self.del_inproject_click)
        self.save_inprojects.clicked.connect(self.save_inprojects_click)

        self.add_project.clicked.connect(self.add_project_click)
        self.add_project.clicked.connect(self.projects_table.scrollToBottom)
        self.del_project.clicked.connect(self.del_project_click)
        self.save_projects.clicked.connect(self.save_projects_click)

        self.logout.clicked.connect(self.logout_click)
        self.logout_2.clicked.connect(self.logout_click)
        self.settings.clicked.connect(self.settings_click)
        self.settings_2.clicked.connect(self.settings_click)
        self.update_data.clicked.connect(self.update_data_click)
        self.update_data_2.clicked.connect(self.update_data_click)


    def update_workers(self):
        self.label_log_main.setText('')
        if not self.api.ping_server():
            self.label_log_main.setText('Сервер не доступен!')
            return 
        self.workers_table.clearContents()
        self.workers_table.setRowCount(0)
        for worker in self.api.get_all_users():
            row_pos = self.workers_table.rowCount()
            self.workers_table.insertRow(row_pos)
            self.workers_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(worker['email']))
            for x in range(1, 4):
                self.workers_table.setItem(row_pos, x, QtWidgets.QTableWidgetItem(worker['name'][x-1]))
            self.workers_table.setItem(row_pos, 4, QtWidgets.QTableWidgetItem(worker['position']))


    def update_projects(self):
        self.label_log_main.setText('')
        if not self.api.ping_server():
            self.label_log_main.setText('Сервер не доступен!')
            return 
        self.projects_table.clearContents()
        self.projects_table.setRowCount(0)
        for project in self.api.get_all_projects():
            row_pos = self.projects_table.rowCount()
            self.projects_table.insertRow(row_pos)
            self.projects_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(project['name']))
            self.projects_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(project['deadline']))


    def add_worker_click(self):
        chose_dialog = newUsertDialogWindow(self.api)
        chose_dialog.exec_()
        self.update_workers()
        self.workers_table.scrollToBottom()


    def del_worker_click(self):
        selected_rows = sorted(self.workers_table.selectionModel().selectedRows())
        for row in selected_rows:
            self.rows_to_delete.append({'email': row.sibling(row.row(), 0).data()})
        selected_rows = self.workers_table.selectedItems()
        for obj in selected_rows:
            obj.setBackground(QColor(255, 127, 127))


    def save_workers_click(self):
        self.label_log_main.setText('')
        if not self.api.ping_server():
            self.label_log_main.setText('Сервер не доступен!')
            return 
        if self.rows_to_delete:
            self.api.del_users(self.rows_to_delete)
            self.rows_to_delete.clear()
        if self.rows_were_changed:
            list_changed_rows = []
            for obj in self.rows_were_changed:
                list_changed_rows.append({
                    'email': obj.sibling(obj.row(), 0).data(), 'pwd': '123456', # We are waiting for password corrections
                    'name': [obj.sibling(obj.row(), 1).data(), obj.sibling(obj.row(), 2).data(), obj.sibling(obj.row(), 3).data()],
                    'position': obj.sibling(obj.row(), 4).data()
                    })
            self.api.edit_users(list_changed_rows)
            self.rows_were_changed.clear()
        self.update_workers()


    def changed_cell(self):
        selected_row = self.workers_table.selectedItems()
        for obj in selected_row:
            obj.setBackground(QColor(255, 253, 153))
        self.rows_were_changed.extend(self.workers_table.selectionModel().selectedRows())


    def new_inproject_click(self):
        chose_dialog = inprojectDialogWindow(self.api.get_all_projects())
        chose_dialog.exec_()
        answer = chose_dialog.answer
        if answer != None:
            row_pos = self.current_projects_table.rowCount()
            self.current_projects_table.insertRow(row_pos)
            self.current_projects_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(answer[0]))
            self.current_projects_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(answer[1]))


    def del_inproject_click(self):
        selected_row = self.current_projects_table.selectionModel().selectedRows()
        while len(selected_row):
            self.current_projects_table.removeRow(selected_row[-1].row())
            selected_row.pop()


    def save_inprojects_click(self):
        print('save_inprojects_click')


    def add_project_click(self):
        self.projects_table.insertRow(self.projects_table.rowCount())


    def del_project_click(self):
        selected_row = self.projects_table.selectionModel().selectedRows()
        while len(selected_row):
            self.projects_table.removeRow(selected_row[-1].row())
            selected_row.pop()


    def save_projects_click(self):
        print('save_projects_click')


    def logout_click(self):
        self.workers_table.clear()
        self.projects_table.clear()
        self.current_projects_table.clear()
        self.destroy()
        self.last_window.show()


    def settings_click(self):
        print("settings_click")


    def update_data_click(self):
        self.update_workers()
        self.update_projects()

    # [X]
    def closeEvent(self, event):
        event.accept()
        quit()


# class responsible for the stack window
class loginStackWindow(QtWidgets.QDialog, login_stack.Ui_login_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.api = db_api.API()

        try:
            with open('memory.json') as f:
                self.data = json.load(f)
        except IOError:
            self.data = {'user_info':{'login': '', 'pwd': ''}, 'flag': False}
            with open('memory.json') as f:
                self.data = json.load(f)

        # page_login(0) buttons events and data logic
        self.check_save_loginpwd.setChecked(self.data['flag'])
        self.input_login.setText(self.data['user_info']['login'])
        self.input_pwd.setText(self.data['user_info']['pwd'])

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
        self.label_log_login.setText('')
        if not self.api.ping_server():
            self.label_log_login.setText('Сервер не доступен!')
            return 
        flag = self.check_save_loginpwd.isChecked()
        self.api.user = self.input_login.text()
        self.api.pwd = self.input_pwd.text()
        answer = self.api.authorization(self.api.user, self.api.pwd)
        if not answer:
            self.error_loginpwd.setText('Неверный логин или пароль!')
        elif flag:
            with open('memory.json', 'w') as f:
                f.write(json.dumps({'user_info':{'login': self.api.user, 'pwd': self.api.pwd}, 'flag': flag}))
            self.destroy()
            self.pemiWindow = pemiWindow(self.api)
            self.pemiWindow.last_window = self
            self.pemiWindow.show()
        else:
            with open('memory.json', 'w') as f:
                f.write(json.dumps({'user_info': {'login': '', 'pwd': ''}, 'flag': False}))
            self.input_login.setText('')
            self.input_pwd.setText('')
            self.destroy()
            self.pemiWindow = pemiWindow(self.api)
            self.pemiWindow.last_window = self
            self.pemiWindow.show()

    # page_login(0) go to the user password change window
    def newlogin_button_click(self):
        self.login_stack.setCurrentIndex(2) # page_replace_pwd

    # page_login(0) go to the user login change window
    def newpwd_button_click(self):
        self.login_stack.setCurrentIndex(1) # page_replace_login

   # page_replace_login(2) button user login changes
    def save_newlogin_button_click(self):
        self.label_log_replogin.setText('')
        if not self.api.ping_server():
            self.label_log_replogin.setText('Сервер не доступен!')
            return 
        old_login = self.input_oldlogin.text()
        pwd = self.input_pwd_replogin.text()
        new_login = self.input_newlogin.text()
        if old_login != new_login:
            data = [{'user_unfo': {'login': old_login, 'pwd': pwd}, 'new_login': new_login}]
            # self.api.edit_users(data)
            print(data)
        else:
            self.error_replog.setText('Новый логин совпадает с текущим!')
    # page_replace_login(2) and page_replace_pwd(2) back button
    def back_login_button_click(self):
        self.login_stack.setCurrentIndex(0) # page_login

    # page_replace_pwd(2) button user pwd changes
    def save_newpwd_button_click(self):
        self.label_log_reppwd.setText('')
        if not self.api.ping_server():
            self.label_log_reppwd.setText('Сервер не доступен!')
            return 
        login = self.input_login_reppwd.text()
        old_pwd = self.input_oldpwd.text()
        new_pwd = self.input_newpwd.text()
        answer = self.api.authorization(login, old_pwd)
        if not answer:
            self.error_reppwd.setStyleSheet("color: rgb(255, 0, 0);; font-weight: bold;")
            self.error_reppwd.setText('Неверный логин или пароль!')
        elif old_pwd != new_pwd:
            data = [{'email': login, 'pwd': new_pwd, 'name': ['1', '2', '3'], 'position': '4'}]
            self.api.edit_users(data)
            self.error_reppwd.setStyleSheet("color: rgb(75, 225, 0);; font-weight: bold;")
            self.error_reppwd.setText('Пароль успешно изменен')
        else:
            self.error_reppwd.setStyleSheet("color: rgb(255, 0, 0);; font-weight: bold;")
            self.error_reppwd.setText('Новый пароль совпадает с текущим!')

    # [X]
    def closeEvent(self, event):
        event.accept()
        quit()



class inprojectDialogWindow(QtWidgets.QDialog, add_inproject_dialog.Ui_add_inproject_dialog):
    def __init__(self, list_projects):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.answer = None
        self.add_button.clicked.connect(self.add_button_click)
        self.cancel_button.clicked.connect(self.cancel_button_click)

        for project in list_projects:
            row_pos = self.table_projects.rowCount()
            self.table_projects.insertRow(row_pos)
            self.table_projects.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(project['name']))
            self.table_projects.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(project['deadline']))


    def add_button_click(self):
        self.answer = self.table_projects.selectedItems()
        self.close()


    def cancel_button_click(self):
        self.close()


    def on_table_projects_itemClicked(self, item):
        self.add_button.setEnabled(True)



class newUsertDialogWindow(QtWidgets.QDialog, add_new_user_dialog.Ui_add_new_user_dialog):
    def __init__(self, api):
        super().__init__()
        self.setupUi(self)
        self.api = api
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.add_button.clicked.connect(self.add_button_click)
        self.cancel_button.clicked.connect(self.cancel_button_click)


    def add_button_click(self):
        email = self.lineEdit_email.text()
        surname = self.lineEdit_surname.text()
        name = self.lineEdit_name.text()
        patron = self.lineEdit_patron.text()
        pos = self.lineEdit_pos.text()
        pwd = self.lineEdit_pwd.text()
        confpwd = self.lineEdit_confpwd.text()
        if not (email and name and surname and patron and pos and pwd and confpwd):
            self.label_error.setText('Заполнены не все поля!')
        elif not (pwd == confpwd):
            self.label_error.setText('Пароли не совпадают!')
        else:
            data = [{'email': email, 'pwd': pwd, 'name': [surname, name, patron], 'position': pos}]
            answer = self.api.add_users(data)
            if not answer['ok']:
                self.label_error.setText('Неверный вид Email!')
            elif answer['content']['add_users'][0]['ok']:
                self.close()
            else:
                self.label_error.setText('Пользователь с таким Email уже существует!')


    def cancel_button_click(self):
        self.close()



def main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = loginStackWindow()
    login_window.show()
    app.exec_()

if __name__ == '__main__':
    main()