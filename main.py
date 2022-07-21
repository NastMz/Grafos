import re
import sys

from PyQt6.QtWidgets import QApplication

from Core.Graph import Graph
from Views.MainWindow import MainWindow
from Views.SplashScreen import SplashScreen


def main():
    graph = Graph(is_directed=True)

    nodes_list = ['A', 'B', 'C', 'D', 'D', 'E', 'F']
    edges_list = [['A', 'B', 1], ['A', 'D', 1], ['B', 'D', 1], ['B', 'C', 1], ['D', 'E', 1], ['E', 'A', 1],
                  ['E', 'B', 1], ['F', 'C', 1]]

    # nodes_list = [0, 1, 2, 3, 4, 5, 6]
    # edges_list = [[2, 0, 12], [0, 6, 15], [6, 3, 15], [0, 5, 56], [6, 5, 65], [6, 4, 54], [1, 4, 45], [0, 1, 76]]

    for node in nodes_list:
        graph.add_node(node)

    for i in range(0, len(edges_list)):
        graph.add_edge(edges_list[i][0], edges_list[i][1], edges_list[i][2])

    graph.get_short_route('D', 'C')

    app = QApplication(sys.argv)
    window = SplashScreen(graph, is_opening=True)
    window.show()
    app.exec()


main()