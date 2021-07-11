from sys import argv, exit
import application
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(argv)
    window = application.MainWindow()
    window.showMaximized()
    exit(app.exec_())
