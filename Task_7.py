import random
key =  '+-/*!&$#? =@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def password_generagor(length):
    password = ''
    for i in range(length):
        password += random.choice(key)
    return password