month = input()
nights = int(input())
studio = 0
apartment = 0
if month in 'May October':
    if 7 < nights <= 14:
        apartment = 65 * nights
        print(f'Apartment: {apartment:.2f} lv.')
        studio = (50 - 50 * 0.05) * nights
        print(f'Studio: {studio:.2f} lv.')
    elif nights > 14:
        apartment = (65 - 65 * 0.1) * nights
        print(f'Apartment: {apartment:.2f} lv.')
        studio = (50 - 50 * 0.30) * nights
        print(f'Studio: {studio:.2f} lv.')
    elif nights <= 7:
        apartment = 65 * nights
        print(f'Apartment: {apartment:.2f} lv.')
        studio = 50 * nights
        print(f'Studio: {studio:.2f} lv.')
elif month in 'June September':
    if nights > 14:
        apartment = (68.70 - 68.70 * 0.1) * nights
        print(f'Apartment: {apartment:.2f} lv.')
        studio = (75.20 - 75.20 * 0.20) * nights
        print(f'Studio: {studio:.2f} lv.')
    else:
        apartment = 68.70 * nights
        print(f'Apartment: {apartment:.2f} lv.')
        studio = 75.20 * nights
        print(f'Studio: {studio:.2f} lv.')
elif month in 'July August':
    if nights > 14:
        apartment = (77 - 77 * 0.1) * nights
        print(f'Apartment: {apartment:.2f} lv.')
        studio = 76 * nights
        print(f'Studio: {studio:.2f} lv.')
    elif nights <= 14:
        apartment = 77 * nights
        print(f'Apartment: {apartment:.2f} lv.')
        studio = 76 * nights
        print(f'Studio: {studio:.2f} lv.')