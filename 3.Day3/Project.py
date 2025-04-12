print('''
   _____       .___             .__  __  .__                         .___ _________ .__    .__                             /\      
  /  _  \    __| _/__  _______  |__|/  |_|  |__   _____    ____    __| _/ \_   ___ \|  |__ |__| ____   _____ _____  ___.__.)/_____ 
 /  /_\  \  / __ |\  \/ /\__  \ |  \   __\  |  \  \__  \  /    \  / __ |  /    \  \/|  |  \|  |/    \ /     \\__  \<   |  |/  ___/ 
/    |    \/ /_/ | \   /  / __ \|  ||  | |   Y  \  / __ \|   |  \/ /_/ |  \     \___|   Y  \  |   |  \  Y Y  \/ __ \\___  |\___ \  
\____|__  /\____ |  \_/  (____  /__||__| |___|  / (____  /___|  /\____ |   \______  /___|  /__|___|  /__|_|  (____  / ____/____  > 
        \/      \/            \/              \/       \/     \/      \/          \/     \/        \/      \/     \/\/         \/  
___________                                                   .__                  __                                              
\__    ___/______   ____ _____    ________ _________   ____   |  |__  __ __  _____/  |_     _________    _____   ____              
  |    |  \_  __ \_/ __ \\__  \  /  ___/  |  \_  __ \_/ __ \  |  |  \|  |  \/    \   __\   / ___\__  \  /     \_/ __ \             
  |    |   |  | \/\  ___/ / __ \_\___ \|  |  /|  | \/\  ___/  |   Y  \  |  /   |  \  |    / /_/  > __ \|  Y Y  \  ___/             
  |____|   |__|    \___  >____  /____  >____/ |__|    \___  > |___|  /____/|___|  /__|    \___  (____  /__|_|  /\___  > ''')



print("Welcome to the Treasureisland game:")
choice_l_r  = input("Choose left(l) or right(r): \n").lower()

if choice_l_r == "r":
    print("game over because you fell into a hole")
elif choice_l_r == "l":
    swim_or_wait = input("Do you want to swim or wait: \n").lower()
    if swim_or_wait == "swim":
        print("game over because you are a bad swimmer")
    elif swim_or_wait == "wait":
        choose_door = input("choose a color of the door: yellow, red or blue: \n").lower()
        if choose_door == "red" or choose_door == "blue":
            print("game over as there is a an angry dinosaur here")
        elif choose_door == "yellow":
            print("You Win! you found the treasure")
        else:
            print("Please correct your answer, yellow, red or blue")
    else:
        print("Please correct your answer, swim or wait")
else:
    print("Please correct your answer, l or r")



