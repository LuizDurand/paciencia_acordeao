# função para extrair o naipe da carta
def extrai_valor(cartas_b):
    if cartas_b == 'A♦' or cartas_b == 'A♣' or cartas_b == 'A♥' or cartas_b == 'A♠':
        return 'A'
    if cartas_b == '2♦' or cartas_b == '2♣' or cartas_b == '2♥' or cartas_b == '2♠':
        return '2'
    if cartas_b == '3♦' or cartas_b == '3♣' or cartas_b == '3♥' or cartas_b == '3♠':
        return '3'
    if cartas_b == '4♦' or cartas_b == '4♣' or cartas_b == '4♥' or cartas_b == '4♠':
        return '4'
    if cartas_b == '5♦' or cartas_b == '5♣' or cartas_b == '5♥' or cartas_b == '5♠':
        return '5'
    if cartas_b == '6♦' or cartas_b == '6♣' or cartas_b == '6♥' or cartas_b == '6♠':
        return '6'
    if cartas_b == '7♦' or cartas_b == '7♣' or cartas_b == '7♥' or cartas_b == '7♠':
        return '7'
    if cartas_b == '8♦' or cartas_b == '8♣' or cartas_b == '8♥' or cartas_b == '8♠':
        return '8'
    if cartas_b == '9♦' or cartas_b == '9♣' or cartas_b == '9♥' or cartas_b == '9♠':
        return '9'
    if cartas_b == '10♦' or cartas_b == '10♣' or cartas_b == '10♥' or cartas_b == '10♠':
        return '10'
    if cartas_b == 'J♦' or cartas_b == 'J♣' or cartas_b == 'J♥' or cartas_b == 'J♠':
        return 'J'
    if cartas_b == 'Q♦' or cartas_b == 'Q♣' or cartas_b == 'Q♥' or cartas_b == 'Q♠':
        return 'Q'
    if cartas_b == 'K♦' or cartas_b == 'K♣' or cartas_b == 'K♥' or cartas_b == 'K♠':
        return 'K'