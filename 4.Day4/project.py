import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
        ''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

#user choice
comp_list = [rock, paper, scissors]
user_choice = int(input("What do you choose 0 for Rock, 1 for Paper and 2 for Scissors: \n" ))

if user_choice == 0:
    print(f"You chose rock {rock}")
elif user_choice == 1:
    print(f"You chose paper {paper}")
elif user_choice == 2:
   print(f"You chose scissors {scissors}") 
else:
    print("Invalid Choice")

# computer choice
comp_choice = random.randint(0,2)
#print(comp_choice)

if comp_choice == 0:
    print(f"Computer chose rock {rock}")
elif comp_choice == 1:
    print(f"Computer chose paper {paper}")
elif comp_choice == 2:
   print(f"Computer chose scissors {scissors}") 

# winner declaration

if user_choice == 0 and comp_choice == 0:
    print("its a tie!, lets play again")
elif user_choice == 0 and comp_choice == 1:
    print("computer wins!")
elif user_choice == 0 and comp_choice == 2:
    print("you Win!")

if user_choice == 1 and comp_choice == 0:
    print("you Win!")
elif user_choice == 1 and comp_choice == 1:
    print("its a tie!, lets play again")
elif user_choice == 1 and comp_choice == 2:
    print("computer wins!")

if user_choice == 2 and comp_choice == 0:
    print("computer wins!")
elif user_choice == 2 and comp_choice == 1:
    print("you Win!")
elif user_choice == 2 and comp_choice == 2:
     print("its a tie!, lets play again")