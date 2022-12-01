
import random

#currentdeck = []
#pastcards = []
#playerhand = []
#dealerhand = []
#playerhandvalue = 0
#dealerhandvalue = 0
#playerhandaces = 0
#dealerhandaces = 0
#playermoney = 100
#bet = 0

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + " of " + self.suit

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            print(c)

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
