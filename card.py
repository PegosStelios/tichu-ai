# Path: main.py

import random as random

totalCards = 0
existingCards = {}
existingSpecialCards = {}
possibleCards = []

suits = [
    'Hearts', 
    'Diamonds', 
    'Clubs', 
    'Spades'
]

special = [
    'Mahjong',
    'Dragon',
    'Phoenix',
    'Dogs',
    'unknown'
]

powerValues = {
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 5,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': 0,
    'J': 0,
    'Q': 0,
    'K': 10,
    'A': 0,
    'Mahjong': 0,
    'Dragon': 25,
    'Phoenix': -25,
    'Dogs': 0,
    'unknown': 0,
}

cardValues = {  
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
    'Mahjong': 1,
    'Dragon': 15,
    'Phoenix': 0.5,
    'Dogs': 0,
    'unknown': None
}

# add all possible cards to possibleCards dict
def allPossibleCombinations():
    for suit in suits:
        for card in cardValues:
            # TODO: Find a better way to do this
            if card != 'unknown' and card != 'Mahjong' and card != 'Dragon' and card != 'Phoenix' and card != 'Dogs':
                possibleCards.append([suit, card])
    for specialCard in special:
        possibleCards.append(["Special", specialCard])
    if len(possibleCards) > 57:
        RaiseError("Too many cards generated")
class Card:
    suit = None
    value = None
    special = None
    power = None
    point = None

    def __init__(self, suit, value):
        if self.isValidValue(value):
            self.value = value
            self.point = cardValues[value]
            self.power = powerValues[value]
        else:
            raise ValueError('Invalid value')

        if self.isValidSuit(suit):
            self.suit = suit
            if (suit, value) in existingCards:
                raise ValueError('Card already exists')
            else:
                existingCards[(suit, value)] = self
        else:
            raise ValueError('Invalid suit')

    def __add__(self, other):
        return self.point + other.point

    def __str__(self):
        return f'{self.suit} {self.value}'

    def __repr__(self):
        return f'{self.suit} {self.value}'

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value
    
    def __hash__(self):
        return hash((self.suit, self.value))

    def __lt__(self, other):
        return self.point < other.point

    def __gt__(self, other):
        return self.point > other.point
    
    def __le__(self, other):
        return self.point <= other.point
    
    def __ge__(self, other):
        return self.point >= other.point

    def __ne__(self, other):
        return self.suit != other.suit or self.value != other.value

    # Only 1 of each suit can exist and up to 4 in total
    def generateRandomCard(self):
        if self.value not in existingCards:
            existingCards[self.value] = self
        else:
            raise ValueError('Card already exists')
        
    def isValidValue(self, value):
        return value in cardValues

    def isValidSuit(self, suit):
        return suit in suits

    def isValidSpecial(self, special):
        return special in special
    
    def isSpecial(self):
        return self.special

    def getPower(self):
        return self.power
    
    def getPoint(self):
        return self.point

    def getCard(self):
        return self.value, self.suit, self.special, self.power, self.point

    def dumpCards(self):
        print(existingCards)
class specialCard:
    value = None
    special = None
    power = None
    point = None

    def __init__(self, value):
        if self.isValidSpecial(value):
            self.special = True
            self.value = value
            self.point = cardValues[value]
            self.power = powerValues[value]

            # Add the card to the existing special cards, if it already exists then raise an error
            if self.value not in existingSpecialCards:
                existingSpecialCards[self.value] = self
            else:
                raise ValueError('Card already exists')

        else:
            raise ValueError('Invalid value')
    def __str__(self):
        return f'{self.value}'
    def isValidSpecial(self, special):
        return special in special
    def generateRandomSpecial(self):
        if self.value not in existingSpecialCards:
            existingSpecialCards[self.value] = self
        else:
            raise ValueError('Special Card already exists')
