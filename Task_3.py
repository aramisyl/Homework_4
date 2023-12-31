def is_leap_year(year):
    if year in range(1, 2025):
        return 'Високосный' if year % 4 == 0 else 'Не високосный'
    else:
        return 'Введите значение года от 1 до 2024'
