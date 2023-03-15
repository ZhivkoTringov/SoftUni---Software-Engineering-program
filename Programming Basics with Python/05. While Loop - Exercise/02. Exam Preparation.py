num_bad_grades = int(input())
failed_times = 0
solved = 0
grade_sum = 0
last = ''
failed = True
while failed_times < num_bad_grades:
    task = input()
    if task == 'Enough':
        failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grade_sum += grade
    solved += 1
    last = task
if failed:
    print(f'You need a break, {failed_times} poor grades.')
else:
    print(f'Average score: {(grade_sum / solved):.2f}')
    print(f'Number of problems: {solved}')
    print(f'Last problem: {last}')