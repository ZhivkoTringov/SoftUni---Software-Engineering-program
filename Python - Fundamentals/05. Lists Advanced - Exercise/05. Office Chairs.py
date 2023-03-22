num_of_rooms = int(input())
total_free_chairs = 0
needed_chairs = 0
for room in range(1, num_of_rooms + 1):
    chairs_and_people = input().split()
    chairs = chairs_and_people[0]
    people = chairs_and_people[1]
    if len(chairs) >= int(people):
        total_free_chairs += len(chairs) - int(people)
    else:
        diff = abs(len(chairs) - int(people))
        needed_chairs += diff
        print(f'{diff} more chairs needed in room {room}')
if total_free_chairs >= needed_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')
