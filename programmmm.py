def from_dict(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u,v))
    return links

def odd_degree_nodes(G):
        for u in G:
            if len(G[u]) % 2 != 0:
                return False
        return True

def fleury(G):
    if not odd_degree_nodes(G):
        return 'Not Eulerian Graph'
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
