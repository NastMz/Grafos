import re
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from Alert import Alert
from FormWindowView import FormWindowView


class FormWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = FormWindowView()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.alert = Alert()
        self.nodes = []
        self.edges = []

        self.ui.btn_dir.clicked.connect(lambda: self.set_directed(is_directed=True))
        self.ui.btn_nodir.clicked.connect(lambda: self.set_directed(is_directed=False))
        self.ui.btn_infone.clicked.connect(lambda: self.set_num_nod_edg(self.ui.nnodes.value()))
        self.ui.btn_addnamenode.clicked.connect(lambda: self.set_name_nodes(self.ui.namenode.text()))
        self.ui.btn_next.clicked.connect(lambda: self.validation_next())
        self.ui.btn_addedge.clicked.connect(lambda: self.set_edges(self.ui.originnode.text(), self.ui
                                                                   .destinynode.text(), self.ui.weight.value()))

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
        elif len(self.nodes) < self.number_nodes and name_node not in self.nodes:
            self.nodes.append(name_node)
            self.ui.namenode.setText("")
            self.ui.list_namenode.addItem(name_node)
            self.ui.label_nodes.setText("V = " + str(self.nodes))
        elif name_node in self.nodes:
            self.alert.set_message("El nodo '" + name_node + "' ya fue ingresado.")
            self.alert.show()
        else:
            self.ui.btn_addnamenode.setEnabled(False)
            self.alert.set_message("No puede superar el número de nodos ingresados.")
            self.alert.show()

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
            edge = "(" + str(from_node) + ", " + str(to_node) + ", " + str(weight) + ")"
            flag = False
            for item in self.edges:
                f_node = item[1]
                t_node = item[4]
                print(f_node)
                print(t_node)
                if from_node == f_node and to_node == t_node:
                    self.alert.set_message("La arista ya está en la lista.")
                    self.alert.show()
                    flag = True
                    break
            if not flag:
                self.edges.append(edge)
                self.ui.list_edges.addItem(edge)
                if not self.directed:
                    reverse_edge = "(" + str(to_node) + ", " + str(from_node) + ", " + str(weight) + ")"
                    self.edges.append(reverse_edge)
                    self.ui.list_edges.addItem(reverse_edge)
                self.ui.originnode.setText("")
                self.ui.destinynode.setText("")
                self.ui.weight.setValue(0)
        else:
            self.alert.set_message("Uno o más nodos no pertenecen a la lista de nodos ingresado.")
            self.alert.show()


app = QApplication(sys.argv)
window = FormWindow()
window.show()
app.exec()
