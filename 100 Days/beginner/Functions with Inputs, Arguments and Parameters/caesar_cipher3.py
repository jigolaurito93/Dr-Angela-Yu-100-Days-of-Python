from cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue= True

print(logo)


#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(code_message, shift_amount, direction):
    plain_text = ""
    for char in code_message:
        
        if char in alphabet:
            if direction == "encode":
                position = alphabet.index(char)
                new_position = position + shift_amount
            elif direction == "decode":
                position = alphabet.index(char)
                new_position = position - shift_amount
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    if direction == "encode":
        print(f"The encoded text is {plain_text}")
    elif direction == "decode":
        print(f"The decoded text is {plain_text}.")
    

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

    shift = shift % 26
    caesar(code_message=text, shift_amount=shift, direction=direction)

    result = input(f"Do you want to restart the program? (y/n):\n").lower()
    if result == 'n':
        should_continue = False
        print("Goodbye!")







