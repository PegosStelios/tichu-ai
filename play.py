        
import card as c
import hand as h
import rules as r

class Game:
    def __init__(self):
        self.player1 = h.Hand('Player 1')
        self.player2 = h.Hand('Player 2')
        self.player3 = h.Hand('Player 3')
        self.player4 = h.Hand('Player 4')
        self.players = [self.player1, self.player2, self.player3, self.player4]

    def play(self):
        # Generate all possible cards, if any future cards are not in this list, they are not possible and an error will be thrown
        c.allPossibleCombinations()

        # How many cards are there?
        print(len(c.possibleCards))

        # Make full hand generation
        self.player1.generateHand()
        self.player2.generateHand()
        self.player3.generateHand()
        self.player4.generateHand()

        # Print the hands
        print(self.player1)
        print(self.player2)
        print(self.player3)
        print(self.player4)

    def playRound(self):
        # A player must always follow the rules of the game
        # The first player to play must play the majong
        r.Rules().gameRules['isMoveLegal'](self.player1.hand[0], self.player1.hand[0])
        
    def playGame(self):
        # Play the game
        self.play()
        # Play a round
        self.playRound()

# Test run
game = Game()
game.playGame()
