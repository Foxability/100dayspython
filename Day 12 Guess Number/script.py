import random

def play_game():

    def set_difficulty():
        if input("Would you like to play on hard mode or easy?\nType 'hard' or 'easy': ") == 'hard': return 5
        else: return 10

    attempts = set_difficulty()

    number = random.randint(1, 100)

    def check_answer(number, answer, attempts):
        if number < answer:
            attempts -= 1
            print("Is too high!")
        elif number > answer:
            attempts -= 1
            print("Is too low!")
        else: 
            print(f"You got it! Guessing number was {answer}")
            attempts = 0
        return attempts

    while attempts != 0:
        print(f"You have {attempts} attempts left...")
        asnwer = int(input("Guess the number: "))
        attempts = check_answer(number, asnwer, attempts)
        if attempts == 0: print("Game is over!")

play_game()