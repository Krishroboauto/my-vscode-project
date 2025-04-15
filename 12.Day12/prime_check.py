import math
def is_prime(num):
    square_root = int(math.sqrt(num))
    #is_prime = True
    for i in range(2, square_root+1):
        rem = num%i
        if rem == 0:
            return False
    return True



print(is_prime(9))
