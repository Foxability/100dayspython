import os
from bind_auction_art import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


is_active = True

print(logo)

auction_dictionary = {}



while is_active:

    name = input("What's your name? \n")
    bid_price = int(input("What's your bid? \n"))

    auction_dictionary[name] = bid_price

    if input("Are there any other bidders? Type 'yes' or 'no':\n").lower() == 'no':
        is_active = False
    cls()

    
    
winner = ""

temp = 0

for key in auction_dictionary:
    if auction_dictionary[key] > temp: 
        temp = auction_dictionary[key]
        winner = key



print(winner, auction_dictionary[winner])