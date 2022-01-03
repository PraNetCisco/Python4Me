""" Dictonaries: Curly barcket, key, value pair, separated by ":"
    Keys - must be immutable
    value: must be mutable
    Ex. phonetic = dict(a ='alpha', b ='bravo', c ='charlie', d ='delta', e ='echo')
    
Copy Dictionary:
    d = phonetic.copy()
    f = dict(phonetic)
    
Update: dict.update()
    Adds entries from one dictionary into another
    call this on the dictionary that is to be updated
    
Iterable:   for vlaue in colors.values():
                        print (value)
dict.values() : to print values
dict.keys() - to print keys
dict.items() - iterates over keys and values in tandem. Yields(key, value)
tuple on each iteration

Membership operatiors - in or not int works on the keys only

Deleting element - del dict['key']



"""
    
phonetic = dict(a ='alpha', b ='bravo', c ='charlie', d ='delta', e ='echo')
d = phonetic.copy()
f = dict(phonetic)   
print(phonetic)
print("Copy using dict.copy()", d)
print("Copy using newdict = dict(original)", f)

g = {'kaho' : ' hello', 'chalo' : "jao", 'khao' : 'kha'}

phonetic.update(g)
print (phonetic)

# Iteration
for value in phonetic.values():
    print(value)

for key in phonetic.keys():
    print (key)

for key, value in phonetic.items():
    print(f"{key} => {value}")
    
    
    