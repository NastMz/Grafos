import networkx as nx


class ShortRouteCanvas:

    def __init__(self, short_route):
        self.short_route = short_route

    def get_path_graph(self):
        short_path = nx.DiGraph()
        path = self.short_route.split()
        for i in range(len(path)):
            if path[i].__contains__('['):
                path[i] = path[i].replace('[', '')
            if path[i].__contains__(']'):
                path[i] = path[i].replace(']', '')
            if path[i].__contains__(','):
                path[i] = path[i].replace(',', '')
        for i in range(len(path) - 1):
            short_path.add_edge(path[i], path[i + 1])

        return short_path
