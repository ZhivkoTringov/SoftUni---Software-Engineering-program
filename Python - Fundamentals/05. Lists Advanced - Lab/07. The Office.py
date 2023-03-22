happiness = list(map(int, input().split(' ')))
happy_employees_counter = 0
happiness_counter = 0
factor = int(input())
improvement = list(map(lambda x : int(x) * factor, happiness))
average = sum(improvement) / len(improvement)
happy_employees = [k for k in improvement if k >= average]
for l in range(len(happiness)):
    happiness_counter += 1
for m in range(len(happy_employees)):
    happy_employees_counter += 1
if len(happy_employees) >= len(happiness) / 2:
    print(f'Score: {happy_employees_counter}/{happiness_counter}. Employees are happy!')
else:
    print(f'Score: {happy_employees_counter}/{happiness_counter}. Employees are not happy!')