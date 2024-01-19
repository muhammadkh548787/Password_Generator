import random

print("--------------------------")
print("|____PASSWORD-GENERATOR____|")
print("--------------------------")

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "[]()//*-+@#$%^&*!?<>:;.,`"
all = uppercase + lowercase + numbers + symbols
all1 = uppercase + lowercase + numbers
all2 = lowercase + numbers + symbols
all3 = uppercase + lowercase



plength = int(input("The LENGTH of your password: "))
pupper = int(input("The number of UPPER letters: "))
plower = int(input("The number of LOWER letters: "))
pnumbers = int(input("The amount of NUMBERS: "))
psymbols = int(input("The number of SYMBOLS: "))

password = ""

for i in range(pupper):
    password += random.choice(uppercase)
for i in range(plower):
    password += random.choice(lowercase)
for i in range(pnumbers):
    password += random.choice(numbers)
for i in range(psymbols):
    password += random.choice(symbols)

another = plength - (pupper + plower + pnumbers + psymbols)

for i in range(another):
    password += random.choice(all)



password = list(password)
random.shuffle(password)
print("".join(password))






