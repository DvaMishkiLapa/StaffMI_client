# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\login_stack.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(250, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icons/title.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(login_dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.login_stack = QtWidgets.QStackedWidget(login_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_stack.sizePolicy().hasHeightForWidth())
        self.login_stack.setSizePolicy(sizePolicy)
        self.login_stack.setMinimumSize(QtCore.QSize(250, 300))
        self.login_stack.setMaximumSize(QtCore.QSize(250, 300))
        self.login_stack.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_stack.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_stack.setLineWidth(1)
        self.login_stack.setObjectName("login_stack")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_login)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.error_loginpwd = QtWidgets.QLabel(self.page_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_loginpwd.sizePolicy().hasHeightForWidth())
        self.error_loginpwd.setSizePolicy(sizePolicy)
        self.error_loginpwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.error_loginpwd.setStyleSheet("color: rgb(255, 0, 0);\n"
"font-weight: bold;")
        self.error_loginpwd.setText("")
        self.error_loginpwd.setAlignment(QtCore.Qt.AlignCenter)
        self.error_loginpwd.setObjectName("error_loginpwd")
        self.gridLayout_5.addWidget(self.error_loginpwd, 6, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.page_login)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_5.addWidget(self.line_3, 16, 0, 1, 2)
        self.name_menu_login = QtWidgets.QLabel(self.page_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_menu_login.sizePolicy().hasHeightForWidth())
        self.name_menu_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.name_menu_login.setFont(font)
        self.name_menu_login.setFocusPolicy(QtCore.Qt.NoFocus)
        self.name_menu_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_menu_login.setAutoFillBackground(False)
        self.name_menu_login.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.name_menu_login.setTextFormat(QtCore.Qt.AutoText)
        self.name_menu_login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_menu_login.setObjectName("name_menu_login")
        self.gridLayout_5.addWidget(self.name_menu_login, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.page_login)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 2)
        self.input_pwd = QtWidgets.QLineEdit(self.page_login)
        self.input_pwd.setStyleSheet("")
        self.input_pwd.setText("")
        self.input_pwd.setMaxLength(100)
        self.input_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.input_pwd.setObjectName("input_pwd")
        self.gridLayout_5.addWidget(self.input_pwd, 5, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 8, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.page_login)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 9, 0, 1, 2)
        self.label_log_login = QtWidgets.QLabel(self.page_login)
        self.label_log_login.setStyleSheet("color: rgb(255, 0, 0);\n"
"font-weight: bold;")
        self.label_log_login.setText("")
        self.label_log_login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_log_login.setObjectName("label_log_login")
        self.gridLayout_5.addWidget(self.label_log_login, 17, 0, 1, 2)
        self.input_login = QtWidgets.QLineEdit(self.page_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_login.sizePolicy().hasHeightForWidth())
        self.input_login.setSizePolicy(sizePolicy)
        self.input_login.setStyleSheet("")
        self.input_login.setText("")
        self.input_login.setMaxLength(100)
        self.input_login.setAlignment(QtCore.Qt.AlignCenter)
        self.input_login.setObjectName("input_login")
        self.gridLayout_5.addWidget(self.input_login, 3, 0, 1, 2)
        self.check_save_loginpwd = QtWidgets.QCheckBox(self.page_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_save_loginpwd.sizePolicy().hasHeightForWidth())
        self.check_save_loginpwd.setSizePolicy(sizePolicy)
        self.check_save_loginpwd.setCheckable(True)
        self.check_save_loginpwd.setTristate(False)
        self.check_save_loginpwd.setObjectName("check_save_loginpwd")
        self.gridLayout_5.addWidget(self.check_save_loginpwd, 8, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.newpwd_button = QtWidgets.QPushButton(self.page_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newpwd_button.sizePolicy().hasHeightForWidth())
        self.newpwd_button.setSizePolicy(sizePolicy)
        self.newpwd_button.setMinimumSize(QtCore.QSize(0, 0))
        self.newpwd_button.setObjectName("newpwd_button")
        self.gridLayout_2.addWidget(self.newpwd_button, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 15, 0, 1, 2)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_login)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_8, 4, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.page_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(0, 6, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 2, 1, 1)
        self.login_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setMinimumSize(QtCore.QSize(0, 18))
        self.login_button.setObjectName("login_button")
        self.gridLayout_3.addWidget(self.login_button, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 7, 0, 1, 2)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setHorizontalSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem7, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.page_login)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem8, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_7, 2, 0, 1, 2)
        self.login_stack.addWidget(self.page_login)
        self.page_replace_pwd = QtWidgets.QWidget()
        self.page_replace_pwd.setObjectName("page_replace_pwd")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_replace_pwd)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_log_reppwd = QtWidgets.QLabel(self.page_replace_pwd)
        self.label_log_reppwd.setStyleSheet("color: rgb(255, 0, 0);\n"
"font-weight: bold;")
        self.label_log_reppwd.setText("")
        self.label_log_reppwd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_log_reppwd.setObjectName("label_log_reppwd")
        self.gridLayout_6.addWidget(self.label_log_reppwd, 11, 0, 1, 2)
        self.input_oldpwd = QtWidgets.QLineEdit(self.page_replace_pwd)
        self.input_oldpwd.setText("")
        self.input_oldpwd.setMaxLength(100)
        self.input_oldpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_oldpwd.setAlignment(QtCore.Qt.AlignCenter)
        self.input_oldpwd.setObjectName("input_oldpwd")
        self.gridLayout_6.addWidget(self.input_oldpwd, 5, 0, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.page_replace_pwd)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_6.addWidget(self.line_5, 10, 0, 1, 2)
        self.input_login_reppwd = QtWidgets.QLineEdit(self.page_replace_pwd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_login_reppwd.sizePolicy().hasHeightForWidth())
        self.input_login_reppwd.setSizePolicy(sizePolicy)
        self.input_login_reppwd.setStyleSheet("")
        self.input_login_reppwd.setText("")
        self.input_login_reppwd.setMaxLength(100)
        self.input_login_reppwd.setAlignment(QtCore.Qt.AlignCenter)
        self.input_login_reppwd.setObjectName("input_login_reppwd")
        self.gridLayout_6.addWidget(self.input_login_reppwd, 3, 0, 1, 2)
        self.input_newpwd = QtWidgets.QLineEdit(self.page_replace_pwd)
        self.input_newpwd.setStyleSheet("")
        self.input_newpwd.setText("")
        self.input_newpwd.setMaxLength(100)
        self.input_newpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_newpwd.setAlignment(QtCore.Qt.AlignCenter)
        self.input_newpwd.setObjectName("input_newpwd")
        self.gridLayout_6.addWidget(self.input_newpwd, 7, 0, 1, 2)
        self.message_newpwd = QtWidgets.QLabel(self.page_replace_pwd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_newpwd.sizePolicy().hasHeightForWidth())
        self.message_newpwd.setSizePolicy(sizePolicy)
        self.message_newpwd.setMaximumSize(QtCore.QSize(16777215, 200))
        self.message_newpwd.setSizeIncrement(QtCore.QSize(20, 20))
        self.message_newpwd.setBaseSize(QtCore.QSize(10, 20))
        self.message_newpwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.message_newpwd.setTextFormat(QtCore.Qt.AutoText)
        self.message_newpwd.setScaledContents(False)
        self.message_newpwd.setAlignment(QtCore.Qt.AlignCenter)
        self.message_newpwd.setObjectName("message_newpwd")
        self.gridLayout_6.addWidget(self.message_newpwd, 6, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_replace_pwd)
        self.groupBox_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setToolTipDuration(-1)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_4.setContentsMargins(0, 6, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.save_newpwd_button = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.save_newpwd_button.sizePolicy().hasHeightForWidth())
        self.save_newpwd_button.setSizePolicy(sizePolicy)
        self.save_newpwd_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.save_newpwd_button.setAutoFillBackground(False)
        self.save_newpwd_button.setFlat(False)
        self.save_newpwd_button.setObjectName("save_newpwd_button")
        self.gridLayout_4.addWidget(self.save_newpwd_button, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 0, 0, 1, 1)
        self.back_login_button = QtWidgets.QPushButton(self.groupBox_2)
        self.back_login_button.setObjectName("back_login_button")
        self.gridLayout_4.addWidget(self.back_login_button, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 9, 0, 1, 2)
        self.name_menu_reppwd = QtWidgets.QLabel(self.page_replace_pwd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_menu_reppwd.sizePolicy().hasHeightForWidth())
        self.name_menu_reppwd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.name_menu_reppwd.setFont(font)
        self.name_menu_reppwd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.name_menu_reppwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_menu_reppwd.setAutoFillBackground(False)
        self.name_menu_reppwd.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.name_menu_reppwd.setTextFormat(QtCore.Qt.AutoText)
        self.name_menu_reppwd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_menu_reppwd.setObjectName("name_menu_reppwd")
        self.gridLayout_6.addWidget(self.name_menu_reppwd, 0, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.page_replace_pwd)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_6.addWidget(self.line_4, 1, 0, 1, 2)
        self.message_oldpwd = QtWidgets.QLabel(self.page_replace_pwd)
        self.message_oldpwd.setAlignment(QtCore.Qt.AlignCenter)
        self.message_oldpwd.setObjectName("message_oldpwd")
        self.gridLayout_6.addWidget(self.message_oldpwd, 2, 0, 1, 2)
        self.error_reppwd = QtWidgets.QLabel(self.page_replace_pwd)
        self.error_reppwd.setStyleSheet("color: rgb(255, 0, 0);\n"
"font-weight: bold;")
        self.error_reppwd.setText("")
        self.error_reppwd.setAlignment(QtCore.Qt.AlignCenter)
        self.error_reppwd.setObjectName("error_reppwd")
        self.gridLayout_6.addWidget(self.error_reppwd, 8, 0, 1, 2)
        self.login_stack.addWidget(self.page_replace_pwd)
        self.gridLayout.addWidget(self.login_stack, 0, 0, 1, 1)

        self.retranslateUi(login_dialog)
        self.login_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)
        login_dialog.setTabOrder(self.input_login, self.input_pwd)
        login_dialog.setTabOrder(self.input_pwd, self.login_button)
        login_dialog.setTabOrder(self.login_button, self.check_save_loginpwd)
        login_dialog.setTabOrder(self.check_save_loginpwd, self.newpwd_button)
        login_dialog.setTabOrder(self.newpwd_button, self.input_login_reppwd)
        login_dialog.setTabOrder(self.input_login_reppwd, self.input_oldpwd)
        login_dialog.setTabOrder(self.input_oldpwd, self.input_newpwd)
        login_dialog.setTabOrder(self.input_newpwd, self.save_newpwd_button)
        login_dialog.setTabOrder(self.save_newpwd_button, self.back_login_button)

    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "StaffMI"))
        self.name_menu_login.setText(_translate("login_dialog", "Вход"))
        self.input_login.setToolTip(_translate("login_dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.check_save_loginpwd.setText(_translate("login_dialog", "Запомнить"))
        self.newpwd_button.setText(_translate("login_dialog", "Сменить пароль"))
        self.label_2.setText(_translate("login_dialog", "Пароль"))
        self.login_button.setText(_translate("login_dialog", "Вход"))
        self.label.setText(_translate("login_dialog", "Логин"))
        self.input_login_reppwd.setToolTip(_translate("login_dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.message_newpwd.setText(_translate("login_dialog", "<html><head/><body><p align=\"center\">Длина нового пароля должна<br/>быть не менее 8 символов</p></body></html>"))
        self.save_newpwd_button.setText(_translate("login_dialog", "Сохранить"))
        self.back_login_button.setText(_translate("login_dialog", "Назад"))
        self.name_menu_reppwd.setText(_translate("login_dialog", "Смена пароля"))
        self.message_oldpwd.setText(_translate("login_dialog", "Введите ваш логин и текущий пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_dialog = QtWidgets.QDialog()
    ui = Ui_login_dialog()
    ui.setupUi(login_dialog)
    login_dialog.show()
    sys.exit(app.exec_())

