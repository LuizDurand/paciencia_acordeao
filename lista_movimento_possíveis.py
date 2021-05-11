#Cria função de movimentos possíveis
def lista_movimentos_possiveis (cartas_b, ip):
    numero_carta_b = []
    naipe_carta_b = []
    for carta in cartas_b:
        if len(carta) == 2:
            numero_carta_b.append (carta [0])
            naipe_carta_b.append (carta [1])
        else:
            numero_carta_b.append (10)
            naipe_carta_b.append (carta [2])
    movimentos = []
    if ip == 0:
        return []
    elif ip >= 3:
            if naipe_carta_b [ip] == naipe_carta_b [ip - 3]:
                movimentos.append (3)
            if numero_carta_b [ip] == numero_carta_b [ip -3]:
                movimentos.append (3)
            if numero_carta_b [ip] == numero_carta_b [ip - 1]:
                movimentos.append (1)
            if naipe_carta_b[ip] == naipe_carta_b [ip - 1 ] :
                movimentos.append (1)
    else:
        if numero_carta_b [ip] == numero_carta_b [ip - 1]:
            movimentos.append (1)
        if naipe_carta_b[ip] == naipe_carta_b [ip - 1 ] :
            movimentos.append (1)
    return movimentos