def life_in_weeks(age):
    ninety_in_weeks = 90*52
    age_in_weeks = age*52
    age_left = ninety_in_weeks - age_in_weeks
    print(f"you have {age_left} weeks left")

life_in_weeks(47)