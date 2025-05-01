def greet():
    print("Hello")
    print("This is my second Hello")
    print("This is my third Hello!")

greet()

def greet_name(name):
    print(f"Hello, {name}")

greet_name("Billie")

def greet_new(name, location):
    print(f"Hello {name}")
    print(f"Are you from {location}")

greet_new("advaith", "enschede")
greet_new(location = "London", name = "Angela")