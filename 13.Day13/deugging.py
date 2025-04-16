#debugging
def my_function():
    for i in range(1,20):
        #print(i)
        if i ==19:
            print("you got it")

#my_function()

# reproduce the bug
from random import randint

dice = ["1","2","3","4","5","6"]
dice_num = randint(1,6)

print(dice[dice_num-1])


