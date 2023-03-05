numbers_pen = int(input())
number_markers = int(input())
detergent_lt = int(input())
discount = int(input())
pen_price = 5.8
marker_price = 7.2
detergent_price = 1.2
pen_cost = numbers_pen * pen_price
marker_cost = number_markers * marker_price
detergent_cost = detergent_lt * detergent_price
total_materials = pen_cost + marker_cost + detergent_cost
total_price_with_discount = total_materials - (total_materials * discount/100)
print(total_price_with_discount)