name = input('Введите имя и фамилию')
last_letter = name[-1]

match last_letter:
    case "а" | "я":
        print("Здравствуйте, госпожа {}".format(name.split(" ")[1]))
    case _:
        print("Здравствуйте, господин {}".format(name.split(" ")[1]))
