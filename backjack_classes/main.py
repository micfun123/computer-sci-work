
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
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for c in self.cards:
            print(c)
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class player(object):
    def __init__(self,player_money,deck) -> None:
        self.hand = []
        self.total_count = 0
        self.money = int(player_money)
        self.deck = deck
        for i in range(2):
            self.add_card(self.deck)
        self.show_hand()
            
    def add_card(self,deck):
        self.hand.append(deck.drawCard())
        self.show_hand()

        

        
            

    def show_hand(self):
        print("\n ===============================")
        for card in self.hand:
            print(card)
        print("\n ===============================")

newdeck = Deck()
newdeck.show()
newdeck.shuffle()
newdeck.show()

michael = player(1000000000000,newdeck)
gwyneth = player(2,newdeck)


