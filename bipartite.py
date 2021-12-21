"bipartite.py"

def bipartite(vert_dict: dict) -> bool:
    """
    Divides all vertices of connected non directed graph into two parts
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

    >>> bipartite({'a':['b'],'c':['d'],'b':['a','k'],'d':['k','c'],'k':['d','b']})
    True
    """
    blue = set()
    vert_left = True
    red = set()
    for vertice in vert_dict:
        red.add(vertice)
        break
    while vert_left:
        vert_left=False
        for vertice in vert_dict:
            if vertice in red:
                for item in vert_dict[vertice]:
                    if item not in red:
                        if item not in blue:
                            blue.add(item)
                    else:
                        return False
            elif vertice in blue:
                for item in vert_dict[vertice]:
                    if item not in blue:
                        if item not in red:
                            red.add(item)
                    else:
                        return False
            else:
                vert_left=True

    return True

# if __name__=='__main__':
#     import input
    # import time
    # time1=time.time()
    # graph=input.read_csv('/mnt/c/Users/vovak/Downloads/bipartie_5000_3126273_try3.csv')
    # print(time.time()-time1)
    # print(bipartite(graph))
    # print(time.time()-time1)
    # import doctest
    # doctest.testmod()
