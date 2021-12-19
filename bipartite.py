"bipartite.py"


def bipartite(vert_dict: dict) -> bool:
    """Divides all vertices of connected non directed graph into two parts
    and if that can be done, graph is bipartite

    Args:
        vert_dict: dict of vertices

    Returns:
        bool: whether the graph is bipartite or not

    >>> bipartite({'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['m', 'h', 'a'], 'm': ['c', 't'],\
    'h': ['c', 'n'], 't': ['m'], 'n': ['h', 'z'], 'z': ['n'], 'd': ['b'], 'e': ['b']})
    True

    >>> bipartite({'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['m', 'h', 'a'], 'm': ['c', 't'],\
    'h': ['c', 'n'], 't': ['m'], 'n': ['h', 'z'], 'z': ['n'], 'd': ['b'], 'e': ['b', 'd']})
    False

    """
    red = []
    blue = []
    vertices = list(vert_dict.keys())
    red += vertices[0]
    for vertice in vertices:
        if vertice in red:
            for item in vert_dict[vertice]:
                if item not in red:
                    blue += vert_dict[vertice]
                else:
                    return False
        else:
            for item in vert_dict[vertice]:
                if item not in blue:
                    red += vert_dict[vertice]
                else:
                    return False
    return True
