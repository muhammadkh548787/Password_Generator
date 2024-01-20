import pathlib
from pathlib import Path
class ShoppingCart:

    def __init__(self, cwd):
        self.cwd = cwd
    def add(self):
        item = input("What you want to buy: ")
        price = int(input("Enter the price: "))
        file_name = 'prices.txt'
        file = 'items.txt'
        with open(file, 'a') as f:
            f.write((item)+ '\n')
        with open(file_name, 'a') as f:
            f.write(str(price)+ " ")
    def show(self):
        ert = input("What to show(prices/items): ")
        file_path = Path("items.txt")
        fp = Path("prices.txt")
        if ert == "items":
            file = open(file_path, 'r')
            file_content = file.read()
            file.close
            print(file_content)
        elif ert == "prices":
            files = open(fp, 'r')
            file_contents = files.read()
            files.close
            print(file_contents)
    def calculate(sef):
        file = Path('prices.txt')
        total_price = 0
        
        with open(file, 'r') as f:
            for line in f:
                price = float(line.strip())
                total_price += price
                
        print(total_price)
     

    