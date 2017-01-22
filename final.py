import json
from pprint import pprint
with open('input.json', 'r+') as f:
    data = json.load(f)

target = open('aftertrans.txt', 'r')
output = open('transjson.json', 'w')
output.write(str('{\n'))
for key, value in data.items():
    for n in target:
        data[key] = n
        break
    #print  key, data[key],
    output.write(str('"') + str(key) + str('": ') + str('"') + str(data[key].rstrip() + '"' + ',\n'))

output.write(str('\n}'))
target.close()
output.close()
