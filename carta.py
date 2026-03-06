from random import choice

NUMERI=['2','4','5','6','7','J','Q','K','3','A']
SEMI=['H','S','D','C']
SEMI_DICT={
    'H':'♥',
    'S':'♠',
    'D':'♦',
    'C':'♣'
}

class Carta:

    def __init__(self,numero=None,seme=None,*args):
        # Se si mettono dentro meno di 2 input, genera una carta a caso.
        # Se si mettono almeno 2 input contano solo i primi 2. Il primo è il numero e il secondo il seme.
        # Se sono stringhe presenti in NUMERI e SEMI vengono assegnati; se sono interi n e m viene assegnato come numero
        # NUMERI[n % len(NUMERI)] e come seme SEMI[m % len(SEMI)];
        # altrimenti assegna numero 'A' e seme 'H'.
        self.numero=NUMERI[-1]
        self.seme=SEMI[0]
        if numero is not None and seme is not None:
            if isinstance(numero,str):
                if numero in NUMERI:
                    self.numero=numero
            elif isinstance(numero, int):
                self.numero=NUMERI[numero % len(NUMERI)]
            if isinstance(seme, str):
                if seme in SEMI:
                    self.seme = seme
            elif isinstance(seme, int):
                self.seme = SEMI[seme % len(SEMI)]
        else:
            self.numero = choice(NUMERI)
            self.seme = choice(SEMI)

    def print(self):
        print(self.numero+SEMI_DICT[self.seme])

    def __str__(self):
        return self.numero+SEMI_DICT[self.seme]

    def __repr__(self):
        return self.numero+SEMI_DICT[self.seme]

    def valore(self):
        # Va da 1 a 10
        return NUMERI.index(self.numero)+1

