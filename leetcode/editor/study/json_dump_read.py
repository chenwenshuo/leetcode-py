import json

number = [1, 2, 3, 4, 5]
with open('json_text.json', 'w') as j:
    json.dump(number, j)

with open('json_text.json') as j:
    print(json.load( j))
