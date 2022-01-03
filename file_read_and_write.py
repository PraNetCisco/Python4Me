performances = {'Ventriloquism':       '9:00am', 
                'Snake Charmer':       '12:00pm', 
                'Amazing Acrobatics':  '2:00pm', 
                'Enchanted Elephants': '5:00pm'}

schedule_file = open('schedule.txt', 'w')

for key, val in performances.items():
    # input to write function is concatenated because it only takes 
    # one value at a time
    schedule_file.write(key + '-' + val + '\n')

schedule_file.close()

### Reading a file

schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    print(line)

schedule_file.close()

performances_new = {}
performances_stripped = {}
schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.split('-')
    performances_new[show] = time
    performances_stripped[show] = time.strip()

schedule_file.close() 

### Adding new entry to file schedule.txt
schedule_file = open('schedule.txt', 'a')
schedule_file.write('Sholay' + '-' + '3:00pm')
schedule_file.close()

print (performances_new, '\n')
print (performances_stripped)