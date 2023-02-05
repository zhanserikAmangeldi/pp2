# lambda arg : expression
x = lambda a : a + 10
print(x(5))

x = lambda a , b , c : a + b + c
print(x(5, 10, 20))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

print(myfunc(5)(10)) # first is n, second is 10
