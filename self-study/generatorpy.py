# def gensquares(N):
#     for i in range(N):
#         yield i * i
    
# print(gensquares(5)) # <generator object gensquares at 0x0000027DB98782B0>

# print(next(gensquares(5)))
# print(next(gensquares(5)))
# print(next(gensquares(5)))
# print(next(gensquares(5)))
# print(next(gensquares(5)))

# x = gensquares(4)

# print(x)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# print(next(gensquares(5))
# for i in gensquares(5):
#     print(i)

# x = (x*x for x in range(4))
# print(x)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


x = [1, 2, 3, 4]
xiter = iter(x)

print(next(xiter))

print(next(xiter))
print(next(xiter))
print(next(xiter))
