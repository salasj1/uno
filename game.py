from player import Player

class Game:
    def __init__(self, player1: Player, player2, player3, player4):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.previous_card = None

    def play(self):
        self.player1.print_cards()
        print("Game started!")
        self.player1.prompt_card(self.previous_card)
        self.player1.print_cards()
