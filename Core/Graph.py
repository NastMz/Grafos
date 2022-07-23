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
        neighbors = self.nodes[from_node].neighbors

        short_route = [{'weight': weight, 'from': '-', 'iteration': counter}]

        end = False
        route_exist = False

        before_node = from_node

        while not end:
            if neighbors:
                minor = None
                for neighbor in neighbors:
                    if not self.nodes[neighbor['node']].visited:
                        if minor is None or neighbor['weight'] < minor['weight']:
                            minor = neighbor
                if minor is not None:
                    counter += 1
                    weight += int(minor['weight'])
                    short_route.append({'weight': weight, 'from': before_node, 'iteration': counter})
                    self.nodes[before_node].visited = True
                    before_node = minor['node']
                    neighbors = self.nodes[before_node].neighbors
                    if minor['node'] == to_node:
                        end = True
                        route_exist = True
            elif not route_exist:
                if len(short_route) > 2:
                    short_route.pop()
                    before_node = short_route[-1]['from']
                    neighbors = self.nodes[before_node].neighbors
                else:
                    end = True

        weight = '-'
        if route_exist:
            array = '['
            for item in short_route:
                if item['from'] != '-':
                    array += str(item['from']) + ', '
            array += str(to_node) + ']'
            weight = short_route[-1]['weight']
            print(short_route)
        else:
            array = f'No existe una ruta de {from_node} a {to_node}'

        self.reset_graph()
        return array, weight

    def reset_graph(self):
        for node in self.nodes:
            self.nodes[node].visited = False
