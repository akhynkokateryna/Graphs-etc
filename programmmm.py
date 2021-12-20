# from copy import copy


# print(odd_degree_nodes({1: [2, 5], 2: [1, 5], 3: [4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}))

'''
	from_dict - return a list of tuples links from a graph G in a 
	dictionary format
'''	
def from_dict(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u,v))
    return links

'''
	fleury(G) - return eulerian trail from graph G or a 
	string 'Not Eulerian Graph' if it's not possible to trail a path
'''
def fleury(G):
    '''
		Пусть задан граф  Начинаем с некоторой вершины
  и каждый раз вычеркиваем пройденное ребро. Не проходим по ребру, 
  если удаление этого ребра приводит к разбиению 
  графа на две связные компоненты (не считая изолированных вершин), 
  т.е. необходимо проверять, является ли ребро мостом или нет.
	'''
 
 
    def odd_degree_nodes(G):
        odd_degree_nodes = []
        for u in G:
            if len(G[u]) % 2 != 0:
                odd_degree_nodes.append(u)
        return odd_degree_nodes
    
    odn = odd_degree_nodes(G)
    if len(odn) != 0:
        return 'Not Eulerian Graph'
    else:
        # g = copy(G)
        trail = []
        u = list(G)[0]
        while len(from_dict(G)) > 0:
            current_vertex = u
            for u in G[current_vertex]:
                G[current_vertex].remove(u)
                G[u].remove(current_vertex)
                bridge = not is_connected(G)
                if bridge:
                    G[current_vertex].append(u)
                    G[u].append(current_vertex)
                else:
                    break
            if bridge:
                G[current_vertex].remove(u)
                G[u].remove(current_vertex)
                G.pop(current_vertex)
            trail.append((current_vertex, u))
    list_of = []
    for item in trail:
        list_of.append(item[0])
    list_of.append(list_of[0])
    return list_of

print(fleury({1: [2, 5], 2: [1, 5], 3: [4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}))
