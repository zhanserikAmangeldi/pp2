import json

x = {
    "name": "Zhanserik",
    "age": 17,
    "city": "Almaty"
}

y = json.dumps(x)

print(y)

y = json.dumps(x, indent=4, separators=(". ", " = "))

print(y)