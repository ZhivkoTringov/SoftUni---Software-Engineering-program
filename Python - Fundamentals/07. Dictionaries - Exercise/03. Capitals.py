country_names = input().split(', ')
capital_names = input().split(', ')
country_capital = {country_names[index] : capital_names[index]  for index in range(len(capital_names))}
for key, value in country_capital.items():
    print(f'{key} -> {value}')