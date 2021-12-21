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
            if line[0] in res:
                res[line[0]]+=[line[1]]
            else:
                res[line[0]]=[line[1]]
            if not oriented:
                if line[1] in res:
                    res[line[1]]+=[line[0]]
                else:
                    res[line[1]]=[line[0]]
            else:
                if line[1] not in res:
                    res[line[1]]=[]
    return res

# if __name__=='__main__':
    # print(read_csv('/mnt/c/Users/user/Downloads/isomorphic_6_16_try1.csv'))
