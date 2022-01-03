"""
Set - unordered collection of unique elements
set are mutable
Elements in a set must be immutable

Ex: p = {1, 2, 44, 32, 43}

imp: removes duplicate items from the set

sets are iterable 
for value in set1():
    print (value)

membership is allowed using "in" or "not in"

Adding element - set.add(value)
set.update([value1, value2])

Removing element - k.remove(value)
k.discard(value)

Copy - newset = set.copy()

"""

set1 = {4,5,6,63,44,44,43}
set2 = set()
set3 = set([45,23,23,23,1,12,121,1213])

print (set1)

for value in set1:
    print (value)

print (set3)

