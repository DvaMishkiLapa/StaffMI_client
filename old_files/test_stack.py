import json
import sys
from PyQt5 import QtWidgets
import stack




    # def closeEvent(self, event):
    #     event.accept()
    #     quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = login_stack()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()