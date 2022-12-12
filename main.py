import card as c
import hand as h


# Generate all possible cards, if any future cards are not in this list, they are not possible and an error will be thrown
c.allPossibleCombinations()

# How many cards are there?
print(len(c.possibleCards))
player1 = h.Hand('Player 1')

# Make full hand generation 
player1.generateHand()
print(player1)

