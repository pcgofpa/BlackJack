import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    for new_card in cards:
        card = random.choice(cards)
        return card

#cards = {
#    "2": 2, 
#    "3": 3, 
#    "4": 4, 
#    "5": 5, 
#    "6": 6, 
#    "7": 7, 
#    "8": 8, 
#    "9": 9, 
#    "10": 10, 
#    "J": 10, 
#    "Q": 10, 
#    "K": 10,
#    "A": 11 or 1
#    }