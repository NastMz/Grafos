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

    def get_minor(self, neighbors):
        minor = None
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if not self.nodes[neighbor['node']].visited:
                    if minor is None or neighbor['weight'] < minor['weight']:
                        minor = neighbor
        return minor

    def get_short_route(self, from_node, to_node):
        counter = 0
        weight = 0

        self.nodes[from_node].visited = True
        neighbors = self.nodes[from_node].neighbors

        short_route = [{'weight': weight, 'from': '-', 'iteration': counter}]

        end = False
        route_exist = False

        actual_node = from_node

        while not end:
            minor = self.get_minor(neighbors)
            if minor is not None:
                counter += 1
                weight += int(minor['weight'])
                actual_node = minor['node']
                if actual_node == to_node:
                    end = True
                    route_exist = True
                    short_route[-1]['weight'] = weight
                else:
                    short_route.append({'weight': weight, 'from': actual_node, 'iteration': counter})
                    self.nodes[actual_node].visited = True
                    neighbors = self.nodes[actual_node].neighbors

            elif not route_exist:
                if len(short_route) > 2:
                    counter -= 1
                    before_weight = short_route[-2]['weight']
                    actual_weight = short_route[-1]['weight']
                    weight -= int(actual_weight-before_weight)
                    short_route.pop()
                    actual_node = short_route[-1]['from']
                    neighbors = self.nodes[actual_node].neighbors
                else:
                    end = True

        return short_route, route_exist

    def print_shortest_route(self, from_node, to_node):
        if from_node != to_node:
            short_route, route_exist = self.get_short_route(from_node, to_node)
            weight = '-'
            if route_exist:
                array = f'[{from_node}, '
                for item in short_route:
                    if item['from'] != '-':
                        array += str(item['from']) + ', '
                array += f'{to_node}]'
                weight = short_route[-1]['weight']
            else:
                array = f'No existe una ruta de {from_node} a {to_node}'

            self.reset_graph()
        else:
            array = f'[{from_node}]'
            weight = 0
        return array, weight

    def reset_graph(self):
        for node in self.nodes:
            self.nodes[node].visited = False
