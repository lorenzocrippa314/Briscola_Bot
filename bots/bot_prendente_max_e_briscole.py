import random

class Bot_Prendente_Max_E_Briscole:
    # Ogni volta che può superare la carta giocata con una dello stesso seme, lo fa giocando la carta più alta di quel seme,
    # altrimenti gioca la carta più bassa (briscole escluse, a meno di mettere carichi), inoltre taglia i carichi con la briscola più bassa che ha,


    def __init__(self):
        pass

    def seme_presente(self,carte,seme):
        if seme in [carta.seme for carta in carte]:
            return True
        else:
            return False

    def carte_per_seme(self,carte,seme):
        bruls=[]
        for carta in carte:
            if carta.seme==seme:
                bruls.append(carta)
        return bruls

    def start_game(self,briscola):
        self.briscola=briscola

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
            else:
                if cartagiocata.valore()>=9:
                    if self.seme_presente(carte,self.briscola.seme):
                        carte_giocabili=self.carte_per_seme(carte,self.briscola.seme)
                        minimo=min(carte_giocabili, key=lambda p: p.valore())
                        return carte.index(minimo)
        carte_giocabili=[carta for carta in carte if carta.seme!=self.briscola.seme]
        if carte_giocabili==[] or min([carta.valore() for carta in carte_giocabili])>=9:
            carte_giocabili=carte
        minimo = min(carte_giocabili, key=lambda p: p.valore())
        return carte.index(minimo)
