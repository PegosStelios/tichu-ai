import card as c
import hand as h


# Generate all possible cards, if any future cards are not in this list, they are not possible and an error will be thrown
c.allPossibleCombinations()
print(c.possibleCards)

# How many cards are there?
print(len(c.possibleCards))
player1 = h.Hand('Player 1')

player1.add_card(c.Card('Spades', 'A'))

print(player1)

# TODO: Make full hand generation 