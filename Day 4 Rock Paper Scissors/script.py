import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

print(f"You choice: \n{choices[player_choice]}")

print(f"Computer choice: \n{choices[computer_choice]}")
print

if player_choice == computer_choice:
    print("Draw!")

elif player_choice == 0 and computer_choice == 2 or player_choice == 1 and computer_choice == 0 or player_choice == 2 and computer_choice == 1:
    print("You Win")
else:
    print("You Lose!")