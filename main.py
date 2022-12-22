from art import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

at_end_of_chat = False
while not at_end_of_chat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caeser(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            if shift_amount > 25:
                shift_amount_ = (shift_amount % 26)
                shift_amount = shift_amount_ * (-1)
            else:
                shift_amount *= -1
        for letter in start_text:
            if letter not in alphabets:
                end_text += letter
            else:
                position = alphabets.index(letter)
                new_position = position + shift_amount
                end_text += alphabets[new_position]
        print(f"The {cipher_direction}d text is {end_text}")

    caeser(text, shift, direction)
    continua = input("Do you want to restart the cipher program. Yes or No ").lower()
    if continua == "yes":
        at_end_of_chat = False
    elif continua == "no":
        at_end_of_chat = True
