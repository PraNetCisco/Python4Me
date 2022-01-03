price = input("Enter the price:")

try:
    price = float(price)
    print('price =', price)
except ValueError as err:
    print (err)
