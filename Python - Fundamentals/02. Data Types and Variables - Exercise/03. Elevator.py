from math import ceil

num_of_people = int(input())
elevator_capacity = int(input())
courses = ceil(num_of_people / elevator_capacity)
print(courses)