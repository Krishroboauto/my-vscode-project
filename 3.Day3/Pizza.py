print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want S,M or L:")
pepperoni = input("Do you want pepperoni on your pizza? Y or N?")
extra_cheese = input("Do you want extra cheese Y or N?")
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("you typed a wrong statement")

if pepperoni == "Y" and size == "S":
    price += 2
elif pepperoni == "Y" and (size == "M" or size == "L"): 
    price += 3

if extra_cheese == "Y":
     price += 1

print(f"Total Bill: {price}")

