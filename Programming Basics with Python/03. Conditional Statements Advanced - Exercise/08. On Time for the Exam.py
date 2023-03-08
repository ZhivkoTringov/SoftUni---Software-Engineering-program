hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
time_of_exam = hour_of_exam * 60 + minute_of_exam
time_of_arrival = hour_of_arrival * 60 + minute_of_arrival
diff = abs(time_of_arrival - time_of_exam)
if time_of_exam == time_of_arrival:
    print('On time')
elif time_of_arrival > time_of_exam:
    print('Late')
    hour = diff // 60
    minutes = diff % 60
    if diff > 59:
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')
elif time_of_arrival < time_of_exam:
    if diff <= 30:
        print('On time')
        hour = diff // 60
        minutes = diff % 60
        print(f'{diff} minutes before the start')
    if 59 >= diff > 30:
        print('Early')
        hour = diff // 60
        minutes = diff % 60
        print(f'{diff} minutes before the start')
    elif diff > 59:
        print('Early')
        hour = diff // 60
        minutes = diff % 60
        print(f'{hour}:{minutes:02d} hours before the start')