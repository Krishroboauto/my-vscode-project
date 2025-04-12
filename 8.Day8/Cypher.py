from art import logo

print(logo)

alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(original_text, shift_amount, encode_decode):
    final_text = ""
    if encode_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            shift_index = (index + shift_amount) % 26
            final_text += alphabet[shift_index]
        else:
            final_text += char  # Keep symbols, numbers, and spaces unchanged
    print(f"The {encode_decode}d text is: {final_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    redo = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if redo == "no":
        should_continue = False
        print("Bye bye")


