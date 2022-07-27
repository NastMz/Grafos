import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_qtagg import FigureCanvas

from Utils.ShortRouteCanvas import ShortRouteCanvas


class Canvas(FigureCanvas):

    def __init__(self, graph, is_directed, short_route=None):
        self.fig, self.ax = plt.subplots(1, figsize=(10, 10))
        super().__init__(self.fig)
        self.plot = graph
        self.is_directed = is_directed

        pos = nx.circular_layout(graph)
        edges_weight = nx.get_edge_attributes(graph, 'weight')

        nx.draw_networkx_nodes(graph, pos, node_color='#d665a9')
        nx.draw_networkx_labels(graph, pos, font_color='#383a59', font_size=10)

        if is_directed:
            nx.draw_networkx_edges(graph, pos, arrows=True, edge_color='#6272a4')
        else:
            nx.draw_networkx_edges(graph, pos, arrows=False, edge_color='#6272a4')

        if short_route and not short_route.__contains__('No existe una ruta'):
            short_path_canvas = ShortRouteCanvas(short_route)
            short_path_graph = short_path_canvas.get_path_graph()
            if is_directed:
                nx.draw(short_path_graph, pos=pos, arrows=True, edge_color='#ffffff', node_color='#fe79c7',
                        width=2)
            else:
                nx.draw(short_path_graph, pos=pos, arrows=False, edge_color='#ffffff', node_color='#fe79c7',
                        width=2)

        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edges_weight, font_color='#383a59', label_pos=0.8,
                                     clip_on=False)

        self.ax.set_facecolor('#383a59')
        self.ax.axis('off')
        self.fig.set_facecolor('#383a59')
        self.ax.plot()
