import input

def search(stack,graph):
    if len(stack)==len(graph)+1:
        return stack
    if len(stack)==len(graph):
        pos_opt=set(graph[stack[-1]])-set(stack[1:-1])
    else:
        pos_opt=set(graph[stack[-1]])-set(stack[:-1])
    if pos_opt==set():
        return False
    for i in pos_opt:
        result=search(stack+[i],graph)
        if result is not False:
            return result
    return False


def hamiltonian(graph):
    for i in graph:
        stack_start=[i]
        break
    return search(stack_start,graph)
    
    if __name__=='__main__':
    graph=input.read_csv('graph.py')
    print(hamiltonian(graph))
