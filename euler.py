"""
Module looking for Euler circuits in graphs.
"""
import connection


def from_dict(G: dict) -> list:
    """Additional fucntion to look for Euler circuit in graph.

    Args:
        G (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values

    Returns:
        list: the list with edges as tuples

    >>> print(from_dict({1: [2, 5], 2: [1, 5], 3: [4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}))
    [(1, 2), (1, 5), (2, 1), (2, 5), (3, 4), (3, 5), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]

    """
    links = []
    for u in G:
        for v in G[u]:
            links.append((u,v))
    return links

def fleury(G: dict) -> list:
    """Does Fleury algorithm to find Euler circuit.

    Args:
        G (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values

    Returns:
        list: the list which contains a sequence of vertexes which form Euler circuit

    >>> print(fleury({'1': ['2', '5'], '2': ['1', '5'], '3': ['5', '4'], '4': ['3', '5'], '5': ['1', '2', '3', '4']}))
    ['1', '2', '5', '4', '3', '5', '1']

    """
    for item in G:
        if len(G[item]) % 2 != 0:
            return 'Not Eulerian Graph'
    trail = []
    for u in G:
        break
    while len(from_dict(G)) > 0:
        current_vertex = u
        for u in G[current_vertex]:
            G[current_vertex].remove(u)
            G[u].remove(current_vertex)
            bridge = not connection.connection(G)
            if bridge:
                G[current_vertex].append(u)
                G[u].append(current_vertex)
            else:
                break
        if bridge:
            G[current_vertex].remove(u)
            G[u].remove(current_vertex)
            G.pop(current_vertex)
        trail.append((current_vertex, u))
    list_of = []
    for item in trail:
        list_of.append(item[0])
    list_of.append(list_of[0])
    return list_of

# if __name__=='__main__':
    # print(fleury({1: [2, 5], 2: [1, 5], 3: [4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}))
