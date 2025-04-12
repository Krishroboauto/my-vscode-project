#data types, math operators and many more
#datatypes are:
'''
1. Strings --> "Hello"
2. Integers  --> 1,2,3,...
3. Floats and --> 1.2, 3.5, 4.1...
4. Booleans --> True or False'''
'''
print("Hello"[0]) #called subscripting
print("Hello"[-1]) #called subscripting

print("123" + "345") # this is a string concatanetion

#Large integers
print(123_456_789)  #the underscores are ignored in python

#float
print(3.14)

#boolean
print(True)
print(False)



len("12345")


print(type("string"))
print(type(123))
print(type(1.25))
print(type(True))


print(int("123") + int("345"))'
'''

#Input_Name = len(input("Enter your name: "))
#print("Number of letters in your name: ", Input_Name)

#print("Number of letters in your name: ", len(input("Enter your name: ")))

print("Number of letters in your name: " +  str(len(input("Enter your name: "))))