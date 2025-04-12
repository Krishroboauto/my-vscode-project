import random
import hangman_words
from hangman_art import stages, logo3

lives = 6

print(logo3)


chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)

placeholder = ""

for count in chosen_word:
    placeholder = placeholder +  "_" + " "

print(placeholder)

# Convert to a list so we can update it
game_over = False
correct_letters = []

while not game_over:

    print(f"**********************************{lives}/6 LIVES LEFT*******************************************")
    guess = input("Guess a Letter: ").lower()

    if guess in correct_letters:
        print(f"you have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter + " "
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter + " "

        else:
            display += "_ "

    print(display)



    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, thats not in the word, you lose a life")

    if "_" not in display:
        game_over = True
        print("*********************************************you win******************************************")
    
    if lives == 6:
        print(stages[6])
    elif lives == 5:
        print(stages[5])
    elif lives == 4:
        print(stages[4])
    elif lives == 3:
        print(stages[3])   
    elif lives == 2:
        print(stages[2])  
    elif lives == 1:
        print(stages[1])
    elif lives == 0:
        print(stages[0])
        game_over = True
        print(f"********************************It was {chosen_word} You Lose!**********************************")