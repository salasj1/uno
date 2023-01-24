from player import Player
from helpers import clear
import random
from card import Card

class Game:
    def __init__(self, player1: Player, player2: Player, player3: Player, player4: Player):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.previous_card = None
        self.turn = "clockwise" # can be clockwise (1, 2, 3, 4) or counterclockwise (4, 3, 2, 1)
        self.previous_player = 4

    def play(self):

        while not self.check_winning():
            print(len(self.player1.cards))
            print(len(self.player2.cards))
            print(len(self.player3.cards))
            print(len(self.player4.cards))
            next_player = self.get_next_player()
            if next_player == 1:
                self.player1_play()
            elif next_player == 2:
                self.player2_play()
            elif next_player == 3:
                self.player3_play()
            elif next_player == 4:
                self.player4_play()


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

    

    def reverse(self):
        
        if self.turn == "clockwise":
            self.turn = "counterclockwise"
            self.previous_player=self.get_next_player() - 1
        else:
            self.turn = "clockwise"
            self.previous_player=self.get_next_player() + 1
        

    def skip(self):
        # clockwise: 1 -> 3, 2 -> 4, 3 -> 1, 4 -> 2
        # counterclockwise: 1 -> 3, 2 -> 4, 3 -> 1, 4 -> 2
        if self.turn == "clockwise":
            if self.previous_player == 1:
                self.previous_player = 2
            elif self.previous_player == 2:
                self.previous_player = 3
            elif self.previous_player == 3:
                self.previous_player = 4
            elif self.previous_player == 4:
                self.previous_player = 1
        else:
            if self.previous_player == 1:
                self.previous_player = 4
            elif self.previous_player == 2:
                self.previous_player = 1
            elif self.previous_player == 3:
                self.previous_player = 2
            elif self.previous_player == 4:
                self.previous_player = 3

    def get_next_player(self):
        if self.turn == "clockwise":
            if self.previous_player == 4:
                return 1
            else:
                return self.previous_player + 1
        else:
            if self.previous_player == 1:
                return 4
            else:
                return self.previous_player - 1

    def player1_play(self):
        print("Player 1, please make your choice. ")
        self.player1.print_cards()
        self.previous_card = self.player1.prompt_card(self.previous_card, self)
        if self.previous_card.special_ability == "wild" or self.previous_card.special_ability == "+4":
            self.previous_card.color = self.player1.color
        clear()
        self.previous_player=self.get_next_player()

    def player2_play(self):
        print("Player 2, please make your choice. ")
        self.player2.print_cards()
        self.previous_card = self.player2.prompt_card(self.previous_card, self)
        if self.previous_card.special_ability == "wild" or self.previous_card.special_ability == "+4":
            self.previous_card.color = self.player2.color
        clear()
        self.previous_player=self.get_next_player()

    def player3_play(self):
        print("Player 3, please make your choice. ")
        self.player3.print_cards()
        self.previous_card = self.player3.prompt_card(self.previous_card, self)
        if self.previous_card.special_ability == "wild" or self.previous_card.special_ability == "+4":
            self.previous_card.color = self.player3.color
        clear()
        self.previous_player=self.get_next_player()
        

    def player4_play(self):
        print("Player 4, please make your choice. ")
        self.player4.print_cards()
        self.previous_card = self.player4.prompt_card(self.previous_card, self)
        if self.previous_card.special_ability == "wild" or self.previous_card.special_ability == "+4":
            self.previous_card.color = self.player4.color
        clear()
        self.previous_player=self.get_next_player()


    def enviarcartas(self,player:Player,number):
        for n in range(0, number):
            player.cards.append(player.deck[random.randint(0, len(player.deck) - 1)])
        
    def mas2(self):
        if self.previous_player == 4:
            self.enviarcartas(self.player2,2)
        elif self.previous_player == 1:
            self.enviarcartas(self.player3,2)
        elif self.previous_player == 2:
            self.enviarcartas(self.player4,2)
        elif self.previous_player == 3:
            self.enviarcartas(self.player1,2) 
    
    def mas4(self):
        if self.previous_player == 4:
            self.enviarcartas(self.player2,4)
        elif self.previous_player == 1:
            self.enviarcartas(self.player3,4)
        elif self.previous_player == 2:
            self.enviarcartas(self.player4,4)
        elif self.previous_player == 3:
            self.enviarcartas(self.player1,4) 
    
    def wild(self):
        color = int(input("Enter the Color you want to play.\n 1)Red \n 2)Green \n 3)Blue \n 4)Yellow \n"))
        match color:
            case 1: 
                color = "red"
            case 2:
                color = "green"
            case 3:
                color = "blue" 
            case 4:
                color = "yellow"
        return color
