try:
    age = int(input("How old are you?"))
except ValueError:
    print("you have typed an invalid number, try agin with a numberical value")
    age = int(input("How old are you?"))

if age > 18:
    print(f"you can drive at age {age}")

