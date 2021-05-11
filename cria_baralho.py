#função que cria baralho
def cria_baralho():
    v_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cartas_b = []
    for i in range(13):
        cartas_b.append(v_cartas[i] + '♠')
        cartas_b.append(v_cartas[i] + '♥')
        cartas_b.append(v_cartas[i] + '♦')
        cartas_b.append(v_cartas[i] + '♣')
    return cartas_b