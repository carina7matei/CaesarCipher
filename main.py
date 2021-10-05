alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text,shift,direction):
    end_text=""
    if direction == 'decode':
        shift *=-1
    for char in text:
        if char in alphabet:
            # ne va trb doar indicele primei aparitii a literei
            position=alphabet.index(char)
            new_position=position + shift
            end_text +=alphabet[new_position]
        else:
            end_text+=char
    print(f"Here's the {direction}d message: {end_text}")
from art import logo
print(logo)
game_on=True
while game_on:
    direction=input("Type 'encode' to encrypt,or 'decode' to decrypt: ")
    text=input(f"Enter the text you want to {direction}: ")
    shift=int(input("Type the shift number: "))
    shift =shift % 26
    caesar(text,shift,direction)
    restart=input("Do you want to continue? Type 'y' or 'n': ").lower()
    if restart == 'n':
        game_on=False
        print("Good Bye!")

