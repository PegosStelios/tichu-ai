# import card.py
import card as c

class Hand:
    def __init__(self, n):
        self.cards = []
        self.label = n
    def add_card(self, card):
        self.cards.append(card)
    def __str__(self):
        return f'{self.label}: {self.cards}'
    def __repr__(self):
        return f'{self.label}: {self.cards}'
    def __eq__(self, other):
        return self.cards == other.cards
    def __hash__(self):
        return hash((self.label, self.cards))
    def __lt__(self, other):
        return self.cards < other.cards
    def __gt__(self, other):
        return self.cards > other.cards
    def __le__(self, other):
        return self.cards <= other.cards
    def __ge__(self, other):
        return self.cards >= other.cards
    def __ne__(self, other):
        return self.cards != other.cards