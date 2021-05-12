
#importa as funções
from cria_baralho import *
from Extrai_Naipe import *
from extrai_valor import *
from lista_movimento_possíveis import *
from possui_movimentos_possiveis import *
from empilha_cartas import *
import random
#começa jogo
jogo = False

jogador = input('Você quer jogar paciencia acordeão? ')
if jogador == 'sim':
    jogo = True
else:
    jogo = False

if jogo == True:
    v_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    while jogo:
        baralho = cria_baralho()
        print('Este é o seu baralho {0}'.format(baralho))

        

    

        denovo = input('Quer jogar novamente? ')
        if denovo == 'sim':
            jogo = True 
        else: 
            jogo = False 




               
        
