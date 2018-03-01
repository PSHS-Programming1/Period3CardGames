import random

class Card(object):
    """This creates a playing card"""
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["C","S","H","D"]

    def __init__(self, rank:str, suit:str, isFaceUp = True):
        """creates a card of a given rank and suit"""
        self.rank = rank #defines rank of card
        self.suit = suit #defines suit of card
        self.card = (rank, suit) #creates card as a tuple
        self.isFaceUp = isFaceUp #determines if card can be shown


    def __str__(self):
        """returns the card if it is face up"""
        if self.isFaceUp:
            output = self.rank + "-" + self.suit
            return output
        else:
            return "XX"

    def flipCard(self):
        """changes state of isFaceUp so that card is printed correctly"""
        if self.isFaceUp:
            self.isFaceUp = False
        else:
            self.isFaceUp = True

class Hand(object):
    """Hand of cards"""
    def __init__(self):
        self.cards = [] #list containing card objects

    def __str__(self):
        if len(self.cards) == 0:
            return "<EMPTY>"
        output = ""
        for card in self.cards:
            output += "(" + card.__str__() + ")" + " "
        return output

    def addCard(self, card:Card):
        """Adds a card object to the hand"""
        self.cards.append(card)

    def giveCard(self, card:Card, otherHand):
        """remove a card from this deck to add
        to the otherHand"""
        self.cards.remove(card)
        otherHand.addCard(card)

    def clearCard(self):
        """remove all cards from the hand"""
        self.cards = []

    def getCard(self,rank, suit):
        for card in self.cards:
            if card.suit == suit and card.rank == rank:
                return card
        print("Card is not in hand")
        return None

h = Hand()

h.addCard(Card("9", "S"))
h.addCard(Card("J", "C", False))
h.clearCard()
print(h)














