import re
import sys

from PyQt6.QtWidgets import QApplication

from Core.Graph import Graph
from Views.MainWindow import MainWindow
from Views.SplashScreen import SplashScreen


def main():
    app = QApplication(sys.argv)
    window = SplashScreen(is_opening=True)
    window.show()
    app.exec()


main()
