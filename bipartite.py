"bipartite.py"

import time
start_time = time.time()

def read_csv(path):
    res={}

    oriented=input('Your graph is oriented?(y/n)')
    while oriented not in ['y','n']:
        oriented=input('Incorrect input. Your graph is oriented?(y/n)')
    if oriented=='y':
        oriented=True
    else:
        oriented=False

    with open(path, 'r',encoding='utf-8') as file:
        for line in file:
            line=line.strip().split()
            res[line[0]]=res.get(line[0],[])+[line[1]]
            if not oriented:
                res[line[1]]=res.get(line[1],[])+[line[0]]
    return res


res = read_csv("C:/Users/HP/Desktop/work/descrete/project/task7_data/task7_data/bipartie/bipartie_5000_3126273_try3.csv")


def two_parts(vert_dict):
    "Divides all vertices into to parts"
    red = []
    blue = []
    vertices = list(vert_dict.keys())
    red += vertices[0]
    for vertice in vert_dict:
        if vertice in red:
            for item in vert_dict[vertice]:
                if item not in red:
                    blue += vert_dict[vertice]
                else:
                    return 'Graph is not Bipartite'
        else:
            for item in vert_dict[vertice]:
                if item not in blue:
                    red += vert_dict[vertice]
                else:
                    return 'Graph is not Bipartite'
    return 'Graph is Bipartite'

print(two_parts(res))

print("My program took", time.time() - start_time, "to run")
