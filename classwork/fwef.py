import random

class Card(object):
    def __init__(self,suit,name,value):
        self.suit = suit
        self.name = name
        self.value = value
        
    def __str__(self):
        return "{} of {} (value = {})".format(self.name, self.suit, self.value)

class Deck(object):
    def __init__(self):
        suits = ['Clubs','Hearts','Diamonds','Spades']
        names = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.cards = []
        for suit in suits:
            for index in range(len(names)):
                c = Card(suit,names[index],values[index])
                self.cards.append(c)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card
                
d = Deck()
d.shuffle()
player_hand = [d.deal(),d.deal()]

for card in player_hand:
  print(card)
choice = input("Hit or stand?")

while choice != "stand":
  player_hand.append(d.deal())
  for card in player_hand:
    print(card)
  choice = input("Hit or stand?")