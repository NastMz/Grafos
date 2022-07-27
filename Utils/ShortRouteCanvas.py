import networkx as nx


class ShortRouteCanvas:

    def __init__(self, short_route):
        self.short_route = short_route
        self.path = self.get_path()

    def get_path_graph(self):
        short_path = nx.DiGraph()
        if len(self.path) > 1:
            for i in range(len(self.path) - 1):
                short_path.add_edge(self.path[i], self.path[i + 1])

        return short_path

    def get_path(self):
        path = self.short_route.split()
        for i in range(len(path)):
            if path[i].__contains__('['):
                path[i] = path[i].replace('[', '')
            if path[i].__contains__(']'):
                path[i] = path[i].replace(']', '')
            if path[i].__contains__(','):
                path[i] = path[i].replace(',', '')
        return path
