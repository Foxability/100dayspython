from caesar_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, shift_direction):

    result = ""

    if shift_direction == "decode": shift_amount *= -1 # When we decode we swift to left from current index, when we encode we swift to right from current index.

    for char in text:
         if char in alphabet:
                new_index = alphabet.index(char) + shift_amount
                new_index = new_index % 26
                result += alphabet[new_index]

         else: result += char
                 

    print(f"Here's the {shift_direction}d result: {result}")

is_active = True

while is_active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_amount=shift, shift_direction=direction)
    
    keep_doing = input("Would you like to encode or decode something else? (Y/N)\n").lower()
    if keep_doing == 'n':
        is_active = False
        print("Goodbye! 👋")

