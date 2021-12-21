"""
Module finding Hamiltonian circuits in graphs.
"""
import input


def search(stack: list, graph: dict) -> list:
    """Additional fucntion to look for Hamiltonian circuit in graph.

    Args:
        stack (list): the list with the initial vertex,
        the possible Hamiltonian circuit will be saved in it

        graph (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values

    Returns:
        list: if Hamiltonian circuit exists or False if it doesn`t

    """
    if len(stack)==len(graph)+1:
        return stack
    if len(stack)==len(graph):
        pos_opt=set(graph[stack[-1]])-set(stack[1:-1])
    else:
        pos_opt=set(graph[stack[-1]])-set(stack[:-1])
    if pos_opt==set():
        return False
    for i in pos_opt:
        result=search(stack+[i],graph)
        if result is not False:
            return result
    return False


def hamiltonian(graph: dict) -> list:
    """Look for Hamiltonian circuit.

    Args:
        graph (dict): a dictionary with vertexes as keys and
        lists of adjacent vertexes as values

    Returns:
        list: if Hamiltonian circuit exists or False if there`s no one
    
    >>> print(hamiltonian({'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['a','b']}))
    ['a', 'b', 'c', 'a']
    """
    for i in graph:
        stack_start=[i]
        break
    return search(stack_start,graph)

# if __name__=='__main__':
    # graph=input.read_csv('graph.py')
    # print(hamiltonian(graph))
