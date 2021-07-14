import sys
import json

jname = sys.argv[1] # example.json
jpath = sys.argv[2] # 'members[0].name'

jpath = jpath.split('.')

with open(jname, "r") as read_file:
    pjson = json.load(read_file)

atr_path = []

for atr in jpath:
    if ']' in atr:
        atr_path.append(atr[:-3])
        atr_path.append(int(atr[-2:-1]))
        
    else:
        atr_path.append(atr)

try:

    for atr in atr_path:
        pjson = pjson[atr]
    print(pjson)

except KeyError:
    print('The path is not correct')
    sys.exit(1)


