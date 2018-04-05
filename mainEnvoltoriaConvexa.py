import networkx as nx
from tools import graph_functions as gf

graph = nx.Graph()

#loading nodes
with open("input/nodesS.txt") as f:
    for line in f:
        graph.add_node(line.rstrip('\n'))

#loading edges
with open("input/edgesS.txt") as f:
    for line in f:
        u, v = line.split(',')
        graph.add_edge(u, v.rstrip('\n'))


#loading envoltoria inicial
S = []
with open("input/nodesEnvoltoriaS.txt") as f:
    for line in f:
        S.append(line.rstrip('\n'))

print('S')
print(sorted(S))
print()

I_S = []
H_S = set()
i = 0
'''
Repete a operação até que a envoltória não seja mais modificada
'''
while set(S) != H_S:

    H_S = set(S)

    result = gf.get_min_paths_lenghts_and_vertex(S, graph)

    for tam, path in result.values():
        I_S = list(set().union(I_S, path))

    if i == 0:
        i += 1
        print('Iº(S)')
        print(sorted(I_S))
        print()

    if not set(I_S).issubset(H_S):
        for u in I_S:
            if u not in H_S:
                S.append(u)
        I_S = []

print('H(S)')
print(sorted(H_S))