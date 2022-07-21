# SPLASH SCREEN
import re

from PyQt6 import QtCore
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect

from Views.MainWindow import MainWindow
from Views.SplashScreenView import SplashScreenView

# ==> GLOBALS
counter = 0


class SplashScreen(QMainWindow):
    def __init__(self, graph, is_opening):
        QMainWindow.__init__(self)
        self.ui = SplashScreenView()
        self.ui.setupUi(self)

        self.graph = graph
        self.main = MainWindow()

        # UI ==> INTERFACE CODES
        ########################################################################

        # REMOVE TITLE BAR
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        if not is_opening:
            # TIMER IN MILLISECONDS
            self.timer.start(25)

            # CHANGE DESCRIPTION

            # Initial Text
            self.ui.label_description.setText("<STRONG> HERRAMIENTA</STRONG> DE VISUALIZACIÓN DE GRAFOS")

            # Change Texts
            QtCore.QTimer.singleShot(1000, lambda: self.ui.label_description.setText(
                "<strong>CARGANDO</strong> MATRIZ DE ADYACENCIA"))

            QtCore.QTimer.singleShot(1500,
                                     lambda: self.ui.label_description.setText(
                                         "<strong>CARGANDO</strong> LISTA DE ADYACENCIA"))

            QtCore.QTimer.singleShot(2000,
                                     lambda: self.ui.label_description.setText(
                                         "<strong>CARGANDO</strong> GRAFICO"))

            QtCore.QTimer.singleShot(2500,
                                     lambda: self.ui.label_description.setText(
                                         "<strong>CARGANDO</strong> INTERFAZ DE USUARIO"))
        else:
            # TIMER IN MILLISECONDS
            self.timer.start(20)

            # CHANGE DESCRIPTION

            # Initial Text
            self.ui.label_description.setText("<STRONG> HERRAMIENTA</STRONG> DE VISUALIZACIÓN DE GRAFOS")

            QtCore.QTimer.singleShot(1500,
                                     lambda: self.ui.label_description.setText(
                                         "<strong>CARGANDO</strong> INTERFAZ DE USUARIO"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        # self.show()
        # ==> END #

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP

        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # # SHOW MAIN WINDOW
            self.main.set_table(self.graph)
            self.main.set_list(self.graph)
            self.main.set_graph_plot(self.graph.draw(), self.graph.is_directed)
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


