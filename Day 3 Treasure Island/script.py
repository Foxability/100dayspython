
print("Welcome to Treasure Island.Your mission is to find the treasure.")
print("""
      _                                                       _
     / \                                                     / \
     )_(                                                     )_(
      |            _________________________________________  |
      |      _____|.-----..-----..-----..-----..----..-----.] |      
      |     /.--.|||;;;;;||;;;;;||;;;;;||;;;;;||;;;;||;;;;;|| |
      |    //   ||||;;;;;||;;;;;||;;;;;||;;;;;||;;;;||;;;;;|| |
  ___...--'|`---'|||;;;;;||;;;;;||;;;;;||;;;;;||;;;;||;;;;;|| |
 (=      | |   -'|||;;;;;||;;;;;||;;;;;||;;;;;||;;;;||;;;;;||_|__
 |  _..--' |____.'||;;;;;||;;;;;||;;;;;||;;;;;|'----'|;;;;;||____|
 |-'.----.  _____ |'-----''-----''-----''-----'.----.'-----'|.....
|=./ .--. \|=====||___________________________/ .--. \______] 
'=' :(--): `-----''--------------------------' :(--): `-----'   
.... `--' ..................................... `--' ..XYZ........
===================\\\\==========================================
""")

answer = ""

answer = input("left or right?\n").lower()

if answer == 'left':
    answer = input("swim or wait?\n").lower()
    if answer == 'wait':
        answer = input("which door red or blue or yellow?\n").lower()
        if answer == 'yellow':
            print("You Win!")
        elif answer == 'red':
            print("Burned by fire. Game Over.")
        elif answer == 'blue':
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")