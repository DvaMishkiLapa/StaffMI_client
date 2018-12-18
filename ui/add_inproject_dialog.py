# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\add_inproject_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_inproject_dialog(object):
    def setupUi(self, add_inproject_dialog):
        add_inproject_dialog.setObjectName("add_inproject_dialog")
        add_inproject_dialog.setWindowModality(QtCore.Qt.NonModal)
        add_inproject_dialog.resize(350, 275)
        add_inproject_dialog.setMinimumSize(QtCore.QSize(350, 275))
        add_inproject_dialog.setMaximumSize(QtCore.QSize(350, 275))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icons/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_inproject_dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(add_inproject_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_dialog_inpoject = QtWidgets.QLabel(add_inproject_dialog)
        self.label_dialog_inpoject.setObjectName("label_dialog_inpoject")
        self.gridLayout.addWidget(self.label_dialog_inpoject, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(add_inproject_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 3, 2, 1, 1)
        self.add_button = QtWidgets.QPushButton(add_inproject_dialog)
        self.add_button.setEnabled(False)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 3, 1, 1, 1)
        self.line = QtWidgets.QFrame(add_inproject_dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.table_projects = QtWidgets.QTableWidget(add_inproject_dialog)
        self.table_projects.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_projects.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_projects.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_projects.setObjectName("table_projects")
        self.table_projects.setColumnCount(2)
        self.table_projects.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_projects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_projects.setHorizontalHeaderItem(1, item)
        self.table_projects.horizontalHeader().setDefaultSectionSize(120)
        self.gridLayout.addWidget(self.table_projects, 2, 0, 1, 3)

        self.retranslateUi(add_inproject_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_inproject_dialog)
        add_inproject_dialog.setTabOrder(self.table_projects, self.add_button)
        add_inproject_dialog.setTabOrder(self.add_button, self.cancel_button)

    def retranslateUi(self, add_inproject_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_inproject_dialog.setWindowTitle(_translate("add_inproject_dialog", "Добавление прользователя в проект"))
        self.label_dialog_inpoject.setText(_translate("add_inproject_dialog", "Выберете проект"))
        self.cancel_button.setText(_translate("add_inproject_dialog", "Отмена"))
        self.add_button.setText(_translate("add_inproject_dialog", "Добавить"))
        item = self.table_projects.horizontalHeaderItem(0)
        item.setText(_translate("add_inproject_dialog", "Название продукта"))
        item = self.table_projects.horizontalHeaderItem(1)
        item.setText(_translate("add_inproject_dialog", "Срок сдачи"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_inproject_dialog = QtWidgets.QDialog()
    ui = Ui_add_inproject_dialog()
    ui.setupUi(add_inproject_dialog)
    add_inproject_dialog.show()
    sys.exit(app.exec_())

