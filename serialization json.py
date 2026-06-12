import json

L=[1,2,3,4,5]

with open('demo.json','w') as f:
    json.dump(L,f)