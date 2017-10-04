#Taylor Scafe
#CSIT/Python Files/Homework 9 - Deck
#11/21/2014
#Class that creats a deck of cards

import random

class Card:
    def __init__(self,value):
        self.value = value
        self.name = ""
        
    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value


    def getName(self):
        return self.name

    
    def setName(self,name):
        self.name = name





class Deck:

    
    def __init__(self):
        self.deck = []

    def add(self, card):
        self.deck.append(card)

    def remove(self, card):
        self.deck.remove()

    def buildDeck(self):
        for x in range(4):
            for i in range(13):
                self.add(Card(i+1))


    def getDeck(self):
        return self.deck

    def draw(self):
        x = random.randint(0,len(self.deck)-1)
        card = self.deck.pop(x)
        return card

    def shuffle(self):
        for i in range(100):
            j = random.randint(0,(len(self.deck)-1))
            x = self.deck[j]
            self.deck.remove(x)
            self.deck.append(x)

    def setName(self):
        for card in self.deck:
            if card.getValue() == 1:
                card.setName("Ace")
                card.setValue(11)
            elif card.getValue() >1 and card.getValue() <11:
                card.setName(str(card.getValue()))
            elif card.getValue() == 11:
                card.setName("Jack")
                card.setValue(10)
            elif card.getValue() == 12:
                card.setName("Queen")
                card.setValue(10)
            elif card.getValue() == 13:
                card.setName("King")
                card.setValue(10)



