import re

from PyQt6 import QtCore
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect

from Views.Alert.Alert import Alert
from Views.FormWindow.FormWindowView import FormWindowView


class FormWindow(QMainWindow):
    def __init__(self, splash_screen):
        QMainWindow.__init__(self)
        self.dragPos = None
        self.number_nodes = None
        self.ui = FormWindowView()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.splashScreen = splash_screen

        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.close_btn.clicked.connect(lambda: self.close())

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

        self.ui.frame_header.mouseMoveEvent = self.mouse_move

        self.alert = Alert()
        self.nodes = []
        self.edges = []
        self.directed = False

        self.ui.btn_dir.clicked.connect(lambda: self.set_directed(is_directed=True))
        self.ui.btn_nodir.clicked.connect(lambda: self.set_directed(is_directed=False))
        self.ui.btn_infone.clicked.connect(lambda: self.set_num_nod_edg(self.ui.nnodes.value()))
        self.ui.btn_addnamenode.clicked.connect(lambda: self.set_name_nodes(self.ui.namenode.text()))
        self.ui.btn_next.clicked.connect(lambda: self.validation_next())
        self.ui.btn_addedge.clicked.connect(
            lambda: self.set_edges(self.ui.originnode.text(), self.ui.destinynode.text(), self.ui.weight.value()))
        self.ui.btn_finish.clicked.connect(lambda: self.open_main_window())

        self.ui.page0_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.welcome_page))
        self.ui.page1_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.graphinfo_page))
        self.ui.page2_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.infonode_page))

        self.ui.remove_btn.clicked.connect(lambda: self.remove_item(2))
        self.ui.remove_btn_2.clicked.connect(lambda: self.remove_item(3))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouse_move(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def set_directed(self, is_directed):
        self.directed = is_directed
        self.ui.stackedWidget.setCurrentWidget(self.ui.graphinfo_page)

    def set_num_nod_edg(self, num_nodes):
        self.number_nodes = num_nodes
        if num_nodes == 0:
            self.alert.set_message("Ingrese un valor distinto a 0.")
            self.alert.show()
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.infonode_page)

    def set_name_nodes(self, name_node):
        validate = re.match('\w+', name_node, re.I)
        if not validate:
            self.alert.set_message("Ingrese el nombre del nodo.")
            self.alert.show()
        elif len(self.nodes) <= self.number_nodes and name_node not in self.nodes:
            self.nodes.append(name_node)
            self.ui.namenode.setText("")
            self.ui.list_namenode.addItem(name_node)
            self.ui.label_nodes.setText("V = " + str(self.nodes))
        elif name_node in self.nodes:
            self.alert.set_message("El nodo '" + name_node + "' ya fue ingresado.")
            self.alert.show()
        else:
            self.alert.set_message("No puede superar el número de nodos ingresados.")
            self.alert.show()
        if len(self.nodes) < self.number_nodes:
            self.ui.btn_addnamenode.setEnabled(True)
            self.ui.btn_addnamenode.setStyleSheet("background-color: rgb(254, 121, 199);")
        else:
            self.ui.btn_addnamenode.setEnabled(False)
            self.ui.btn_addnamenode.setStyleSheet("background-color:  rgb(214,101,169);")
        self.ui.namenode.setFocus()

    def validation_next(self):
        if len(self.nodes) < self.number_nodes:
            self.alert.set_message("Aún quedan " + str(self.number_nodes - len(self.nodes)) + " nodos por nombrar.")
            self.alert.show()
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.infoedge_page)

    def set_edges(self, from_node, to_node, weight):

        validate_from = re.match('\w+', from_node, re.I)
        validate_to = re.match('\w+', to_node, re.I)
        if not validate_from or not validate_to or weight == 0:
            self.alert.set_message("Rellene todos los campos.")
            self.alert.show()
        elif from_node in self.nodes and to_node in self.nodes:
            edge = "( " + str(from_node) + " , " + str(to_node) + " , " + str(weight) + " )"
            flag = False
            for item in self.edges:
                e = item.split()
                f_node = e[1]
                t_node = e[3]
                if from_node == f_node and to_node == t_node:
                    self.alert.set_message("La arista ya fue ingresada a la lista.")
                    self.alert.show()
                    flag = True
                    break
            if not flag:
                self.edges.append(edge)
                self.ui.list_edges.addItem(edge)
                self.ui.originnode.setText("")
                self.ui.destinynode.setText("")
                self.ui.weight.setValue(0)
        else:
            self.alert.set_message("Uno o más nodos no pertenecen a la lista de nodos ingresado.")
            self.alert.show()
        self.ui.originnode.setFocus()

    def open_main_window(self):
        self.splashScreen.__init__(is_opening=False)
        self.splashScreen.set_graph(is_directed=self.directed, nodes=self.nodes, edges=self.edges)
        self.splashScreen.show()
        self.close()

    def remove_item(self, page_index):
        if page_index == 2:
            for item in self.ui.list_namenode.selectedItems():
                self.nodes.remove(item.text())
                self.ui.list_namenode.takeItem(self.ui.list_namenode.row(item))
            self.ui.list_namenode.clearSelection()
        if page_index == 3:
            for item in self.ui.list_edges.selectedItems():
                self.edges.remove(item.text())
                self.ui.list_edges.takeItem(self.ui.list_edges.row(item))
            self.ui.list_edges.clearSelection()
        if len(self.nodes) < self.number_nodes:
            self.ui.btn_addnamenode.setEnabled(True)
            self.ui.btn_addnamenode.setStyleSheet("background-color: rgb(254, 121, 199);")
