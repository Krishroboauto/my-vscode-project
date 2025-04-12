#%%
'''Printing, commenting, variables, basics of Python'''
# In the end we create a project called Band Generator

print ("Hello World!")



#%%
print("1. Mix 500g of Flour, 10g Yeast and 300ml water in a bowl")
print("2. Knead the dough for 10 minutes")
print("3. Add 3g of salt")
print("4. Leave to rise for 2 hours")
print("5. Bake at 200 degrees C for 30 minutes")

#%% Using backslash
print("1. Mix 500g of Flour, 10g Yeast and 300ml water in a bowl\n2. Knead the dough for 10 minutes")



# %% concatenate strings
print ("Hello" + " Buddi")
# %% this does not work so well while running in a block
input("What is your name?")
# %%
print("Hello " + input("what is your name?") + "!")
# %%
inputName = input("What is your name?")
x = len(inputName)
print(f"your name has {x} characters")


# %%

namesize = print(len(input("what is your name?")))

# %%
glass1 = "milk"
glass2 = "juice"

temp1 = glass1 #now temp has milk in it and glass1 has milk as well
glass1 = glass2 # with this glass1 should have juice
glass2 = temp1 #glass2 should have milk in that
print(glass1, glass2)

# %% Bandname generator
City_Name = input("Welcome to the Band Name Generator.\n Whats the name of the city you grew in?\n")
print(City_Name)
# %%
