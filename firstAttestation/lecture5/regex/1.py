import re

text = input()

pattern = "[0-9]+"
pattern1 = "\d"

x = re.search(pattern, text)
x1 = re.search(pattern1, text)
print(x.group(), x1)
