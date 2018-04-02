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


#loading envoltoria inicial
envoltoria_inicial = []
with open("input/nodesEnvoltoria.txt") as f:
    for line in f:
        envoltoria_inicial.append(line.rstrip('\n'))
#target_nodes = [u for u in graph.nodes if graph.degree[u] == 1]

nodes_in_solution = []

'''
Repete a operação até que a envoltória não seja mais modificada
'''

envoltoria = set()

while set(envoltoria_inicial) != envoltoria:

    envoltoria = set(envoltoria_inicial)

    result = gf.get_min_paths_lenghts_and_vertex(envoltoria_inicial, graph)

    for tam, path in result.values():
        nodes_in_solution = list(set().union(nodes_in_solution, path))

    if not set(nodes_in_solution).issubset(envoltoria):
        for u in nodes_in_solution:
            if u not in envoltoria:
                envoltoria_inicial.append(u)
        nodes_in_solution = []

print(envoltoria)
#for item in envoltoria:
#    print(item)