""" Negative indices : - Index from the end of the sequences using the 
negative number

Last Element = index -1

Negative indexing is 1 based and not 0 based like positive

Slicing :  Extended form of indexing for referring to a portion of a
list or other sequence.

Syntax: list[start:stop] -stop index is not included in output

list[1:-1] - will print all but first and last items
list[2:] - 3rd to the end of list
list[:2] - print starting to 3rd item
list[:] - prints whole list
list use repetition using multiplication operator
list[] * 9

Index method: list.index()
Find the location of an object in a list
returns the index of the first list element which is equal to the argument

list.index('item') - to find index of item in the list 
list.count('item') - returns the number of times item is present in list

item in list - to test for presence of item in list
item not in list - to test absence of item in list

Deleting an element : del list[index] - Remove element from a list by index
Syntax : del list[index] or list.remove('element')

Inserting an element: list.insert() - Accepts an item and the index of
the the new item

Reversing and sorting : list.reverse() [also reveresed() can be used] 
and list.sort() or [sorted() can be used]

list.sort() - can accept two parameter, key and reverse
list.sort(reverse = True) - Ascending sort (when set to True)
list.sort(key)- key can be any callable (ex. len function) object that accepts a single parameter
Items passed to callable and sorted on ites return value

"""
r = [1, 2, 3, 3, 9, -16, 12, 13]
last = r[-1]
Secondlast = r[-2]
first = r[0]

print("Last item in", last)
print("2nd Last item in", Secondlast)
print("First item in", first)

w = "the quick brown fox jumps over the lazy dog".split()
print("list is ", w)
i = w.index('fox')
print("index for 'fox' is using list.index()", i)

count = w.count('the')
print("number of times 'the' is present in list using count.list()' is", count)

w.insert(3, 'yellow')
print ("inserted yellow at the location 4 of the old stirng", w)

w = ' '.join(w)
print ("joined string using ' '.join(list)  : ", w)

h = 'not perplexing do handwriting family where I illegibly know doctors'.split()

sortedlist=h.sort(key=len)

print("sorted list using key = len", h)






