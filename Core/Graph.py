import networkx as nx

# Class for defining the Graph
from Core.Node import Node


class Graph:
    # Constructor
    def __init__(self, is_directed=False):
        self.nodes = {}
        self.is_directed = is_directed

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = Node(node)

    def add_edge(self, from_node, to_node, edge_weight=1):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].add_neighbor({"node": to_node, "weight": edge_weight})
            if not self.is_directed:
                self.nodes[to_node].add_neighbor({"node": from_node, "weight": edge_weight})

    def draw(self):
        G = nx.DiGraph()
        nodes = []
        edges = []
        for node in self.nodes:
            nodes.append(node)
            for neighbor in self.nodes[node].neighbors:
                edges.append((node, neighbor['node'], neighbor['weight']))

        G.add_nodes_from(nodes)
        G.add_weighted_edges_from(edges)

        return G

    def get_short_route(self, from_node, to_node):
        counter = 0
        weight = 0

        self.nodes[from_node].visited = True
        start_neighbors = self.nodes[from_node].neighbors

        short_route = [{'weight': weight, 'from': '-', 'iteration': counter}]

        end = False
        route_exist = False

        while not end:
            if start_neighbors:
                minor = None
                for neighbor in start_neighbors:
                    if not self.nodes[neighbor['node']].visited:
                        if minor is None:
                            minor = neighbor
                        if neighbor['weight'] < minor['weight']:
                            minor = neighbor
                if minor is not None:
                    if minor['node'] == to_node:
                        end = True
                        route_exist = True
                    else:
                        counter += 1
                        weight += int(minor['weight'])
                        short_route.append({'weight': weight, 'from': minor['node'], 'iteration': counter})
                        self.nodes[minor['node']].visited = True
                        before_node = minor['node']
                        start_neighbors = self.nodes[before_node].neighbors
            elif not route_exist:
                if len(short_route) > 2:
                    short_route.pop()
                    before_node = short_route[-1]['from']
                    start_neighbors = self.nodes[before_node].neighbors
                else:
                    end = True

        weight = '-'
        if route_exist:
            array = f'[{from_node}, '
            for item in short_route:
                if item['from'] != '-':
                    array += str(item['from']) + ', '
            array += str(to_node) + ']'
            weight = short_route[-1]['weight']
        else:
            array = 'No existe una ruta'

        self.reset_graph()
        return array, weight

    def reset_graph(self):
        for node in self.nodes:
            self.nodes[node].visited = False
