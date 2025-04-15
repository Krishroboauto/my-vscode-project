import random

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")

def high_low(): 

    r_numb = random.randint(1,100)
    #print(r_numb)


    level = input("choose a difficulty. Type 'easy' or 'hard' ").lower()
    if level == 'easy':
        n_attempts = 10
    elif level == 'hard':
        n_attempts = 7
    print(f"you have {n_attempts} attempts to guess the number")
        
    for i in range(n_attempts):
        n_guess = int(input("Make a guess: "))
        n_attempts -= 1
        if n_guess == r_numb:
            print("you guessed it correct!")
            return 
        elif n_guess > r_numb:
            print("Too High")            
            print(f"you have {n_attempts} attempts to guess the number")
        elif n_guess < r_numb:
            print("Too Low")
            print(f"you have {n_attempts} attempts to guess the number")
    if n_attempts == 0:
        print(f"Too bad! The number was {r_numb}")
    

high_low()


