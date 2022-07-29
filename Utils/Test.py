import networkx as nx

from Core.Graph import Graph

graph = Graph(is_directed=True)

nodes_list = [0, 1, 2, 3, 4, 5]

for node in nodes_list:
    graph.add_node(node)

edges_list = [[1, 2, 100], [1, 3, 30], [2, 3, 20], [3, 4, 10], [4, 2, 15], [4, 5, 50], [3, 5, 60]]

for i in range(0, len(edges_list)):
    graph.add_edge(edges_list[i][0], edges_list[i][1], edges_list[i][2])

G = graph.create()

from_node = 1
to_node = 5

print(nx.dijkstra_path(G, from_node, to_node), nx.dijkstra_path_length(G, from_node, to_node))
print(graph.print_shortest_route(from_node, to_node))
