import random

# random.random generates random betweem [0.0, 1.0]
r1 = random.random()

# random.choice generates random choice from given list
r2 = random.choice([1,2,3,4,5,6])

# random.randintgenerates random integer from the given range
r3 = random.randint(1, 1000)

print ("random.random is ", r1, "random.choice is", r2, "random int is", r3)
