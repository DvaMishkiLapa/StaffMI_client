# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\add_new_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_new_project_dialog(object):
    def setupUi(self, add_new_project_dialog):
        add_new_project_dialog.setObjectName("add_new_project_dialog")
        add_new_project_dialog.resize(370, 341)
        add_new_project_dialog.setMinimumSize(QtCore.QSize(370, 341))
        add_new_project_dialog.setMaximumSize(QtCore.QSize(370, 341))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconstitle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_new_project_dialog.setWindowIcon(icon)
        add_new_project_dialog.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.gridLayout = QtWidgets.QGridLayout(add_new_project_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(add_new_project_dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 4)
        self.calendarWidget = QtWidgets.QCalendarWidget(add_new_project_dialog)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 4, 0, 1, 4)
        self.cancel_button = QtWidgets.QPushButton(add_new_project_dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 5, 3, 1, 1)
        self.label_name = QtWidgets.QLabel(add_new_project_dialog)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 3, 0, 1, 1)
        self.add_button = QtWidgets.QPushButton(add_new_project_dialog)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 5, 2, 1, 1)
        self.line_project_name = QtWidgets.QLineEdit(add_new_project_dialog)
        self.line_project_name.setObjectName("line_project_name")
        self.gridLayout.addWidget(self.line_project_name, 3, 1, 1, 3)
        self.label_dialog_newproject = QtWidgets.QLabel(add_new_project_dialog)
        self.label_dialog_newproject.setObjectName("label_dialog_newproject")
        self.gridLayout.addWidget(self.label_dialog_newproject, 0, 0, 1, 4)
        self.label_error = QtWidgets.QLabel(add_new_project_dialog)
        self.label_error.setMinimumSize(QtCore.QSize(0, 20))
        self.label_error.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_error.setStyleSheet("font: 11pt \"Times New Roman\";\n"
"color: rgb(255, 0, 0);\n"
"font-weight: bold;")
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_error.setObjectName("label_error")
        self.gridLayout.addWidget(self.label_error, 8, 0, 1, 4)
        self.line = QtWidgets.QFrame(add_new_project_dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)

        self.retranslateUi(add_new_project_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_new_project_dialog)

    def retranslateUi(self, add_new_project_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_new_project_dialog.setWindowTitle(_translate("add_new_project_dialog", "Создание нового проекта"))
        self.cancel_button.setText(_translate("add_new_project_dialog", "Отмена"))
        self.label_name.setText(_translate("add_new_project_dialog", "Наименование проекта:"))
        self.add_button.setText(_translate("add_new_project_dialog", "Добавить"))
        self.label_dialog_newproject.setText(_translate("add_new_project_dialog", "Введите название проекта и выберете его срок сдачи"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_new_project_dialog = QtWidgets.QDialog()
    ui = Ui_add_new_project_dialog()
    ui.setupUi(add_new_project_dialog)
    add_new_project_dialog.show()
    sys.exit(app.exec_())
