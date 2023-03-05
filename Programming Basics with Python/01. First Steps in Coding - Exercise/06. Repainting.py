nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())
nylon_price = 1.5
paint_price = 14.5
thinner_price = 5
bags = 0.4
total_nylon = (nylon + 2) * nylon_price
total_paint = (paint + (paint * 0.1)) * paint_price
total_thinner = thinner * thinner_price
total_materials = total_nylon + total_paint + total_thinner + bags
workers_cost = (total_materials * 0.3) * work_hours
total_sum = total_materials + workers_cost
print(total_sum)