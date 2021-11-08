from card import Card

def create_all_cards():
    deck = []
    for _ in range(4):
        for color in ["red", "green", "blue", "yellow"]:
            for number in range(1, 10):
                deck.append(Card(color, number, None))
            for special_ability in ["skip", "reverse", "+2"]:
                deck.append(Card(color, special_ability=special_ability))

    deck.append(Card(special_ability="+4"))
    deck.append(Card(special_ability="+4"))
    deck.append(Card(special_ability="everything"))
    deck.append(Card(special_ability="everything"))

    return deck

