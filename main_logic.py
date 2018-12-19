import json
import sys
import hashlib

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from ui import main_window
from ui import login_stack
from ui import add_inproject_dialog
from ui import add_new_user_dialog
from ui import add_new_project_dialog
import db_api


# class responsible for the main window of working with the database
class miWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, api):
        super().__init__()
        self.setupUi(self)

        self.api = api

        self.worker_rows_to_delete = []
        self.worker_rows_were_changed = []
        self.unpacked_worker_rows_were_changed = [] # Сохранения данных других страниц
        self.new_worker_rows = []
        self.old_data_workers_rows = []

        self.project_rows_to_delete = []
        self.project_rows_were_changed = []
        self.unpacked_project_rows_were_changed = [] # Сохранения данных других страниц
        self.new_project_rows = []
        self.old_data_projects_rows = []

        self.user_projects = {}

        self.workers_table_page = 0

        self.update_workers()
        self.update_projects()

        # buttons events
        self.add_worker.clicked.connect(self.add_worker_click)
        self.del_worker.clicked.connect(self.del_worker_click)
        self.save_workers.clicked.connect(self.save_workers_click)
        self.workers_table.doubleClicked.connect(self.changed_cell_workers_table)
        self.workers_table.itemClicked.connect(self.show_user_projects)

        self.new_inproject.clicked.connect(self.new_inproject_click)
        self.new_inproject.clicked.connect(self.current_projects_table.scrollToBottom)
        self.del_inproject.clicked.connect(self.del_inproject_click)
        self.save_inprojects.clicked.connect(self.save_inprojects_click)

        self.add_project.clicked.connect(self.add_project_click)
        self.del_project.clicked.connect(self.del_project_click)
        self.save_projects.clicked.connect(self.save_projects_click)
        self.projects_table.doubleClicked.connect(self.changed_cell_projects_table)

        self.undo_changes_workers.clicked.connect(self.undo_changes_workers_table)
        self.undo_changes_projects.clicked.connect(self.undo_changes_projects_table)
        self.logout.clicked.connect(self.logout_click)
        self.logout_2.clicked.connect(self.logout_click)
        self.settings.clicked.connect(self.settings_click)
        self.settings_2.clicked.connect(self.settings_click)
        self.update_data.clicked.connect(self.update_workers_table_click)
        self.update_data_2.clicked.connect(self.update_projects_table_click)

        self.full_left.clicked.connect(self.full_left_click)
        self.page_left.clicked.connect(self.page_left_click)
        self.page_right.clicked.connect(self.page_right_click)
        self.full_right.clicked.connect(self.full_right_click)
        self.size_page.editingFinished.connect(self.full_left_click)

        self.workers_table.setColumnHidden(5, True)
        self.projects_table.setColumnHidden(2, True)


    def update_workers(self):
        self.user_projects.clear()
        self.label_log_main.setText('')
        answer = self.api.get_all_users({"offset": self.workers_table_page, "length": int(self.size_page.text())})
        if answer:
            self.workers_table.clearContents()
            self.workers_table.setRowCount(0)
            for worker in answer:
                self.user_projects.update({worker["email"]: worker["projects"]})
                row_pos = self.workers_table.rowCount()
                self.workers_table.insertRow(row_pos)
                self.workers_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(worker['email']))
                for x in range(1, 4):
                    self.workers_table.setItem(row_pos, x, QtWidgets.QTableWidgetItem(worker['name'][x-1]))
                self.workers_table.setItem(row_pos, 4, QtWidgets.QTableWidgetItem(worker['position']))
                self.workers_table.setItem(row_pos, 5, QtWidgets.QTableWidgetItem(worker['_id']))
        else:
            self.label_log_main.setText('Сервер недоступен!')
            return


    def update_projects(self):
        self.label_log_main.setText('')
        answer = self.api.get_all_projects({"offset": self.workers_table_page, "length": 1000})
        if answer:
            self.projects_table.clearContents()
            self.projects_table.setRowCount(0)
            for project in answer:
                row_pos = self.projects_table.rowCount()
                self.projects_table.insertRow(row_pos)
                self.projects_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(project['name']))
                self.projects_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(project['deadline']))
                self.projects_table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(project['_id']))
        else:
            self.label_log_main.setText('Сервер недоступен!')
            return


    def unpacked_worker_changed(self):
        for obj in self.worker_rows_were_changed:
            self.unpacked_worker_rows_were_changed.append({
                '_id': obj.sibling(obj.row(), 5).data(),
                'email': obj.sibling(obj.row(), 0).data(),
                'name': [obj.sibling(obj.row(), 1).data(), obj.sibling(obj.row(), 2).data(), obj.sibling(obj.row(), 3).data()],
                'position': obj.sibling(obj.row(), 4).data()
            })


    def add_worker_click(self):
        chose_dialog = newUserDialogWindow(self.api, self.workers_table, self.new_worker_rows)
        chose_dialog.exec_()


    def del_worker_click(self):
        selected_rows = self.workers_table.selectionModel().selectedRows()
        for row in selected_rows:
            table = row.model()
            index = row.row()
            row_id = row.sibling(row.row(), 5).data()
            try:
                self.worker_rows_to_delete.remove(row_id)
                for x in range(0, 5):
                    table.setData(table.index(index, x), QColor(255, 255, 255), Qt.BackgroundRole)
            except ValueError:
                self.worker_rows_to_delete.append(row_id)
                for x in range(0, 5):
                    table.setData(table.index(index, x), QColor(255, 127, 127), Qt.BackgroundRole)


    def save_workers_click(self):
        self.label_log_main.setText('')
        if self.api.get_all_users({"offset": 0, "length": 1}):
            if self.worker_rows_to_delete:
                self.api.del_users(self.worker_rows_to_delete)
                self.worker_rows_to_delete.clear()
            if self.new_worker_rows:
                self.api.add_users(self.new_worker_rows)
                self.new_worker_rows.clear()
            self.unpacked_worker_changed()
            if self.unpacked_worker_rows_were_changed:
                self.api.edit_users(self.unpacked_worker_rows_were_changed)
                self.unpacked_worker_rows_were_changed.clear()
                self.worker_rows_were_changed.clear()
            self.update_workers()
        else:
            self.label_log_main.setText('Сервер недоступен!')
            return


    def changed_cell_workers_table(self):
        row = self.workers_table.selectionModel().selectedRows()[0]
        if not self.worker_rows_to_delete.count(row.sibling(row.row(), 5).data()):
            table = row.model()
            index = row.row()
            self.old_data_workers_rows.append({
                '_id': row.sibling(index, 5).data(),
                'email': row.sibling(index, 0).data(), 'pwd': '123456', # We are waiting for password corrections
                'name': [row.sibling(index, 1).data(), row.sibling(index, 2).data(), row.sibling(index, 3).data()],
                'position': row.sibling(index, 4).data()
            })
            for x in range(0, 5):
                table.setData(table.index(index, x), QColor(255, 253, 153), Qt.BackgroundRole)
            self.worker_rows_were_changed.append(row)


    def new_inproject_click(self):
        rows = self.workers_table.selectionModel().selectedRows()
        if rows:
            answer = self.api.get_all_projects({"offset": 0, "length": 100})
            if answer:
                chose_dialog = inprojectDialogWindow(answer)
                chose_dialog.exec_()
                answer_user = chose_dialog.answer
                if answer_user:
                    data = []
                    for item in rows:
                        index = item.row()
                        data.append({
                            "email": item.sibling(index, 0).data(),
                            "project": answer_user[0].text()
                        })
                    self.api.assign_to_projects(data)
                    row_pos = self.current_projects_table.rowCount()
                    self.current_projects_table.insertRow(row_pos)
                    self.current_projects_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(answer_user[0]))
                    self.current_projects_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(answer_user[1]))
                    self.update_workers()
            else:
                self.label_log_main.setText('Сервер недоступен!')
                return


    def del_inproject_click(self):
        selected_row = self.current_projects_table.selectionModel().selectedRows()
        while len(selected_row):
            self.current_projects_table.removeRow(selected_row[-1].row())
            selected_row.pop()


    def save_inprojects_click(self):
        print('save_inprojects_click')


    def add_project_click(self):
        chose_dialog = newProjectDialogWindow(self.api, self.projects_table, self.new_project_rows)
        chose_dialog.exec_()


    def del_project_click(self):
        selected_rows = self.projects_table.selectionModel().selectedRows()
        for row in selected_rows:
            table = row.model()
            index = row.row()
            row_id = row.sibling(row.row(), 2).data()
            try:
                self.project_rows_to_delete.remove(row_id)
                for x in range(0, 5):
                    table.setData(table.index(index, x), QColor(255, 255, 255), Qt.BackgroundRole)
            except ValueError:
                self.project_rows_to_delete.append(row_id)
                for x in range(0, 5):
                    table.setData(table.index(index, x), QColor(255, 127, 127), Qt.BackgroundRole)


    def save_projects_click(self):
        self.label_log_main.setText('')
        if self.api.get_all_users({"offset": 0, "length": 1}):
            if self.project_rows_to_delete:
                self.api.del_projects(self.project_rows_to_delete)
                self.project_rows_to_delete.clear()
            if self.new_project_rows:
                self.api.add_projects(self.new_project_rows)
                self.new_project_rows.clear()
            for obj in self.project_rows_were_changed:
                self.unpacked_project_rows_were_changed.append({
                    '_id': obj.sibling(obj.row(), 2).data(),
                    'name': obj.sibling(obj.row(), 0).data(),
                    'deadline': obj.sibling(obj.row(), 1).data()
                })
            if self.unpacked_project_rows_were_changed:
                self.api.edit_projects(self.unpacked_project_rows_were_changed)
                self.unpacked_project_rows_were_changed.clear()
                self.project_rows_were_changed.clear()
            self.update_projects()
        else:
            self.label_log_main.setText('Сервер недоступен!')
            return


        self.label_log_main.setText('')
        if self.api.get_all_users({"offset": 0, "length": 1}):
            if self.project_rows_to_delete:
                self.api.del_projects([self.projects_dict_links.get(obj) for obj in self.project_rows_to_delete])
                self.project_rows_to_delete.clear()
            if self.new_project_rows:
                self.api.add_projects(self.new_project_rows)
                self.new_project_rows.clear()
            if self.project_rows_were_changed:
                list_changed_rows = []
                for obj in self.project_rows_were_changed:
                    list_changed_rows.append({
                        '_id': self.projects_dict_links.get(obj),
                        'name': obj.sibling(obj.row(), 0).data(),
                        'deadline': obj.sibling(obj.row(), 1).data()
                        })
                self.api.edit_projects(list_changed_rows)
                self.project_rows_were_changed.clear()
            self.update_projects()
        else:
            self.label_log_main.setText('Сервер недоступен!')
            return


    def changed_cell_projects_table(self):
        row = self.projects_table.selectionModel().selectedRows()[0]
        if not self.project_rows_to_delete.count(row.sibling(row.row(), 2).data()):
            table = row.model()
            index = row.row()
            self.old_data_projects_rows.append({
                '_id': row.sibling(index, 2).data(),
                'name': row.sibling(index, 0).data(), # We are waiting for password corrections
                'deadline': row.sibling(index, 1).data()
            })
            for x in range(0, 5):
                table.setData(table.index(index, x), QColor(255, 253, 153), Qt.BackgroundRole)
            self.project_rows_were_changed.append(row)


    def undo_changes_workers_table(self):
        self.worker_rows_to_delete.clear()
        self.unpacked_worker_rows_were_changed.clear()
        self.workers_table.selectAll()
        for item in self.worker_rows_were_changed:
            row_id = item.sibling(item.row(), 5).data()
            index = item.row()
            for old_item in self.old_data_workers_rows:
                if old_item['_id'] == row_id:
                    self.workers_table.setItem(index, 0, QtWidgets.QTableWidgetItem(old_item['email']))
                    for x in range(1, 4):
                        self.workers_table.setItem(index, x, QtWidgets.QTableWidgetItem(old_item['name'][x-1]))
                    self.workers_table.setItem(index, 4, QtWidgets.QTableWidgetItem(old_item['position']))
                    break
        self.worker_rows_were_changed.clear()
        self.old_data_workers_rows.clear()
        rows = self.workers_table.selectedItems()
        for x in rows:
            x.setBackground(QColor(255, 255, 255))
        for item in [item['email'] for item in self.new_worker_rows]:
            self.workers_table.removeRow(self.workers_table.findItems(item, Qt.MatchContains)[0].row())
        self.new_worker_rows.clear()


    def undo_changes_projects_table(self):
        self.project_rows_to_delete.clear()
        self.unpacked_project_rows_were_changed.clear()
        self.projects_table.selectAll()
        for item in self.project_rows_were_changed:
            row_id = item.sibling(item.row(), 2).data()
            index = item.row()
            for old_item in self.old_data_projects_rows:
                if old_item['_id'] == row_id:
                    self.projects_table.setItem(index, 0, QtWidgets.QTableWidgetItem(old_item['name']))
                    self.projects_table.setItem(index, 1, QtWidgets.QTableWidgetItem(old_item['deadline']))
                    break
        self.project_rows_were_changed.clear()
        self.old_data_projects_rows.clear()
        rows = self.projects_table.selectedItems()
        for x in rows:
            x.setBackground(QColor(255, 255, 255))
        for item in [item['name'] for item in self.new_project_rows]:
            self.projects_table.removeRow(self.projects_table.findItems(item, Qt.MatchContains)[0].row())
        self.new_project_rows.clear()

    def logout_click(self):
        self.workers_table.clear()
        self.projects_table.clear()
        self.current_projects_table.clear()
        self.destroy()
        self.last_window.show()

    def show_user_projects(self, item):
        self.current_projects_table.clearContents()
        self.current_projects_table.setRowCount(0)
        row = self.workers_table.selectionModel().selectedRows()[0]
        email = row.sibling(row.row(), 0).data()
        for project in self.user_projects[email]:
            row_pos = self.current_projects_table.rowCount()
            self.current_projects_table.insertRow(row_pos)
            self.current_projects_table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(project["name"]))
            self.current_projects_table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(project["deadline"]))


    def settings_click(self):
        print("settings_click")


    def update_workers_table_click(self):
        self.update_workers()


    def update_projects_table_click(self):
        self.update_projects()


    def page_left_click(self):
        self.workers_table_page -= int(self.size_page.text())
        self.full_right.setEnabled(True)
        self.page_right.setEnabled(True)
        if not self.workers_table_page:
            self.full_left.setEnabled(False)
            self.page_left.setEnabled(False)
        self.unpacked_worker_changed()
        self.worker_rows_were_changed.clear()
        self.update_workers()


    def page_right_click(self):
        self.workers_table_page += int(self.size_page.text())
        if self.api.get_users_count() - self.workers_table_page < int(self.size_page.text()):
            self.full_right.setEnabled(False)
            self.page_right.setEnabled(False)
        self.full_left.setEnabled(True)
        self.page_left.setEnabled(True)
        self.unpacked_worker_changed()
        self.worker_rows_were_changed.clear()
        self.update_workers()


    def full_left_click(self):
        self.workers_table_page = 0
        self.full_left.setEnabled(False)
        self.page_left.setEnabled(False)
        self.full_right.setEnabled(True)
        self.page_right.setEnabled(True)
        self.unpacked_worker_changed()
        self.worker_rows_were_changed.clear()
        self.update_workers()


    def full_right_click(self):
        size = self.api.get_users_count()
        self.workers_table_page = size - size % int(self.size_page.text())
        self.full_right.setEnabled(False)
        self.page_right.setEnabled(False)
        self.full_left.setEnabled(True)
        self.page_left.setEnabled(True)
        self.unpacked_worker_changed()
        self.worker_rows_were_changed.clear()
        self.update_workers()


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
        self.newpwd_button.clicked.connect(self.newpwd_button_click)

        # page_replace_pwd(1) buttons events
        self.save_newpwd_button.clicked.connect(self.save_newpwd_button_click)
        self.back_login_button.clicked.connect(self.back_login_button_click)

    # page_login(0) login button
    def login_button_click(self):
        self.label_log_login.setText('')
        self.api.user = self.input_login.text()
        self.api.pwd = self.input_pwd.text()
        answer = self.api.authorization(self.api.user, self.api.pwd)
        flag = self.check_save_loginpwd.isChecked()
        if answer:
            if not answer['content']['authorization']['ok']:
                self.error_loginpwd.setText('Неверный логин или пароль!')
            elif flag:
                with open('memory.json', 'w') as f:
                    f.write(json.dumps({'user_info':{'login': self.api.user, 'pwd': self.api.pwd}, 'flag': flag}))
                self.destroy()
                self.miWindow = miWindow(self.api)
                self.miWindow.last_window = self
                self.miWindow.show()
            else:
                with open('memory.json', 'w') as f:
                    f.write(json.dumps({'user_info': {'login': '', 'pwd': ''}, 'flag': False}))
                self.input_login.setText('')
                self.input_pwd.setText('')
                self.destroy()
                self.miWindow = miWindow(self.api)
                self.miWindow.last_window = self
                self.miWindow.show()
        else:
            self.label_log_login.setText('Сервер недоступен!')
            return


    # page_login(0) go to the user login change window
    def newpwd_button_click(self):
        self.login_stack.setCurrentIndex(1) # page_replace_login


    # page_replace_pwd(2) back button
    def back_login_button_click(self):
        self.login_stack.setCurrentIndex(0) # page_login

    # page_replace_pwd(2) button user pwd changes
    def save_newpwd_button_click(self):
        self.label_log_reppwd.setText('')
        login = self.input_login_reppwd.text()
        old_pwd = self.input_oldpwd.text()
        new_pwd = self.input_newpwd.text()
        if old_pwd != new_pwd:
            answer = self.api.change_password({"email": login, "old_pwd": old_pwd, "new_pwd": new_pwd})
            if answer == "Password has been changed.":
                self.error_reppwd.setStyleSheet("color: rgb(75, 225, 0);; font-weight: bold;")
                self.error_reppwd.setText('Пароль успешно изменен')
            else:
                self.error_reppwd.setStyleSheet("color: rgb(255, 0, 0);; font-weight: bold;")
                self.error_reppwd.setText('Неверный логин или пароль!')
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
        self.answer = False
        self.close()


    def on_table_projects_itemClicked(self, item):
        self.add_button.setEnabled(True)



class newProjectDialogWindow(QtWidgets.QDialog, add_new_project_dialog.Ui_add_new_project_dialog):
    def __init__(self, api, table, list_new_projects):
        super().__init__()
        self.setupUi(self)
        self.api = api
        self.table = table
        self.list = list_new_projects
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.add_button.clicked.connect(self.add_button_click)
        self.cancel_button.clicked.connect(self.cancel_button_click)


    def add_button_click(self):
        self.label_error.setText('')
        if self.api.get_all_users({"offset": 0, "length": 1}):
            name = self.line_project_name.text()
            deadline = self.calendarWidget.selectedDate()
            if not name or deadline.isNull():
                self.label_error.setText('Заполнены не все данные!')
            else:
                date_deadline = str(deadline.day()) + '.' + str(deadline.month()) + '.' + str(deadline.year())
                data = [{'name': name, 'deadline': date_deadline}]
                answer = self.api.add_projects(data)
                if answer['content']['add_projects'][0]['ok']:
                    row_pos = self.table.rowCount()
                    last_row = self.api.get_all_projects({"offset": -1, "length": row_pos+42})[0]
                    self.api.del_projects([last_row['_id']])
                    self.table.insertRow(row_pos)
                    self.table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(name))
                    self.table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(date_deadline))
                    self.list.extend(data)
                    self.table.selectRow(row_pos)
                    row = self.table.selectedItems()
                    for x in row:
                        x.setBackground(QColor(122, 255, 206))
                    self.table.scrollToBottom()
                    self.close()
                else:
                    self.label_error.setText('Проект с таким наименованием уже существует!')
        else:
            self.label_error.setText('Сервер недоступен!')
            return 


    def cancel_button_click(self):
        self.close()



class newUserDialogWindow(QtWidgets.QDialog, add_new_user_dialog.Ui_add_new_user_dialog):
    def __init__(self, api, table, list_new_workers):
        super().__init__()
        self.setupUi(self)
        self.api = api
        self.table = table
        self.list = list_new_workers
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.add_button.clicked.connect(self.add_button_click)
        self.cancel_button.clicked.connect(self.cancel_button_click)


    def add_button_click(self):
        self.label_error.setText('')
        if self.api.get_all_users({"offset": 0, "length": 1}):
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
                    row_pos = self.table.rowCount()
                    last_row = self.api.get_all_users({"offset": -1, "length": row_pos+42})[0]
                    self.api.del_users([last_row['_id']])
                    self.table.insertRow(row_pos)
                    self.table.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(email))
                    self.table.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(surname))
                    self.table.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(name))
                    self.table.setItem(row_pos, 3, QtWidgets.QTableWidgetItem(patron))
                    self.table.setItem(row_pos, 4, QtWidgets.QTableWidgetItem(pos))
                    self.list.extend(data)
                    self.table.selectRow(row_pos)
                    row = self.table.selectedItems()
                    for x in row:
                        x.setBackground(QColor(122, 255, 206))
                    self.table.scrollToBottom()
                    self.close()
                else:
                    self.label_error.setText('Пользователь с таким Email уже существует!')
        else:
            self.label_error.setText('Сервер недоступен!')
            return 


    def cancel_button_click(self):
        self.close()




def main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = loginStackWindow()
    login_window.show()
    app.exec_()

if __name__ == '__main__':
    main()