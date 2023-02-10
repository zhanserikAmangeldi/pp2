import json

a = ("one", "two")
print(a, "\nits type: ", type(a))

b = json.dumps(a)
print(b, "\nits type: ", type(json.loads(b)))