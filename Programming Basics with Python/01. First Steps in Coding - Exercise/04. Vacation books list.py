book_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())
total_hours_per_book = book_pages // pages_per_hour
needed_hours_per_day = total_hours_per_book // days_per_book
print(needed_hours_per_day)