import networkx as nx


def is_in_min_path(u, v, w, G, min_u_v_path_length):
    """
    Verifica se w pertence a um caminho minimo de u e v"
    :param u: origem
    :param v: destino
    :param w: vertice a ser verificado se está no caminho minimo de u e v
    :param G: Grafo original
    :param min_u_v_path_length: tamanho do caminho minimo de u e v
    :return:
    """

    return min_u_v_path_length == nx.shortest_path(G, w, u) + nx.shortest_path(G, w, v)


def get_set_vertex_on_min_path(u, v, G):
    """
    Encontrar o(s) caminho(s) minimo(s) entre u e v, e retornar o conjunto de
    :param u: um vertice do grafo G
    :param v: um vertice do grafo G
    :param G: Grafo de Entrada
    :return: lista de vertices que pertencem a um caminho minimo entre u e v
    """

    min_path_length = nx.shortest_path_length(G, u, v)
    vertex_in_min_path = [[]]
    vertex_in_min_path[0] = min_path_length

    for w in G:
        if is_in_min_path(u, v, w, G, min_path_length):
            vertex_in_min_path[1].append(w)

    return vertex_in_min_path


def get_min_paths_lenghts_and_vertex(S, G):
    """
    Verificar para cada para de vértices de S, o tamanho do caminho mínimo e os vertices do caminho
    :param S: vertices
    :param G: grafo de entrada
    :return:
    """
    l = [[]]

    for u in S:
        S.remove(u)
        for v in S:
            l[u][v] = get_set_vertex_on_min_path(u, v, G)

    return l
