secret_message = input().split()
for message in secret_message:
    digits = ''
    current_message = ''
    for character in message:
        if character.isdigit():
            digits += character
        else:
            break
    current_message += (chr(int(digits)))
    message = message.replace(digits, '')
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    current_message += message
    print(current_message, end=' ')
