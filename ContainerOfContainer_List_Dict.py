
## List of Lists
menuList = [ ['Egg Sandwich', 'Bagel', 'Coffee'],
         ['BLT', 'PB&J', 'Turkey Sandwich'],
         ['Soup', 'Salad', 'Spaghetti', 'Tao']]

print('Breakfast Menu:\t', menuList[0])
print('Lunch Menu:\t', menuList[1])
print('Dinner Menu:\t', menuList[2])

#Using two index - container of contained

print("MenuList", menuList[0][1])

## Using dictionary

menuDict = {'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
         'Lunch' : ['BLT', 'PB&J', 'Turkey Sandwich'],
         'Dinner' : ['Soup', 'Salad', 'Spaghetti', 'Tao']}
         
print('\n \n Breakfast Menu :\t', menuDict['Breakfast'])
print('Lunch Menu :\t', menuDict['Lunch'])
print('Dinner Menu :\t', menuDict['Dinner'])

## Printing using double for loop
print( "\n For loop printing \n\n")
for name, menu in menuDict.items():
    print(name, ':', menu)
    