from carta import Carta
from random import *
from game import Game
from bots.random_bot import Random_Bot
from bots.bot_prendente_min import Bot_Prendente_Min
from bots.bot_prendente_max import Bot_Prendente_Max
from bots.bot_prendente_max_e_briscole import Bot_Prendente_Max_E_Briscole
from bots.bot_barone import Bot_Barone

n=1000
x=Random_Bot()
y=Bot_Prendente_Max()

winner=[0,0,0]
topscore_1=0
topscore_2=0
for i in range(n):
    game = Game(x,y,randint(0,1))
    game.start()
    game.play_whole_game()
    game.end_game()
    winner[game.vincitore]+=1
    if game.punteggi[0]>topscore_1:
        topscore_1=game.punteggi[0]
    if game.punteggi[1]>topscore_2:
        topscore_2=game.punteggi[1]
print(winner)
print(topscore_1)
print(topscore_2)