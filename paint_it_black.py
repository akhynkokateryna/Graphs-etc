def create_colour_dict(edges):
    colors = {}
    for edge in edges:
        colors[edge[0]] = 0
        colors[edge[1]] = 0
    return colors

def find_coloring(edges):
    colors = create_colour_dict(edges)
    
    color_options = ('r','g','b')
    
    for edge in edges:
        colors[edge[0]] = 'r'
        colors[edge[1]] = 'g'
        edges.remove(edge)
        break
        # works for tuples,
        # can be changed to edges-{edge} if we work with sets
        
    color_search()
    #if colors[edge[0]] != 0 or colors[edge[1]] != 0:

def color_search(edges,colors):
    for edge in edges:
        if colors[edge[0]] == colors[edge[1]]:
            return None
        if colors[edge[0]] != 0 and colors[edge[1]] == 0:
            
        if colors[edge[0]] != 0 and colors[edge[1]] == 0:
