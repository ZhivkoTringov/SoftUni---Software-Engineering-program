data = input().split('\\')
text = data[-1]
text_one = text.split('.')
print(f'File name: {text_one[0]}')
print(f'File extension: {text_one[1]}')