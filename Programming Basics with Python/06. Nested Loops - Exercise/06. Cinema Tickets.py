total_tickets = 0
student = 0
standard = 0
kid = 0
condition = False
while True:
    name_of_movie = input()
    if name_of_movie == 'Finish':
        condition = True
        break
    free_seats = int(input())
    ticket_counter = 0
    student_ticket_counter = 0
    standard_ticket_counter = 0
    kid_ticket_counter = 0
    while True:
        type_of_ticket = input()
        if type_of_ticket == 'End':
            break
        if type_of_ticket == 'student':
            student_ticket_counter += 1
            ticket_counter += 1
            total_tickets += 1
            student += 1
        elif type_of_ticket == 'standard':
            standard_ticket_counter += 1
            ticket_counter += 1
            total_tickets += 1
            standard += 1
        elif type_of_ticket == 'kid':
            kid_ticket_counter += 1
            ticket_counter += 1
            total_tickets += 1
            kid += 1
        if free_seats == ticket_counter:
            break
    occupied = ticket_counter / free_seats * 100
    print(f'{name_of_movie} - {occupied:.2f}% full.')
percent_student = student / total_tickets * 100
percent_standard = standard / total_tickets * 100
percent_kid = kid / total_tickets * 100
if condition:
    print(f'Total tickets: {total_tickets}')
    print(f'{percent_student:.2f}% student tickets.')
    print(f'{percent_standard:.2f}% standard tickets.')
    print(f'{percent_kid:.2f}% kids tickets.')
