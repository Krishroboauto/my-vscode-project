import art
import random
import game_data
from os import system

print(art.logo)
A_compare = random.choice(game_data.data)
print(f"Compare A: {A_compare['name']}, a {A_compare['description']}, from {A_compare['country']} ")
print(art.vs)
B_compare = random.choice(game_data.data)
if A_compare == B_compare:
    B_compare = random.choice(game_data.data)
print(f"Against B: {B_compare['name']}, a {B_compare['description']}, from {B_compare['country']} ")
user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
system("clear")


current_score = 0
game_continue = True
while game_continue:
    if user_input == 'a':
        if A_compare['follower_count'] > B_compare['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            A_compare = B_compare
            print(art.logo)
            print(f"Compare A: {A_compare['name']}, a {A_compare['description']}, from {A_compare['country']} ")
            B_compare = random.choice(game_data.data)
            print(art.vs)
            print(f"Against B: {B_compare['name']}, a {B_compare['description']}, from {B_compare['country']} ")
            user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
            system("clear")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_continue = False
    elif user_input == 'b':
        if B_compare['follower_count'] > A_compare['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            A_compare = B_compare
            print(art.logo)
            print(f"Compare A: {A_compare['name']}, a {A_compare['description']}, from {A_compare['country']} ")
            B_compare = random.choice(game_data.data)
            print(art.vs)
            print(f"Against B: {B_compare['name']}, a {B_compare['description']}, from {B_compare['country']} ")
            user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
            system("clear")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_continue = False


