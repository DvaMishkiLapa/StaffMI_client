import os
os.system('python -m PyQt5.uic.pyuic -x main_window.ui -o main_window.py')
os.system('python -m PyQt5.uic.pyuic -x login_stack.ui -o login_stack.py')
os.system('python -m PyQt5.uic.pyuic -x add_inproject_dialog.ui -o add_inproject_dialog.py')
os.system('python -m PyQt5.uic.pyuic -x add_new_user_dialog.ui -o add_new_user_dialog.py')