
#importa as funções
import cria_baralho
import Extrai_Naipe
import extrai_valor
import lista_movimento_possíveis
import possui_movimentos_possiveis
import empilha_cartas
import random
#começa jogo
jogo = False

jogador = input('Você quer jogar paciencia acordeão? ')
if jogador == 'sim':
    jogo = True
else:
    jogo = False

if jogo == True:
    while jogo:
    

        denovo = input('Quer jogar novamente? ')
        if denovo == 'sim':
            jogo = True 
        else: 
            jogo = False 


               
        
