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

    return min_u_v_path_length == nx.shortest_path_length(G, w, u) + nx.shortest_path_length(G, w, v)


def get_set_vertex_on_min_path(u, v, G):
    """
    Encontrar o(s) caminho(s) minimo(s) entre u e v, e retornar o conjunto de
    :param u: um vertice do grafo G
    :param v: um vertice do grafo G
    :param G: Grafo de Entrada
    :return: lista de vertices que pertencem a um caminho minimo entre u e v
    """

    min_path_length = nx.shortest_path_length(G, u, v)
    vertex_in_min_path = list()

    for w in G:
        if w != u and w != v:
            if is_in_min_path(u, v, w, G, min_path_length):
                vertex_in_min_path.append(w)

    return min_path_length, vertex_in_min_path


def get_min_paths_lenghts_and_vertex(S, G):
    """
    Verificar para cada para de vértices de S, o tamanho do caminho mínimo e os vertices do caminho
    :param S: vertices
    :param G: grafo de entrada
    :return:
    """
    solution = dict()

    i = 0

    while i < len(S) - 1:
        #S.remove(u)
        j = i + 1
        while j < len(S):
            solution[(S[i], S[j])] = get_set_vertex_on_min_path(S[i], S[j], G)
            j += 1
        i += 1

    return solution
