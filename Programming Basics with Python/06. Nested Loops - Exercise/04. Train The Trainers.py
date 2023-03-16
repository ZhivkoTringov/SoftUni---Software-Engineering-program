num_jury = int(input())
presentation_counter = 0
total_grades = 0
while True:
    current_grade = 0
    name_of_presentation = input()
    if name_of_presentation == 'Finish':
        total_grades /= presentation_counter * num_jury
        print(f"Student's final assessment is {total_grades:.2f}.")
        break
    presentation_counter += 1
    for n in range(num_jury):
        jury_current_grade = float(input())
        current_grade += jury_current_grade
        total_grades += jury_current_grade
    current_grade /= num_jury
    print(f'{name_of_presentation} - {current_grade:.2f}.')
