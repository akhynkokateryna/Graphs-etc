def connection(graph1):
    graph=graph1.copy()
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