import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
l = int(input("Введите длину вашего пароля: "))
password = ""
while l!=0:
    l-=1
    pas = random.choice(symbols)
    password = password + pas
print(password)
