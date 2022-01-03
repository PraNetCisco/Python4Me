"""
Tuples are immutable sequences of arbitrary objects
Once created, objects inside cannot be modifed, added or removed
    
Tuple literals are optional paranetheses around comma-separated items
    
Use a trailing comma for singe element tuples
single tuple can be created using an item followed by comma,  k = (391,)

Tuple unpacking is useful for multiple return values and swapping

"""
    
    
    
t = ("Norway", 4.954, 2)
    

def minmax(items):
    return min(items), max(items)
    
minmax([83,23,23,24,44,53])