import networkx as nx

from Core.Graph import Graph

graph = Graph(is_directed=True)

nodes_list = [0, 1, 2, 3, 4, 5, 6]

for node in nodes_list:
    graph.add_node(node)

edges_list = [[2, 0, 12], [0, 6, 15], [6, 3, 15], [0, 5, 56], [6, 5, 65], [6, 4, 54], [1, 4, 45], [0, 1, 76]]

for i in range(0, len(edges_list)):
    graph.add_edge(edges_list[i][0], edges_list[i][1], edges_list[i][2])

G = graph.draw()

from_node = 2
to_node = 2

print(nx.dijkstra_path(G, from_node, to_node), nx.dijkstra_path_length(G, from_node, to_node))
print(graph.print_shortest_route(from_node, to_node))
