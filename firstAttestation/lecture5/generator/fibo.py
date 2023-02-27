def f(n):
    a, b = 0 , 1
    cnt = 2
    while cnt < n:
        yield b
        a, b = b, a + b
        cnt += 1


for i in f(50):
    print(i)