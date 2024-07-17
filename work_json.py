import json


with open('data.json', 'r') as file:
    print(file)
    data = json.load(file)
print(data)
name = input('Enter your name')
data['user_name'] = name
with open('data.json', 'w') as file:
    json.dump(data, file, indent = 4)