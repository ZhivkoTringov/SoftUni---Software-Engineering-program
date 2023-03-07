from math import ceil

serial_name = input()
episode_length = int(input())
break_length = int(input())
lunch_time = (break_length * (1 / 8))
rest_time = (break_length * (1 / 4))
time_left = break_length - lunch_time - rest_time
diff = ceil(abs(time_left - episode_length))
if time_left >= episode_length:
    print(f'You have enough time to watch {serial_name} and left with {diff} minutes free time.')
elif time_left < episode_length:
    print(f"You don't have enough time to watch {serial_name}, you need {diff} more minutes.")