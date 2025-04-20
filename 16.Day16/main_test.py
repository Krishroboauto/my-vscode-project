# import another_module
# print(another_module.my_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_Screen = Screen()
# print(my_Screen.canvheight)
# my_Screen.exitonclick()

from prettytable  import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name",
["Pikachu","Squirtle","Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"


print(table)






