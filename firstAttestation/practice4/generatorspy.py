def square(n:int):
    for i in range(n):
        yield i*i
def onlyeven(n:int):
    for i in range(n):
        if i % 2 == 0:
            yield i

def divisable(n):
    for i in range(n):
        if i % 3 ==0 and i % 4 == 0:
            yield i

def squares(a, b):
    for i in range(a, b):
        yield i * i
n = 4
return_N_to_Zero = (x for x in range(n, 0, -1))



print(list(return_N_to_Zero))