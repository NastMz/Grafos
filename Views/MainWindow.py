from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from Utils.Canvas import Canvas
from Views.MainWindowView import MainWindowView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dragPos = None
        self.view = MainWindowView()
        self.view.setupUi(MainWindow=self)

        self.view.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.view.close_btn.clicked.connect(lambda: self.close())

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.view.frame_header.mouseMoveEvent = self.mouse_move

        self.view.matrix_btn.clicked.connect(lambda: self.view.stackedWidget.setCurrentWidget(self.view.matrix_page))
        self.view.list_btn.clicked.connect(lambda: self.view.stackedWidget.setCurrentWidget(self.view.list_page))
        self.view.graph_btn.clicked.connect(lambda: self.view.stackedWidget.setCurrentWidget(self.view.graph_page))
        self.view.route_btn.clicked.connect(lambda: self.view.stackedWidget.setCurrentWidget(self.view.route_page))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouse_move(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def set_table(self, graph):
        # Get the nodes from the graph
        nodes = graph.nodes

        # Get the nodes names for the table labels
        header_labels = []
        for node in nodes:
            header_labels.append(str(node))

        # Set the count of columns and rows for the table with the number of nodes names
        self.view.table_widget.setRowCount(len(header_labels))
        self.view.table_widget.setColumnCount(len(header_labels))

        # Set the vertical and horizontal table labels
        self.view.table_widget.setHorizontalHeaderLabels(header_labels)
        self.view.table_widget.setVerticalHeaderLabels(header_labels)

        # Use the nodes to fill the table
        row = 0
        for node in nodes:

            # Set the weight of the node edges in the table
            for neighbor in nodes[node].neighbors:
                for i in range(self.view.table_widget.columnCount()):
                    # Confirm in the node neighbor is the same of the actual column and if is the case set the weight
                    # value
                    if str(neighbor['neighbor']) == str(self.view.table_widget.horizontalHeaderItem(i).text()):
                        cell = QTableWidgetItem(str(neighbor['weight']))
                        self.view.table_widget.setItem(row, i, cell)

            # Complete the cells without valor with zero
            for j in range(self.view.table_widget.columnCount()):
                # If the cell don't have any value set it to zero
                if self.view.table_widget.item(row, j) is None:
                    cell = QTableWidgetItem(str(0))
                    self.view.table_widget.setItem(row, j, cell)

            # Go to next row
            row += 1

    def set_list(self, graph):
        for node in graph.nodes:
            item = f'[{node}]->'
            for neighbor in graph.nodes[node].neighbors:
                item += '[' + str(neighbor['neighbor']) + ', ' + str(neighbor['weight']) + ']->'
            self.view.listWidget.addItem(item[:-2])

    def set_graph_plot(self, plot, is_directed):
        self.view.graph_img.addWidget(Canvas(plot, is_directed))
