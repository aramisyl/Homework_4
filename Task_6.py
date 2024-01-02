line = input('Введите список чисел').split(", ")

even_counter = 0
for i in line:
    match int(i):
        case int() if int(i) % 2 == 0:
            even_counter += int(i)
        case _:
            continue

print(even_counter)
