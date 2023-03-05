number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegi_menus = int(input())
chicken_menu = 10.35
fish_menu = 12.40
vegi_menu = 8.15
delivery = 2.5
chicken_price = number_chicken_menus * chicken_menu
fish_price = number_fish_menus * fish_menu
vegi_price = number_vegi_menus * vegi_menu
total_menu_price = chicken_price + fish_price + vegi_price
desert_price = total_menu_price *0.2
order_price = total_menu_price + desert_price + delivery
print(order_price)


