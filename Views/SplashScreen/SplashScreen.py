# SPLASH SCREEN

from PyQt6 import QtCore
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect

from Core.Graph import Graph
from Views.FormWindow.FormWindow import FormWindow
from Views.MainWindow.MainWindow import MainWindow
from Views.SplashScreen.SplashScreenView import SplashScreenView


class SplashScreen(QMainWindow):
    def __init__(self, is_opening):
        QMainWindow.__init__(self)
        self.graph = None
        self.ui = SplashScreenView()
        self.ui.setupUi(self)
        self.isOpening = is_opening

        self.main = MainWindow()
        self.form = FormWindow(self)
        self.counter = 0

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

        if not self.isOpening:
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
            self.isOpening = False
        else:
            # TIMER IN MILLISECONDS
            self.timer.start(20)

            # CHANGE DESCRIPTION

            # Initial Text
            self.ui.label_description.setText("<STRONG> HERRAMIENTA</STRONG> DE VISUALIZACIÓN DE GRAFOS")

            QtCore.QTimer.singleShot(1500,
                                     lambda: self.ui.label_description.setText(
                                         "<strong>CARGANDO</strong> INTERFAZ DE USUARIO"))

        self.close()

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREE AND OPEN APP

        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            if not self.isOpening:
                # # SHOW MAIN WINDOW
                self.main.set_table(self.graph)
                self.main.set_list(self.graph)
                self.main.set_graph_plot(self.graph.draw(), self.graph.is_directed)
                self.main.show()
            else:
                self.form.show()
            self.close()

        # INCREASE COUNTER
        self.counter += 1

    def set_graph(self, is_directed, nodes, edges):
        self.graph = Graph(is_directed=is_directed)

        for node in nodes:
            self.graph.add_node(node)

        for edge in edges:
            e = edge.split()
            self.graph.add_edge(e[1], e[3], e[5])

        # graph.get_short_route('D', 'C')
