import networkx as nx
from tools import graph_functions as gf

graph = nx.Graph()

#loading nodes
with open("input/nodes.txt") as f:
    for line in f:
        graph.add_node(line.rstrip('\n'))

#loading edges
with open("input/edges.txt") as f:
    for line in f:
        u, v = line.split(',')
        graph.add_edge(u, v.rstrip('\n'))

target_nodes = [graph.degree[u] == 1 for u in graph.nodes]

result = gf.get_min_paths_lenghts_and_vertex(target_nodes, graph)

print(result)
