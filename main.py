import sys

from PyQt6.QtWidgets import QApplication

from Views.SplashScreen.SplashScreen import SplashScreen


def main():
    app = QApplication(sys.argv)
    window = SplashScreen(is_opening=True)
    window.show()
    app.exec()


main()
