enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    

increase_enemies()
#print(f"enemies outside function: {enemies}")

# player_health has global scope
player_health = 10

# Local scope
def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

player_health = 10

if 3>2:
    a_variable = 12


