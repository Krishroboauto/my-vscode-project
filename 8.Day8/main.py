#encryption

from art import logo

print(logo)

alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']





def caeser(original_text, shift_amount):
    encoded_text = []
    decoded_text = []
    for char in u_message:
        if char in alphabet:
            orig_pos = alphabet.index(char)
            if enc_or_dec == 'encode':
                final_pos = (orig_pos + shift_amount) % 26
                encoded_text.append(alphabet[final_pos])
            elif enc_or_dec == 'decode':
                final_pos = (orig_pos - shift_amount) % 26
                decoded_text.append(alphabet[final_pos])
        else:
            if enc_or_dec == 'encode':
                encoded_text.append(char)
            elif enc_or_dec == 'decode':
                decoded_text.append(char)
                
        
    
    if enc_or_dec == 'encode':
        print("Encrypting Message....")
        for letter in encoded_text:
            print(letter, end ="")
        print()
    elif enc_or_dec == 'decode':
        print("Decrypting Message....")
        for letter in decoded_text:        
            print(letter, end ="")
        print()
    else:
        print("sarigga chusko")

'''
def decrypt(original_text, shift_amount):
    decoded_text = []
    for char in u_message:
        orig_pos = alphabet.index(char)
        final_pos = (orig_pos - shift_amount) % 26
        decoded_text.append(alphabet[final_pos])
    print("Encrypting Message....")
    for letter in decoded_text:
        print(letter, end ="")
    print()

  ''' 
        
should_continuie = True
while should_continuie:
    enc_or_dec = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    u_message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(u_message,shift)
    y_or_n = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if y_or_n == 'yes':
        caeser(u_message,shift)
    else:
        should_continuie = False






