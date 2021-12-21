"""
Module checking two graphs for isomorphism
"""
import connection
import itertools



def izomorph(graph1: dict, graph2: dict) -> bool:
    """Check if two graphs are isomorphic.

    Args:
        graph1 (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values
    
        graph2 (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values
    
    Returns:
        bool: True if isomorphic and False if not
    
    """
    graph1={i:set(k) for i,k in graph1.items()}
    graph2={i:set(k) for i,k in graph2.items()}
    if not connection.connection(graph1) or not connection.connection(graph2):
        print('Wrong type of graph')
        return False

    if len(graph1)!=len(graph2):
        return False

    graphch1=graph1.copy()
    graphch2=graph2.copy()
    for vertex1 in list(graphch1):
        for vertex2 in list(graphch2):
            if vertex1 in graphch1 and vertex2 in graphch2:
                if len(graphch1[vertex1])==len(graphch2[vertex2]):
                    del graphch1[vertex1]
                    del graphch2[vertex2]
    if graphch1!={} or graphch2!={}:
        return False

    graph_lst1=tuple(graph1)
    graph_lst2=tuple(graph2)
    for perm in itertools.permutations(graph_lst2):
        dct1={perm[k1]:graph_lst1[k1] for k1 in range(len(graph1))}
        option={dct1[k]: set([dct1[j] for j in graph2[k]]) for k in graph_lst2}
        if graph1==option:
            return True
    return False



# if __name__=='__main__':
    # import input
    # graph1=input.read_csv('/mnt/c/Users/user/Downloads/samoper_1.csv')
    # graph2=input.read_csv('/mnt/c/Users/user/Downloads/samoper_2.csv')
    # print(izomorph(graph1,graph2))
