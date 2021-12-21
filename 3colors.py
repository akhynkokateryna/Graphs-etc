import input

def search(graph,coloring):
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

def find_coloring(graph,oriented=False):
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

if __name__=="__main__":
    # graph=input.read_csv('/mnt/c/Users/user/Downloads/colour_tes.csv')
    # result = find_coloring(graph)
    # if result:
    #     for i in sorted(result):
    #         print(f'{i[0]} - {i[1]}')
