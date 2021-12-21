"""
Module coloring all vertexes in graphs three colours.
"""
import input


def search(graph: dict,coloring: dict) -> dict:
    """Build suggestion pairs vertex-colour and choose the right one, if exists.

    Args:
        graph (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values
    
        coloring (dict): a dictionary with already coloured vertexes as keys and
        colours as values
    
    Returns:
        dict: an updated dictionary if such coloring option exists, else Fasle

    >>> print(search({1: [2, 5], 2: [1, 5], 3: [4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}, {1: 'r', 2: 'g'}))
    {1: 'r', 2: 'g', 5: 'b'}

    """
    vertices=list(coloring.keys())
    for i in vertices:
        for j in vertices:
            if i==j or coloring[i]==coloring[j]:
                continue
            for k in set(graph[i]) & set(graph[j]):
                if k not in coloring:
                    vertices.append(k)
                    possible_colors=['r','g','b']
                    possible_colors.remove(coloring[i])
                    possible_colors.remove(coloring[j])
                    coloring[k]=possible_colors[0]
                elif coloring[k] in [coloring[i],coloring[j]]:
                    return False
    return coloring


def find_coloring(graph: dict,oriented=False):
    """Colour all vertexes in the graph.

    Args:
        graph (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values
    
        oriented (the default is False): whether graph is oriented or not.
    
    Returns:
        dict_items: list with tuples (vertex, colour)

    >>> print(find_coloring({1: [2, 5], 2: [1, 5], 3: [4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}))
    dict_items([(1, 'r'), (2, 'g'), (5, 'b'), (3, 'r'), (4, 'r')])
    """
    if oriented:
        for vertice in graph:
            for vert in graph[vertice]:
                graph[vert].append(vertice)

    coloring={}
    for i in graph:
        coloring[i]='r'
        coloring[graph[i][0]]='g'
        break

    stack=[]
    while len(coloring)!=len(graph):
        result=search(graph,coloring)
        if result is False and stack==[]:
            print('There is no solution')
            return False
        elif result is False:
            for i in stack[-1]:
                del coloring[i[0]]
            stack.pop()
        elif stack!=[]:
            coloring=result
            basis=stack[-1]
            stack.pop()
            for j in graph:
                if j not in coloring:
                    possible_colors=['r','g','b']
                    for k1 in graph[j]:
                        if k1 in coloring:
                            possible_colors.remove(coloring[k1])
                            break
                    for k2 in possible_colors:
                        stack.append(basis+[(j,k2)])
                    break
        else:
            if len(coloring)==len(graph):
                return coloring.items()
            coloring=result
            for j in graph:
                if j not in coloring:
                    possible_colors=['r','g','b']
                    for k1 in graph[j]:
                        if k1 in coloring:
                            possible_colors.remove(coloring[k1])
                            break
                    for k2 in possible_colors:
                        stack.append([(j,k2)])
                    break
        
        if stack==[]:
            print('There is no solution')
            return False
        
        for k in stack[-1]:
            coloring[k[0]]=k[1]

    return coloring.items()

# if __name__=="__main__":
    # graph=input.read_csv('/mnt/c/Users/user/Downloads/colour_tes.csv')
    # result = find_coloring(graph)
    # if result:
    #     for i in sorted(result):
    #         print(f'{i[0]} - {i[1]}')
