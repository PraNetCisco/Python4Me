def average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    
    avg = total/len(numbers)
    return avg


def main ():
    numbers = [1, 2, 3,4,5]
    my_average = average(numbers)
    print(my_average)

main ()
