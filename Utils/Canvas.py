import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_qtagg import FigureCanvas


class Canvas(FigureCanvas):

    def __init__(self, plot, is_directed):
        self.fig, self.ax = plt.subplots(1, figsize=(10, 10))
        super().__init__(self.fig)
        self.plot = plot
        self.is_directed = is_directed

        pos = nx.spring_layout(plot, seed=len(plot), k=10)
        edges_weight = nx.get_edge_attributes(plot, 'weight')

        nx.draw_networkx_nodes(plot, pos, node_color='#fe79c7')
        nx.draw_networkx_labels(plot, pos, font_color='#383a59', font_size=10)

        if is_directed:
            nx.draw_networkx_edges(plot, pos, arrows=True, edge_color='#6272a4')
        else:
            nx.draw_networkx_edges(plot, pos, arrows=False, edge_color='#6272a4')

        nx.draw_networkx_edge_labels(plot, pos, edge_labels=edges_weight, font_color='#383a59', clip_on=False)

        self.ax.set_facecolor('#383a59')
        self.ax.axis('off')
        self.fig.set_facecolor('#383a59')
        self.ax.plot()
