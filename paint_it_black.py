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
        file.readline()
        for line in file:
            line=line.split(',')
            res[line[0]]=res.get(line[0],[])+[line[1]]
    return res

def create_colour_dict(edges):
    colors = {}
    for edge in edges:
        colors[edge[0]] = 0
        colors[edge[1]] = 0
    return colors

def find_coloring(edges):
    colors = create_colour_dict(edges)


    for edge in edges:
        colors[edge[0]] = 'r'
        colors[edge[1]] = 'g'
        edges.remove(edge)
        break
        # works for lists,
        # can be changed to edges-{edge} if we work with sets


    result=color_search(edges,colors)
    if result != None:
        print('Here is the solution:')
        for i in sorted(result.items()):
            print(f'{i[0]} - {i[1]}')
        return result
    print("There is no solution.")

def color_search(edges,colors):
    color_options = ['r','g','b']
    game_is_completed=True

    for edge in edges:
        if colors[edge[0]] == colors[edge[1]] and colors[edge[1]] in ['r','g','b']:
            return None
        if colors[edge[0]] == 0 or colors[edge[1]] == 0:
            game_is_completed = False

    if game_is_completed:
        return colors

    for edge in edges:
        if colors[edge[0]] != 0 and colors[edge[1]] == 0:
            color_options.remove(colors[edge[0]])

            colors[edge[1]] = color_options[0]
            result1 = color_search(edges,colors)
            if result1 != None:
                return result1
            
            colors[edge[1]] = color_options[1]
            result2 = color_search(edges,colors)
            if result2 != None:
                return result2

            break

        if colors[edge[0]] == 0 and colors[edge[1]] != 0:
            color_options.remove(colors[edge[1]])

            colors[edge[0]] = color_options[0]
            result1 = color_search(edges,colors)
            if result1 != None:
                return result1

            colors[edge[0]] = color_options[1]
            result2 = color_search(edges,colors)
            if result2 != None:
                return result2

            break

if __name__=="__main__":
    graph=[(i,i+1) for i in range (990)]+[(i,i-2) for i in range (2,990)]
    # print(graph)
    find_coloring(graph)
