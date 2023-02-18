thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


# get the keys
for x in thisdict:
    print(x)

for x in thisdict.keys():
    print(x)



# get the values

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)


# get both

for x, y in thisdict.items():
    print(x, y)
