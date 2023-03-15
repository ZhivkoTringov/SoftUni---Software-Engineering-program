the_book = input()
book_counter = 0
while True:
    book_name = input()
    if book_name == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break
    if book_name == the_book:
        print(f'You checked {book_counter} books and found it.')
        break
    book_counter += 1