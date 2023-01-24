from card import Card
from subprocess import call
import os

def create_all_cards():
    deck = []
    for color in ["red", "green", "blue", "yellow"]:
        for number in range(1, 10):
            deck.append(Card(color, number, None))
        for special_ability in ["reverse", "skip", "+2",]: # , "reverse", "+2", "wild", "wild+4"
            deck.append(Card(color, special_ability=special_ability))
    
    for n in range(0,4):
            deck.append(Card("white",special_ability="wild"))
            deck.append(Card("white",special_ability="+4"))
    
    return deck

def clear():
    os.system('cls') 

