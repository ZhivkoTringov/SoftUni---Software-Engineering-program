sqr_meters = float(input())
price_for_sqr_meter = 7.61
discount = 0.18
total_greening = sqr_meters * price_for_sqr_meter
final_price = total_greening - (total_greening * discount)
discount_price = total_greening * discount
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount_price} lv.')