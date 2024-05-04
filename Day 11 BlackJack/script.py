import random
from blackjack_art import logo
import os 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def generate_card():
    return deck[random.randint(0, 11)]


def dealing_cards(hand):

    for i in range(0, 2):
        hand.append(generate_card())

    if sum(hand) == 22:
        hand[1] = 1

    return hand

def hit_card(hand):
    hand.append(generate_card())
    if sum(hand) > 22 and 11 in hand:
        hand[hand.index(11)] = 1
    
    return hand

def check_hand(hand):
    if sum(hand) > 21:
        return [False, 'lose. Went over!']
    elif sum(hand) == 21:
        return [False, 'win. BlackJack!']
    else: 
        return [True]

def showdown():
    if sum(player_hand) > sum(computer_hand):
        return f"You Won! Your Cards: {player_hand} Score: {sum(player_hand)}\nComputer Cards: {computer_hand} Score: {sum(computer_hand)}"
    elif sum(player_hand) < sum(computer_hand):
        return f"You Lose! Your Cards: {player_hand} Score: {sum(player_hand)}\nComputer Cards: {computer_hand} Score: {sum(computer_hand)}"
    else:
        return f"Draw! Your Cards: {player_hand} Score: {sum(player_hand)}\nComputer Cards: {computer_hand} Score: {sum(computer_hand)}"


def hands_check(player, computer):
    if player == 21 and computer != 21:
        return False
        print("You win! BlackJack!")    
    elif computer == 21 and player != 21:
        return False
        print("Computer win! BlackJack!")
    elif player == 21 and computer == 21:
        return False
        print("Draw! Both players have BlackJack!")
    else: 
        return True

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
              

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    cls()
    player_hand = []

    computer_hand = []

    print(logo)


    playing = None


    player_hand = dealing_cards(player_hand)
    computer_hand = dealing_cards(computer_hand)
    playing = hands_check(player_hand, computer_hand)

    player_turn = True
    computer_turn = False

    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}\nComputer's first card: {computer_hand[0]}")

    while player_turn and playing:
        
        design = input("Type 'y' to get another card, type 'n' to pass: ")
        if design == 'y':
            player_hand = hit_card(player_hand)
            print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
            status = check_hand(player_hand)
            if not status[0]:
                print(f"You {status[1]}")
                player_turn = status[0]
                playing = False
        else:
            player_turn = False
            computer_turn = True
        

    while computer_turn and playing:

        if sum(computer_hand) < 11: design = 1
        else: design = random.randint(0,1)
        
        if design == 1:
            computer_hand = hit_card(computer_hand)
            status = check_hand(computer_hand)
            if not status[0]:
                print(f"Computer {status[1]}")
                computer_turn = status[0]
                playing = False
        else:
            computer_turn = False

    if playing:
        print(showdown())



