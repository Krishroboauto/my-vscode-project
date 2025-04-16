print("Welcome to the tip calculator!")
Total_Bill = input("What was the total bill? $")
Total_Bill = float(Total_Bill)
print(type(Total_Bill))
Tip_Percent = int(input("How much tip % would you like to give? 10,12 or 15?"))
print(type(Tip_Percent))

Bill_with_Tip = Total_Bill * (1+ Tip_Percent/100)

Total_number_of_people = int(input("How many people to split the bill?"))
Bill_per_person = round(Bill_with_Tip/Total_number_of_people,2)
print(f"Each person should pay: ${Bill_per_person}")