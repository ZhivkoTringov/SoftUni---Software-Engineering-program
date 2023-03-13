width = int(input())
length = int(input())
pieces = width * length
while pieces > 0:
    num_pieces = input()
    if num_pieces == 'STOP':
        break
    pieces -= int(num_pieces)
if pieces < 0:
    print(f'No more cake left! You need {abs(pieces)} pieces more.')
else:
    print(f'{abs(pieces)} pieces are left.')