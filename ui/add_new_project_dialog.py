# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\\ui\\add_new_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_new_project_dialog(object):
    def setupUi(self, add_new_project_dialog):
        add_new_project_dialog.setObjectName("add_new_project_dialog")
        add_new_project_dialog.resize(350, 300)
        add_new_project_dialog.setMinimumSize(QtCore.QSize(350, 300))
        add_new_project_dialog.setMaximumSize(QtCore.QSize(350, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icons/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_new_project_dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(add_new_project_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(add_new_project_dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)
        self.line = QtWidgets.QFrame(add_new_project_dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.label_dialog_newproject = QtWidgets.QLabel(add_new_project_dialog)
        self.label_dialog_newproject.setObjectName("label_dialog_newproject")
        self.gridLayout.addWidget(self.label_dialog_newproject, 0, 0, 1, 2)
        self.line_project_name = QtWidgets.QLineEdit(add_new_project_dialog)
        self.line_project_name.setObjectName("line_project_name")
        self.gridLayout.addWidget(self.line_project_name, 2, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(add_new_project_dialog)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 3, 0, 1, 2)
        self.label_name = QtWidgets.QLabel(add_new_project_dialog)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 2, 0, 1, 1)
        self.label_error = QtWidgets.QLabel(add_new_project_dialog)
        self.label_error.setStyleSheet("color: rgb(255, 0, 0);\n"
"font-weight: bold;")
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_error.setObjectName("label_error")
        self.gridLayout.addWidget(self.label_error, 5, 0, 1, 2)

        self.retranslateUi(add_new_project_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_new_project_dialog)

    def retranslateUi(self, add_new_project_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_new_project_dialog.setWindowTitle(_translate("add_new_project_dialog", "Создание нового проекта"))
        self.label_dialog_newproject.setText(_translate("add_new_project_dialog", "Введите название проекта и выберете его срок сдачи"))
        self.label_name.setText(_translate("add_new_project_dialog", "Наименование проекта:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_new_project_dialog = QtWidgets.QDialog()
    ui = Ui_add_new_project_dialog()
    ui.setupUi(add_new_project_dialog)
    add_new_project_dialog.show()
    sys.exit(app.exec_())

