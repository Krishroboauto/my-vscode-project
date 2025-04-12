import random

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","#","$","%","&","(",")","*","+"]

print("Welcome to the Python PW Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))


f_letters = ""
# easy level
for letter in range(0,nr_letters):
    letter_choice = random.choice(letters)
    f_letters = f_letters + letter_choice  

f_numbers = ""
for number in range(0,nr_numbers):
    number_choice = random.choice(numbers)
    f_numbers = f_numbers + number_choice

f_symbols = ""
for symbol in range(0,nr_symbols):
    symbol_choice = random.choice(symbols)
    f_symbols = f_symbols + symbol_choice

pw = f_letters+f_numbers+f_symbols
#print(pw)
pw_list = list(pw)
random.shuffle(pw_list)

Final_password = ""
for char in pw_list:
    Final_password = Final_password + char

print(f"your password is: {Final_password}")


    