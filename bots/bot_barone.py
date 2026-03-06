from carta import Carta

class Bot_Barone():

    def __init__(self):
        pass

    def start_game(self,briscola):
        self.briscola=briscola.seme

    def make_move(self,carte,carteprese,cartagiocata=None):
        carte[0]=Carta('A',self.briscola)
        return 0
