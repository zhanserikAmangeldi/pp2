import json

x = '{ "name":"Jhon", "age":30, "city":"New York" }'


# convertor json to py
y = json.loads(x)

print(y["name"])




x = {
    "name": "Jhon",
    "age": 30,
    "city": "New York"
}


# convertor py to json
y = json.dumps(x)

print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "Jhon",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy", "AMelia"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg":24.1}
    ]
}

print(json.dumps(x))

# indent - отступы
print(json.dumps(x, indent=4))

print(json.dumps(x, indent=4, separators=(". ", " = "))) # first change , to . second : to =

print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)) # do not sort nested objects

