while True:
    word = input()
    if word != 'end':
        print(f'{word} = {word[::-1]}')
    else:
        break