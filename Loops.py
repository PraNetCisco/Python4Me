import random

slang = ['Knackered', 'pip pip', 'squidgy', 'smashin']
# For loop

menu = []
for word in slang:
    menu.append(word + ' Spam')
print (menu)

for i in range (10):
    print (i)

# range with start, stop and step values
for i in range (2000, 2020, 2):
    print (i)
    
menu_prices = {}
price = 0.50
for item in menu:
    menu_prices[item] = price
    price = price + 1
    
print (menu_prices)

for name, price in menu_prices.items():
    print(name, ': $', format(price, '.2f'), sep ='')


orders=[]
order = input("What would you like to order? (Q to Quit)")

while (order.upper() != 'Q'):
    # Find the order and add it to the list of it eists
    found = menu_prices.get(order)
    if found:
            orders.append(order)
    else:
            print("Menu item doesn't exist")
    
    order = input("Anything else? (Q to Quit)")

print (orders)





