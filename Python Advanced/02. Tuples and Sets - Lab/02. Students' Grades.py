nums = int(input())
students = {}
for n in range(nums):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))
for name, grades in students.items():
    grade_list = ' '.join(str(f"{grade:.2f}") for grade in grades)
    average_grade = sum(grades) / len(grades)
    print(f'{name} -> {grade_list} (avg: {average_grade:.2f})')