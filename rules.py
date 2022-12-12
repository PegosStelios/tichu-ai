# Set down the rules for the game

import random
import card as c
import hand as h


class Rules:
    def __init__(self):
        self.gameRules = {
            'pair': self.pair,
            'trio': self.trio,
            'bomb': self.bomb,
            'fullHouse': self.fullHouse,
            'kenta': self.kenta,
            'isMoveLegal': self.isMoveLegal,
        }

    def pair(self, c, c2):
        # A pair of cards of the same value
        if c[0] == c2[1]:
            return True
        else:
            return False

    def trio(self, c, c2, c3):
        # A trio of cards of the same value
        if c[0] == c2[1] == c3[2]:
            return True
        else:
            return False

    def bomb(self, c, c2, c3, c4):
        # A bomb of 4 cards of the same value
        if c[0] == c2[1] == c3[2] == c4[3]:
            return True
        else:
            return False

    def fullHouse(self, c, c2, c3, c4, c5):
        # A full house of 5 cards, 3 of the same value and 2 of the same value
        if c[0] == c2[1] == c3[2] and c4[3] == c5[4]:
            return True
        else:
            return False

    def kenta(self, *cards):
        # A kenta of cards increasing in value by 1 at a time, it can be any length of cards
        # Sort the cards by value
        cards = sorted(cards, key=lambda x: x[0])
        # Check if the cards are in order
        for i in range(len(cards) - 1):
            if cards[i][0] + 1 != cards[i + 1][0]:
                return False
        else:
            return True
        
    def isMoveLegal(self, card, lastCard):
    # Check if the card is in the hand
        # A move is legal if its value is greater than the last card played
        if card[0] > lastCard[0]:
            return True
        else:
            return False