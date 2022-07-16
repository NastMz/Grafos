import matplotlib.pyplot as plt
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
            self.nodes[from_node].add_neighbor({"neighbor": to_node, "weight": edge_weight})
            if not self.is_directed:
                self.nodes[to_node].add_neighbor({"neighbor": from_node, "weight": edge_weight})

    def draw(self):
        G = nx.DiGraph()
        nodes = []
        edges = []
        for node in self.nodes:
            nodes.append(node)
            for neighbor in self.nodes[node].neighbors:
                edges.append((node, neighbor['neighbor'], neighbor['weight']))

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

        before_node = from_node

        while not end:
            if start_neighbors:
                minor = None
                for neighbor in start_neighbors:
                    if not self.nodes[neighbor['neighbor']].visited:
                        if minor is None:
                            minor = neighbor
                        if neighbor['weight'] < minor['weight']:
                            minor = neighbor
                if minor is not None:
                    counter += 1
                    weight += minor['weight']
                    short_route.append({'weight': weight, 'from': before_node, 'iteration': counter})
                    if minor['neighbor'] != before_node:
                        before_node = minor['neighbor']
                        self.nodes[before_node].visited = True
                        start_neighbors = self.nodes[before_node].neighbors
                    else:
                        short_route.pop(len(short_route)-1)
                        counter -= 1
                        weight -= minor['weight']
                        before_node = self.nodes[short_route.__getitem__(len(short_route) - 1)['from']]
                        start_neighbors = self.nodes[short_route.__getitem__(len(short_route) - 1)['from']].neighbors
                    if before_node == to_node:
                        end = True
                        route_exist = True
                else:
                    counter -= 1
                    for neighbor in self.nodes[short_route.__getitem__(len(short_route) - 1)['from']].neighbors:
                        if before_node == neighbor['neighbor']:
                            weight -= neighbor['weight']
                    before_node = self.nodes[short_route.__getitem__(len(short_route) - 1)['from']].id
                    start_neighbors = self.nodes[short_route.__getitem__(len(short_route) - 1)['from']].neighbors
                    short_route.pop(len(short_route) - 1)
            else:
                counter -= 1
                for neighbor in self.nodes[short_route.__getitem__(len(short_route) - 1)['from']].neighbors:
                    if before_node == neighbor['neighbor']:
                        weight -= neighbor['weight']
                before_node = self.nodes[short_route.__getitem__(len(short_route) - 1)['from']].id
                start_neighbors = self.nodes[short_route.__getitem__(len(short_route) - 1)['from']].neighbors
                short_route.pop(len(short_route) - 1)
            if len(short_route) <= 1:
                end = True

        if route_exist:
            print(short_route)
        else:
            print('No existe una ruta')