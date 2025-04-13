from os import system

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    n1 = float(input("Enter the First number: "))


    looping = True 
    while looping:
        
        oper = input('Enter the Mathematical Operation \n + \n - \n * \n / \n ')
        n2 = float(input("Enter the Second number: "))
        result = operations[oper](n1, n2)
        print(f"{n1} {oper} {n2} = {result}")
        next_oper = input(f"Do you want to continue next oper with {result} yes or no").lower()

        if next_oper == "yes":
            n1 = result
        else:
            looping = False
            system("clear")
            calculator()

calculator()

 
 