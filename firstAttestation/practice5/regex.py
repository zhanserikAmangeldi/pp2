import re
text = "blueHeadGreen"
pattern1 = r'ab{0,}'

pattern2 = r'ab{2,3}'

pattern3 = r'[a-z]{1,}_[a-z]{1,}'

pattern4 = r'[A-Z][a-z]{0,}'

pattern5 = r'a.*b'

pattern6 = re.sub(r'[\s,.]', ':', text) 
# x = re.findall(pattern5, text)

def p7(text):
    return text.group("snake") + text.group("camel").capitalize()
pattern7 = r'(?P<snake>[a-z]+)(?P<camel>_[a-z])'
# print(re.sub(pattern7, p7, text))

pattern8 = r'[A-Z][a-z]*'

# print(re.findall(pattern8, text))



def p9(s:str):
    return s.group("before") + " " + s.group("after")
pattern9 = r'(?P<before>[a-z]+)(?P<after>[A-Z].)'
# print(re.sub(pattern9, p9, text))

def p10(s:str):
    return s.group("before") + "_" + s.group("snake").lower()

pattern10 = r'(?P<before>[a-z]+)(?P<snake>[A-Z])'

# print(re.sub(pattern10, p10, text))
pattern_name = r'[a-zA-Z]+'
pattern_phone = r'[0-9]+'
print(re.findall(pattern_phone, 'Zhanserik, 8705-4578237'))

# print(pattern10(text))