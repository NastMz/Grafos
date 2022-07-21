import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QApplication
from AlertView import AlertView


class Alert(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = AlertView()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui.btn_accept.clicked.connect(lambda: self.close())

    def set_message(self, message):
        self.ui.message_label.setText(message)
