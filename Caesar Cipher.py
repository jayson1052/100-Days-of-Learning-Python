from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter.isalpha():
            if letter.islower():
                shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
                output_text += alphabet[shifted_position]
            else:  
                shifted_position = (alphabet.index(letter.lower()) + shift_amount) % len(alphabet)
                output_text += alphabet[shifted_position].upper()
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    else:
        print("Please type in the correct command!")
        continue
    again = input("Do you want to try again? Yes or No\n").lower()
    if again == "no":
        break
    elif again == "yes":
        continue

