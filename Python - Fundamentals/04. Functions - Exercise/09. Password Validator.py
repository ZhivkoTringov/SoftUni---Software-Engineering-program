def valid_pass(characters):
    num_of_digits = 0
    if 6 > len(characters) <= 10:
        print('Password must be between 6 and 10 characters')
    for digits in characters:
        if digits.isdigit():
            num_of_digits += 1
    if num_of_digits < 2:
        print('Password must have at least 2 digits')
    if not characters.isalnum():
        print('Password must consist only of letters and digits')
    if 6 <= len(characters) <= 10 and num_of_digits >= 2 and characters.isalnum():
        print('Password is valid')


password = input()
(valid_pass(password))
