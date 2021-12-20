import connection
import itertools
    
def izomorph(graph1,graph2):
    graph1={i:set(k) for i,k in graph1.items()}
    graph2={i:set(k) for i,k in graph2.items()}
    if not connection.connection(graph1) or not connection.connection(graph2):
        print('Wrong type of graph')
        return False

    if len(graph1)!=len(graph2):
        return False
    
    graphch1=graph1.copy()
    graphch2=graph2.copy()
    for i in list(graphch1):
        for j in list(graphch2):
            if i in graphch1 and j in graphch2:
                if len(graphch1[i])==len(graphch2[j]):
                    del graphch1[i]
                    del graphch2[j]
    if graphch1!={} or graphch2!={}:
        return False

    graph_lst1=tuple(graph1)
    graph_lst2=list(graph2)
    for i in itertools.permutations(graph_lst2):
        dct1={i[k1]:graph_lst1[k1] for k1 in range(len(graph1))}
        option={dct1[k]: set([dct1[j] for j in graph2[k]]) for k in graph_lst2}
        if graph1==option:
            return True
    return False

    

if __name__=='__main__':
    import input
    graph1=input.read_csv('/mnt/c/Users/user/Downloads/samoper_1.csv')
    graph2=input.read_csv('/mnt/c/Users/user/Downloads/samoper_2.csv')
    print(izomorph(graph1,graph2))
