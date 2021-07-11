import sys
from PyQt5.QtWidgets import QApplication
import ui

app = QApplication(sys.argv)
form = ui.MainWindow()
form.showMaximized()
sys.exit(app.exec_())
