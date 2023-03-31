user_names = input().split(', ')
for valid_user_name in user_names:
    if 3 <= len(valid_user_name) <= 16 and valid_user_name.isalnum() and ',' not in valid_user_name or '-' in valid_user_name or '_' in valid_user_name:
        print(valid_user_name)
