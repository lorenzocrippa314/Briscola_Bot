from random import *
from carta import Carta

PUNTI_DICT={
            '2':0,
            '4':0,
            '5':0,
            '6':0,
            '7':0,
            'J':2,
            'Q':3,
            'K':4,
            '3':10,
            'A':11
        }

class Game:
    def __init__(self,giocatore_1,giocatore_2,chi_inizia=0,mazzo=None):
        self.giocatore_1=giocatore_1
        self.giocatore_2=giocatore_2
        self.giocatori=[self.giocatore_1,self.giocatore_2]
        if not mazzo==None:
            self.mazzo=mazzo
        else:
            self.mazzo=[Carta(i,i//10) for i in range(40)]
            shuffle(self.mazzo)
        self.briscola=self.mazzo[-1]
        self.a_chi_tocca=chi_inizia
        self.carte_prese_1=[]
        self.carte_prese_2=[]
        self.carte_prese=[self.carte_prese_1,self.carte_prese_2]
        self.carte_giocatore_1=[]
        self.carte_giocatore_2=[]
        self.carte_giocatori=[self.carte_giocatore_1,self.carte_giocatore_2]
        self.punteggi=[0,0]
        self.vincitore=None

    def draw(self):
        # Decurta il mazzo della prima carta e la restituisce
        return self.mazzo.pop(0)

    def who_takes(self,carte):
        # Prende le due carte in una lista dove la prima carta è la prima carta giocata,
        # Restituisce l'indice della carta che prende
        seme_che_comanda = carte[0].seme
        if (carte[1].seme == seme_che_comanda and carte[1].valore() > carte[0].valore()) or (
                carte[1].seme == self.briscola.seme and carte[0].seme != self.briscola.seme):
            return 1
        else:
            return 0

    def start(self):
        # Distribuisce le prime 3 carte a testa, cominciando da quello giusto
        # Chiama le funzioni start_game da entrambi i giocatori
        for i in range(3):
            self.carte_giocatore_1.append(self.draw())
            self.carte_giocatore_2.append(self.draw())
        try:
            self.giocatore_1.start_game(self.briscola)
        except:
            pass
        try:
            self.giocatore_2.start_game(self.briscola)
        except:
            pass

    def get_played_cards(self):
        # Restituisce le due carte giocate chiedendole ai bot, in ordine di quale è stata giocata prima
        carta_che_comanda=self.carte_giocatori[self.a_chi_tocca][self.giocatori[self.a_chi_tocca].make_move(self.carte_giocatori[self.a_chi_tocca],self.carte_prese)%len(self.carte_giocatori[self.a_chi_tocca])]
        altra_carta=self.carte_giocatori[not self.a_chi_tocca][self.giocatori[not self.a_chi_tocca].make_move(self.carte_giocatori[not self.a_chi_tocca],self.carte_prese,carta_che_comanda)%len(self.carte_giocatori[not self.a_chi_tocca])]
        return [carta_che_comanda,altra_carta]

    def play_one_hand(self):
        # Capisce quali carte sono state giocate dai bot e quale ha vinto, le toglie dalle carte in mano e le mette nel mazzetto di chi ha preso
        # Distribuisce un'altra carta a testa se il mazzo non è ancora finito
        carte=self.get_played_cards()
        chi_prende=bool(self.a_chi_tocca-self.who_takes(carte))
        self.carte_prese[chi_prende].extend(carte)
        self.carte_giocatori[self.a_chi_tocca].remove(carte[0])
        self.carte_giocatori[not self.a_chi_tocca].remove(carte[1])
        self.a_chi_tocca=chi_prende
        if not self.mazzo==[]:
            self.carte_giocatori[self.a_chi_tocca].append(self.draw())
            self.carte_giocatori[not self.a_chi_tocca].append(self.draw())
        return 0

    def play_whole_game(self,debug=False):
        # Gioca una partita intera, dopo l'esecuzione entrambi i giocatori avranno 0 carte in mano, il mazzo sarà vuoto,
        # e i mazzetti dei due giocatori saranno pieni
        if debug:
            i=0
            print(self.briscola)
        while not self.carte_giocatori==[[],[]]:
            if debug:
                i+=1
                print(f"mano {i}")
                print(self.carte_giocatori)
            self.play_one_hand()
            if debug:
                print(self.carte_prese)

    def get_score(self,carte):
        score=0
        for x in carte:
            score+=PUNTI_DICT[x.numero]
        return score

    def end_game(self):
        self.punteggi[0]=self.get_score(self.carte_prese[0])
        self.punteggi[1]=self.get_score(self.carte_prese[1])
        if self.punteggi[0]>self.punteggi[1]:
            self.vincitore=1
        elif self.punteggi[0]<self.punteggi[1]:
            self.vincitore=2
        else:
            self.vincitore=0
