#Função que empilha as cartas
def empilha(li, topo, fim):
    i = li[topo]
    li.remove(li[topo])
    li.remove(li[fim])
    li.insert(fim, i)
    return li