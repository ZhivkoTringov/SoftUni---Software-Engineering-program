day_of_week = input()
ticket_price = 0
if day_of_week in 'Monday Tuesday Friday':
    ticket_price = 12
elif day_of_week in 'Wednesday Thursday':
    ticket_price = 14
elif day_of_week in 'Saturday Sunday':
    ticket_price = 16
print(ticket_price)