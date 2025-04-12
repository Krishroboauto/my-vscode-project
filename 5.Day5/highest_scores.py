student_scores = [50,30,45,63,45,33,45,11,24,23,26,27,30,80,91,99,100]

#total = print(sum(student_scores))
#sum_student = 0


max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score


print(max_score)

other_way_max = max(student_scores)
print(other_way_max)