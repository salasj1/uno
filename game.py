from player import Player
from helpers import clear, create_all_cards
import random

class Game:
    def __init__(self, player1: Player, player2: Player, player3: Player, player4: Player):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.previous_card = None

    def play(self):

        while not self.check_winning():
            print("Player 1, please make your choice. ")
            self.player1.print_cards()
            self.previous_card = self.player1.prompt_card(self.previous_card)

            clear()
            print("Player 2, please make your choice. ")
            self.player2.print_cards()
            self.previous_card = self.player2.prompt_card(self.previous_card)

            clear()
            print("Player 3, please make your choice. ")
            self.player3.print_cards()
            self.previous_card = self.player3.prompt_card(self.previous_card)

            clear()
            print("Player 4, please make your choice. ")
            self.player4.print_cards()
            self.previous_card = self.player4.prompt_card(self.previous_card)

    def check_winning(self):
        if len(self.player1.cards) == 0:
            print("Player 1 wins!")
            return True
        elif len(self.player2.cards) == 0:
            print("Player 2 wins!")
            return True
        elif len(self.player3.cards) == 0:
            print("Player 3 wins!")
            return True
        elif len(self.player4.cards) == 0:
            print("Player 4 wins!")
            return True
        else:
            return False


