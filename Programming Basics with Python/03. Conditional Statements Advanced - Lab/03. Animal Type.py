type_of_animal = input()
if type_of_animal == 'dog':
    print('mammal')
elif type_of_animal in 'crocodile tortoise snake':
    print('reptile')
else:
    print('unknown')