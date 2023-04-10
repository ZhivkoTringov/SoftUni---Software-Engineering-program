num_of_el = int(input())
chemical_el = set()
for _ in range(num_of_el):
    el = set(input().split())
    for i in el:
        chemical_el.add(i)
for j in chemical_el:
    print(j)