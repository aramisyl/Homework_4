l, u, s, d = 0, 0, 0, 0
special_character = list("!%@#$^&")
user_password = input("Please enter your password")

if len(user_password) >= 8:
    for i in user_password:
        if i.isupper():
            u += 1

        if i.islower():
            l += 1

        if i in special_character:
            s += 1

        if i.isdigit():
            d += 1

if u == 0 or l == 0 or s == 0 or d == 0:
    print("Пароль должен содержать минимум один строчный и заглавный символ, цифру и спецсимвол.")
else:
    if u >= 1 and l >= 1 and s >= 1 and d >= 1 and u + l + s + d == len(user_password):
        print("Надежный пароль")
    else:
        print("Пароль не надежный")
