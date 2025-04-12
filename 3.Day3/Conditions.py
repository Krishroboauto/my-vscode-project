# If/Else statement ticket vending machine 
Height = float(input("Enter your Height: "))


if Height > 120:
    print("can ride")
    age = int(input("Enter your age:"))
    if age > 18:
        TP = 12
        print("ticket price = 12$")
    elif age > 12 and age < 18:
        TP = 7
        print("ticket price = 7$")
    else:
        TP = 5
        print("ticket price = 5$")
    wants_photo = input("Do you want a photo Y or N:")
    if wants_photo:
        TP = TP + 3;
        print(f"Total price of the ticket is {TP}$")
else:
    print("cannot ride")



