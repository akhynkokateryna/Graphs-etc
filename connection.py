def connection(graph1):
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