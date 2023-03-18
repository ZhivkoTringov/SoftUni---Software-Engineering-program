num_messages = int(input())
for i in range(1,num_messages+1):
    current_num = int(input())
    if current_num == 88:
        print('Hello')
    elif current_num == 86:
        print('How are you?')
    elif current_num > 88:
        print('Bye.')
    else:
        print('GREAT!')