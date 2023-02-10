import json

with open("checkdump.json", "r") as read_file:
    jsonfile = json.load(read_file)

print(jsonfile, "\nits type: ", type(jsonfile))