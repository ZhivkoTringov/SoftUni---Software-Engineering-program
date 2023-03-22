text = input().split(' ')
even_length = [x for x in text if len(x) % 2 == 0]
print('\n'.join(even_length))
