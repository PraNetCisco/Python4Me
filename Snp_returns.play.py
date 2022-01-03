import sys
import json

file = open ('SnP_returns.json')

data = json.load(file)

for i in data['snpreturns']:
    #print (i)
    print (i['year'], ":", i['totalReturn'])
    
file.close()


