students_tracker = {}
num_pairs = int(input())
for num in range(num_pairs):
    student = input()
    grade = float(input())
    if student not in students_tracker:
        students_tracker[student] = []
        students_tracker[student].append(grade)
    elif student in students_tracker:
        students_tracker[student].append(grade)
for key in students_tracker:
    students_tracker[key] = sum(students_tracker[key])/len(students_tracker[key])
    if students_tracker[key] >= 4.5:
        print(f"{key} -> {students_tracker[key]:.2f}")
