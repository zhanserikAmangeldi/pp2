def f():
    yield 1
    yield 2
    yield 3

# two way for print

for i in f():
    print(i)

# or

g = f()

print(next(g))
print(next(g))
print(next(g))