import random
import higher_lower_art
from game_data import data
import os 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_option():
    r_ndx = random.randint(0, len(data) - 1)
    return data[r_ndx]

def compare_options(option_a, option_b, choice):
    if option_a['follower_count'] > option_b['follower_count'] and choice == 'a': return True
    elif option_a['follower_count'] < option_b['follower_count'] and choice == 'b': return True
    else: return False


option_a = get_option()

is_playing = True

score = 0

while is_playing:
    print(higher_lower_art.logo)
    if score != 0: print(f"You're right! Current score: {score}.")
    option_b = get_option()
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(higher_lower_art.vs)
    print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_playing = compare_options(option_a, option_b, choice)
    if is_playing: score += 1
    option_a = option_b
    cls()

print(f"Sorry, that's wrong. Final score: {score}")