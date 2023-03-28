import datetime

def fiveDays():
    return datetime.date.today() - datetime.timedelta(5)

def yestotom():
    return f'Yesterday: {datetime.date.today() - datetime.timedelta(1)}\nToday: {datetime.date.today()}\nTomorrow: {datetime.date.today() + datetime.timedelta(5)}'

def dropMicrosecond(d):
    return d.replace(microsecond=0)

def dif(first, second):
    print(first)
    print(second)
    return abs(first.timestamp() - second.timestamp())
print(fiveDays())
# print(dif(datetime.datetime.now(), datetime.datetime(2020, 5, 6, 13, 52, 5, 208688)))