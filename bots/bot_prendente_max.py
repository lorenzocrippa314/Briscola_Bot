import random

class Bot_Prendente_Max:
    # Ogni volta che può superare la carta giocata con una dello stesso seme, lo fa giocando la carta più alta di quel seme,
    # altrimenti gioca la carta più bassa (briscole incluse)

    def __init__(self):
        pass

    def start_game(self,briscola):
        pass

    def make_move(self,carte,carte_prese,cartagiocata=None):
        if cartagiocata:
            seme=cartagiocata.seme
            carte_giocabili=[]
            for carta in carte:
                if carta.seme==seme and carta.valore()>cartagiocata.valore():
                    carte_giocabili.append(carta)
            if not carte_giocabili==[]:
                massimo=max(carte_giocabili, key=lambda p: p.valore())
                return carte.index(massimo)
        minimo = min(carte, key=lambda p: p.valore())
        return carte.index(minimo)


