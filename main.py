from cards import cards
from cards import deal_card
from art import logo

print(logo)
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def play_game():
    user_cards = []
    dealer_cards = []
    is_game_over = False
    for u_card in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())    

    def calculate_score(cards): 
        """Calculate hand score"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11) 
            cards.append(1)
        return sum(cards)


    def compare_score(user_score, dealer_score):
        if user_score == dealer_score:
            return "Draw"
        elif dealer_score == 0:
            return "Lose, opponent has BlackJack"
        elif user_score == 0:
            return "Win with BlackJack"
        elif user_score > 21:
            return "You busted. You lose"
        elif dealer_score > 21:
            return "Dealer busted. You Win."
        elif user_score > dealer_score:
            return "You win"
        else: 
            return "Dealer wins."

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score:{user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_again = input(f"Draw another card: 'y' or 'n' ")
            if draw_again == "y":
                user_cards.append(deal_card())                
            else:
                is_game_over = True
            print(f"Your cards: {user_cards}, current score:{user_score}")

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        print(dealer_score)

    print(f"Your hand contained {user_cards} for a score of {user_score}")
    print(f"The dealer's hand {dealer_cards} for a score of {dealer_score}")
    print(compare_score(user_score, dealer_score))

play_game()
while input(f"Would you like to play again? 'y' or 'n'") == "y":
    print("\033c", end='')
    print(logo)
    play_game()