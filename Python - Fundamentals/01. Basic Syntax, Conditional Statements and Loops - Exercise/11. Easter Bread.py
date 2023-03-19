budget = float(input())
flour_price = float(input())
egg_counter = 0
bread_counter = 0
loafs_of_bread = 0
egg_price = 0.75 * flour_price
litter_milk_price = 0.25 * flour_price + flour_price
one_loaf_of_bread = egg_price + flour_price + 0.25 * litter_milk_price
while True:
    if budget <= one_loaf_of_bread:
        break
    budget -= one_loaf_of_bread
    bread_counter += 1
    egg_counter += 3
    if bread_counter % 3 == 0:
        egg_counter -=bread_counter - 2
total_sum = loafs_of_bread * one_loaf_of_bread
print(f'You made {bread_counter} loaves of Easter bread! Now you have {egg_counter} eggs and {budget:.2f}BGN left.')