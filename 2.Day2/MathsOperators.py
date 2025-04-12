# +, -, /, //, %

print(7-3)
print(6*4)
print(6/3) # --> returns a float
print(6//3) # --> returns an integer be carful as the result is int 
print(2**3)

### priority - division first and - remember PEMDAS - Perenthesis, Exponent, Multiplication, Division, Addition and Subtraction

print(3*(3 + (3/3) - 3))

bmi = 84/1.65**2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi,2))

### Assignment operator

score = 0
# user scores a point

score = score + 1
# OR
score += 1

# f strings
score = 0
height = 1
is_winning = True
print(f"The score is {score} and the height of the person is {height} and this is {is_winning}")

