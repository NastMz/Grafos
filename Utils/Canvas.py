import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_qtagg import FigureCanvas


class Canvas(FigureCanvas):

    def __init__(self, plot, is_directed, parent=None):
        self.fig, self.ax = plt.subplots(1, figsize=(10, 10))
        super().__init__(self.fig)

        pos = nx.spring_layout(plot, seed=len(plot), k=10)
        edges_weight = nx.get_edge_attributes(plot, 'weight')

        nx.draw_networkx_nodes(plot, pos)
        nx.draw_networkx_labels(plot, pos)

        if is_directed:
            nx.draw_networkx_edges(plot, pos, arrows=True)
        else:
            nx.draw_networkx_edges(plot, pos, arrows=False)

        nx.draw_networkx_edge_labels(plot, pos, edge_labels=edges_weight)

        # print(nx.dijkstra_path(plot, source='D', target='C'))

        self.ax.axis('off')
        self.ax.plot()
