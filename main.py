import networkx as nx
from tools import graph_functions as gf

graph = nx.Graph()

#loading nodes
with open("input/nodesb.txt") as f:
    for line in f:
        graph.add_node(line.rstrip('\n'))

#loading edges
with open("input/edgesb.txt") as f:
    for line in f:
        u, v = line.split(',')
        graph.add_edge(u, v.rstrip('\n'))

target_nodes = [u for u in graph.nodes if graph.degree[u] == 1]

result = gf.get_min_paths_lenghts_and_vertex(target_nodes, graph)

for item in result.items():
    print(item)


nodes_in_solution = []

for tam, path in result.values():
    nodes_in_solution = list(set().union(nodes_in_solution, path))

print()
print('Nodes not in any path:')

for node in graph.nodes:
    if node not in nodes_in_solution and node not in target_nodes:
        print(node)



#print(item,file="output/result1.txt")
