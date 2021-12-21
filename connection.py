"""
Module checking whether graph is connected or not.
"""


def connection(graph1: dict) -> bool:
    """Check if graph is connected.
    Args:
        graph1 (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values

    Returns:
        bool: True if connected and False if not
    
    >>> print(connection({5:[6, 10],8:[6,10],10:[8],6:[5,8], 7:[]}))
    False

    >>> print(connection({5:[6, 10],8:[6,10],10:[8],6:[5,8]}))
    True
    """
    graph=graph1.copy()

    for vertice in graph:
            for vert in graph[vertice]:
                if vertice not in graph[vert]:
                    graph[vert].append(vertice)

    for i in graph:
        vert={i}
        break
    while graph!={}:
        graph1=graph.copy()
        for i in vert:
            if i in graph:
                vert=vert | set(graph[i])
                del graph[i]
        if graph==graph1:
            return False
    return True

# if __name__=='__main__':
    # graph={5:[6],8:[6,10],10:[8],6:[5,8]}
    # print(connection(graph))
