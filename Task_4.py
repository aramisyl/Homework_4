name = input('Введите имя и фамилию')
last_letter = name[-1]
print(last_letter)

match last_letter:
    case "а":
        print("Здравствуйте, госпожа {}".format(name.split(" ")[1]))
    case "я":
        print("Здравствуйте, госпожа {}".format(name.split(" ")[1]))
    case _:
        print("Здравствуйте, господин {}".format(name.split(" ")[1]))
