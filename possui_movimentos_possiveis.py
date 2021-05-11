# cria função de possiveis movimentos possiveis
def possui_movimentos_possiveis(lista):
    i = 0
    j = lista[i]
    p = lista[i + 1]
    g = 0
    v = 0
    print(len(lista))
    while i < len(lista)-1:
        j = lista[i]
        p = lista[i + 1]
        if j[0] == p[1]:
            return True
        i+=1
    while v < len(lista)-3:
        j = lista[v]
        g = lista[v + 3]
        if j[1] == g[1]:
            return True
        v += 1
    if v >= len(lista)-3:
        return False