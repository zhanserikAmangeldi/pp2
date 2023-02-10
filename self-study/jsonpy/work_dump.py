import json

x = {
    "Car": ["mercedes", "bmw"],
    "age": [1998, 1997],
    "owner": None
}

with open("checkdump.json", 'w') as write_file:
    json.dump(x, write_file)
