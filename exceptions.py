import sys

""" 
    Raising an exception interrupts program flow
    
    Handle excptions with try... except..finally 
    
    Exceptions can be detected within try-blocks
    
    Except-blocks define the handlers for exceptions
    
    Except-blocks can capture the exceptions
    
    raise without and argument re-raises the current exception
    
    Don't catch TypeErrors
    
    Use str() to convert exceptiosn to strings
    
    
    IndexError = out of bound indexing
    Existing built-in exceptions are often the right ones to use
    
    KeyError - non existant key for dictonary
    ValueError - An object is of the correct type but has an inappropriate
    value - int("jim")
    
    
"""


DIGIT_MAP = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
      
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr )
        #return -1
        raise

