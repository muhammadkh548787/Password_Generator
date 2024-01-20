from pro2 import ShoppingCart
import pathlib

print("1. Add")
print("2. Show")
print("3. Calculate")



cwd=pathlib.Path.cwd()
file_manager=ShoppingCart(cwd)

run = True
while run:
    x = input("Choose your choice: ")

    if x == "1":
        file_manager.add()
    elif x == "2":
        file_manager.show()
    elif x == "3":
        file_manager.calculate()

