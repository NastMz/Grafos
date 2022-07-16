# Class for defining a node
class Node:
    # Constructor
    def __init__(self, node_id):
        self.id = node_id
        self.visited = False
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
