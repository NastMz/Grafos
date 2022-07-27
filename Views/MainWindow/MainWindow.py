from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QGraphicsDropShadowEffect, QHeaderView

from Utils.Canvas import Canvas
from Views.MainWindow.MainWindowView import MainWindowView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dragPos = None
        self.ui = MainWindowView()
        self.ui.setupUi(self)
        self.graph = None

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

        self.set_option_selected(index=0)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.ui.matrix_btn.clicked.connect(lambda: self.set_option_selected(index=0))
        self.ui.list_btn.clicked.connect(lambda: self.set_option_selected(index=1))
        self.ui.graph_btn.clicked.connect(lambda: self.set_option_selected(index=2))
        self.ui.route_btn.clicked.connect(lambda: self.set_option_selected(index=3))

        self.ui.btn_calculate.clicked.connect(lambda: self.calculate_short_route(str(self.ui.from_option.currentText()),
                                                                                 str(self.ui.to_option.currentText())))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouse_move(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def set_table(self):
        # Get the nodes from the graph
        nodes = self.graph.nodes

        # Get the nodes names for the table labels
        header_labels = []
        for node in nodes:
            header_labels.append(str(node))

        # Set the count of columns and rows for the table with the number of nodes names
        self.ui.table_widget.setRowCount(len(header_labels))
        self.ui.table_widget.setColumnCount(len(header_labels))

        # Set the vertical and horizontal table labels
        self.ui.table_widget.setHorizontalHeaderLabels(header_labels)
        self.ui.table_widget.setVerticalHeaderLabels(header_labels)

        # Use the nodes to fill the table
        row = 0
        for node in nodes:

            # Set the weight of the node edges in the table
            for neighbor in nodes[node].neighbors:
                for i in range(self.ui.table_widget.columnCount()):
                    # Confirm in the node neighbor is the same of the actual column and if is the case set the weight
                    # value
                    if str(neighbor['node']) == str(self.ui.table_widget.horizontalHeaderItem(i).text()):
                        cell = QTableWidgetItem(str(neighbor['weight']))
                        cell.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                        self.ui.table_widget.setItem(i, row, cell)

            # Complete the cells without valor with zero
            for j in range(self.ui.table_widget.columnCount()):
                # If the cell don't have any value set it to zero
                if self.ui.table_widget.item(row, j) is None:
                    cell = QTableWidgetItem(str(0))
                    cell.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
                    self.ui.table_widget.setItem(row, j, cell)

            # Go to next row
            row += 1

    def set_list(self):
        for node in self.graph.nodes:
            item = f'[{node}]->'
            for neighbor in self.graph.nodes[node].neighbors:
                item += '[' + str(neighbor['node']) + ', ' + str(neighbor['weight']) + ']->'
            self.ui.listWidget.addItem(item[:-2])

    def set_graph_plot(self):
        self.ui.graph_img.addWidget(Canvas(self.graph.create(), self.graph.is_directed))
        self.ui.route_img.addWidget(Canvas(self.graph.create(), self.graph.is_directed))

    def set_option_selected(self, index):

        nonselected_style = "background-color: rgb(56, 58, 89); color: rgb(98, 114, 164);"

        selected_style = "background-color: rgb(254, 121, 199); color: rgb(255,255,255); border-radius: 20px;"

        if index == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.matrix_page)
            self.ui.matrix_btn.setStyleSheet(selected_style)
            self.ui.list_btn.setStyleSheet(nonselected_style)
            self.ui.graph_btn.setStyleSheet(nonselected_style)
            self.ui.route_btn.setStyleSheet(nonselected_style)
        elif index == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.list_page)
            self.ui.matrix_btn.setStyleSheet(nonselected_style)
            self.ui.list_btn.setStyleSheet(selected_style)
            self.ui.graph_btn.setStyleSheet(nonselected_style)
            self.ui.route_btn.setStyleSheet(nonselected_style)
        elif index == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.graph_page)
            self.ui.matrix_btn.setStyleSheet(nonselected_style)
            self.ui.list_btn.setStyleSheet(nonselected_style)
            self.ui.graph_btn.setStyleSheet(selected_style)
            self.ui.route_btn.setStyleSheet(nonselected_style)
        elif index == 3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.route_page)
            self.ui.matrix_btn.setStyleSheet(nonselected_style)
            self.ui.list_btn.setStyleSheet(nonselected_style)
            self.ui.graph_btn.setStyleSheet(nonselected_style)
            self.ui.route_btn.setStyleSheet(selected_style)

    def calculate_short_route(self, from_node, to_node):
        short_route, weight = self.graph.print_shortest_route(from_node, to_node)
        self.ui.route_text.setText(str(short_route))
        self.ui.weight_text.setText(str(weight))
        self.ui.route_img.replaceWidget(self.ui.route_img.itemAt(0).widget(),
                                        Canvas(self.graph.create(), self.graph.is_directed, short_route=short_route))
