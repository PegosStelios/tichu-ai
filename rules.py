# Set down the rules for the game

import random
import card as c
import hand as h

bool pair(c, c2):
    # A pair of cards of the same value
    if c[0] == c2[1]:
        return True
    else:
        return False

bool trio(c, c2, c3):
    # A trio of cards of the same value
    if c[0] == c2[1] == c3[2]:
        return True
    else:
        return False

bool bomb(c, c2, c3, c4):
    # A bomb of 4 cards of the same value
    if c[0] == c2[1] == c3[2] == c4[3]:
        return True
    else:
        return False

bool fullHouse(c, c2, c3, c4, c5):
    # A full house of 5 cards, 3 of the same value and 2 of the same value
    if c[0] == c2[1] == c3[2] and c4[3] == c5[4]:
        return True
    else:
        return False

#bool kenta(...):
    # A kenta of cards increasing in value by 1 at a time, it can be any length of cards
    

#bool isMoveLegal(Hand hand, Card card):
    # Check if the card is in the hand
    # A move is legal if its value is greater than the last card played