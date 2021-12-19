"bipartite.py"

import time
start_time = time.time()

def read_csv(path):
    res={}

    # oriented=input('Your graph is oriented?(y/n) ')
    # while oriented not in ['y','n']:
    #     oriented=input('Incorrect input. Your graph is oriented?(y/n) ')
    # if oriented=='y':
    #     oriented=True
    # else:
    #     oriented=False

    oriented=False

    with open(path, 'r',encoding='utf-8') as file:
        for line in file:
            line=line.strip().split()
            res[line[0]]=res.get(line[0],[])+[line[1]]
            if not oriented:
                res[line[1]]=res.get(line[1],[])+[line[0]]
    return res


res = read_csv("C:/Users/HP/Desktop/work/descrete/project/task7_data/task7_data/bipartie/bipartie_100_1246_try3.csv")
# print(res)
print('9', res['9'])
print('85', res['85'])
dif= [item for item in res['9'] if item in res['49']]
print('dif2', [item for item in dif if item in res['85']])
print('49', res['49'])


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


print(bipartite(res))

print("My program took", time.time() - start_time, "to run")

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

# print(bipartite({'1': ['6'], '2': ['3'], '3': ['6', '1'], '4': ['5'], '7': ['4'], '5': ['2', '3']}))
