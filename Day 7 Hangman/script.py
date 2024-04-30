import random
import hangman_art
import hangman_words
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Now, to clear the screen

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

display = ["_" for _ in range(len(chosen_word))]

life_score = -6

is_active = True

print(f"{" ".join(display)}\n")

while is_active:

    guess = input("Guess a letter: ").lower()

    if guess not in display and guess in chosen_word:

        if guess in chosen_word:

            for position in range(len(chosen_word)):

                if chosen_word[position] == guess:

                    display[position] = guess

    elif guess in display:
        print(f"You already guessed {guess}\n")


    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        print(hangman_art.stages[life_score])
        life_score += 1

    print(f"{" ".join(display)}\n")

    if "_" not in display:
        is_active = False
        print("You win!")
    
    if life_score == 0:
        print("You lose!")
        is_active = False