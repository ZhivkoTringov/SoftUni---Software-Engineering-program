name = input()
average_grade = 0
bad_grade = 0
class_counter = 0
bad_grade_condition = False
while class_counter < 12:
    annual_grade = float(input())
    if annual_grade < 4:
       bad_grade += 1
       if bad_grade > 1:
           bad_grade_condition = True
           class_counter += 1
           break
    else:
        average_grade += annual_grade
        class_counter += 1
if bad_grade_condition:
    print(f'{name} has been excluded at {class_counter} grade')
else:
    average_grade /= class_counter
    print(f'{name} graduated. Average grade: {average_grade:.2f}')