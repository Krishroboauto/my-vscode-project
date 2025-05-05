student_scores = {
    'Harry' : 95,
    'Gopi' : 67,
    'lash' : 10,
    'Abhi' : 78,
    'All' : 65
}

student_grades = {}

for item in student_scores:
    if 91 <= student_scores[item] <= 100:
        grade = "outstan"
    elif 81 <= student_scores[item] <= 90:
        grade = "exceeds expec"
    elif 71 <= student_scores[item] <= 80:
        grade = "acceptable"   
    else:
        grade = "fail"   
    student_grades[item] = grade

print(student_scores)
print(student_grades)