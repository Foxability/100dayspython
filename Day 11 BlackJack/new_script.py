import random
from blackjack_art import logo
import os 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_random_card():
    return random.choice(deck)

def dealing_cards(hand):
    player_name = list(hand.keys())[0]
    if len(hand[player_name]) == 0:
        for _ in range(0, 2):
            hand[player_name].append(get_random_card())
        if sum(hand[player_name]) == 22: hand[player_name][1] = 1
        elif sum(hand[player_name]) == 21:
            reason = "win got blackjack!"
            is_over_reason(hand, reason)
    else:
        hand[player_name].append(get_random_card())
        if sum(hand[player_name]) > 21 and 11 in hand[player_name]:
             hand[player_name][hand[player_name].index(11)] = 1
             if player_name == "Player": print({"You drew an Ace, but your total score exceeded 21. The Ace is counted as 1 to prevent busting."})

        print(f"Your cards: {player_hand[list(player_hand.keys())[0]]}, current score: {sum(player_hand[list(player_hand.keys())[0]])} \nDealer's first card: {dealer_hand[list(dealer_hand.keys())[0]][0]}")
        
        if sum(hand[player_name]) > 21:
            reason = "lose hand went over."
            is_over_reason(hand, reason)
        elif sum(hand[player_name]) == 21:
            reason = "win got blackjack."
            is_over_reason(hand, reason)
            
def is_over_reason(hand, reason):
    global is_game_over
    is_game_over = True
    if hand == None: player_name = ""
    else: player_name = list(hand.keys())[0]
    print(f"{player_name} {reason}\nPlayer's hand: {player_hand[list(player_hand.keys())[0]]}.\nDealer's hand: {dealer_hand[list(dealer_hand.keys())[0]]}")

def compare_hands(player_hand, dealer_hand):
    if sum(player_hand[list(player_hand.keys())[0]]) > sum(dealer_hand[list(dealer_hand.keys())[0]]):
        reason = "win highest score."
        is_over_reason(player_hand, reason)
    elif sum(player_hand[list(player_hand.keys())[0]]) < sum(dealer_hand[list(dealer_hand.keys())[0]]):
        reason = "win highest score."
        is_over_reason(dealer_hand, reason)
    else:
        reason = 'Draw.'
        is_over_reason(None, reason)

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Would you like to play BlackJack? Y/N: ").lower() == 'y':
    is_game_over = False

    player_hand = {"Player": []}
    dealer_hand = {"Dealer": []}

    cls()
    print(logo)
    dealing_cards(player_hand)
    dealing_cards(dealer_hand)
    print(f"Your cards: {player_hand[list(player_hand.keys())[0]]}, current score: {sum(player_hand[list(player_hand.keys())[0]])} \nDealer's first card: {dealer_hand[list(dealer_hand.keys())[0]][0]}")

    while not is_game_over and input("Hit another card? Y/N: ").lower() == 'y':
        dealing_cards(player_hand)
    
    while not is_game_over and sum(dealer_hand[list(dealer_hand.keys())[0]]) < 17:
        dealing_cards(dealer_hand)

    while not is_game_over: compare_hands(player_hand, dealer_hand)