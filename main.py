import json
from pprint import pprint
with open('input.json') as f:
    data = json.load(f)

target = open('trans.txt', 'w')
for val in data.values():
    #print(val)
    target.write(val)
    target.write("\n")

target.close()
