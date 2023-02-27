import re
text = "BlueHeadGreen"
pattern1 = r'ab{0,}'

pattern2 = r'ab{2,3}'

pattern3 = r'[a-z]{1,}_[a-z]{1,}'

pattern4 = r'[A-Z][a-z]{0,}'

pattern5 = r'a.*b'

pattern6 = re.sub(r'[\s,.]', ':', text) 
# x = re.findall(pattern5, text)

def pattern7(s:str):
    t = re.findall(r'_[a-z]', s)
    for i in t:
        temp = s.index(i)
        temp2 = s[temp+1]
        s = re.sub(r'_[a-z]', f'{temp2.capitalize()}',s)
    return s

def pattern8(s:str):
    t = re.findall(r'[A-Z]', s)
    list = []
    for i in t:
        temp = s.index(i)
        if(temp == 0):
            continue
        temp2 = s[temp]
        s = s.replace(i, f' {temp2}')     
    return re.split(r' ', s)

print(pattern8(text))


def pattern9(s:str):
    t = re.findall(r'[A-Z]', s)
    for i in t:

        temp = s.index(i)
        if(temp == 0):
            continue
        temp2 = s[temp]
        s = s.replace(i, f' {temp2}')     
    return s


