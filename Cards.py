import random

class Card(object):
    """This creates a playing card"""
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["C","S","H","D"]

    def __init__(self, rank:str, suit:str, isFaceUp = True):
        """creates a card of a given rank and suit"""
        self.rank = rank
        self.suit = suit
        self.card = (rank, suit)
        self.isFaceUp = isFaceUp


    def __str__(self):
        if self.isFaceUp:
            output = self.rank + "-" + self.suit
            return output
        else:
            return "XX"

    def flipCard(self):
        if self.isFaceUp:
            self.isFaceUp = False
        else:
            self.isFaceUp = True

c = Card(random.choice(Card.RANKS), random.choice(Card.SUITS), False)
print(c)
c.flipCard()
print(c)