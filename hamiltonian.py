import random

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

if __name__=='__main__':
    graph=read_csv('/mnt/c/Users/vovak/Downloads/hamiltonian_20_81_try2.csv')
    for i in graph:
        stack_start=[i]
        break
    print(search(stack_start,graph))