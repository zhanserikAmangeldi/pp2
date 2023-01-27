x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

def ex1():
    carname = "Volvo"
    print(carname)

def ex2():
    x = 50
    print(x)

def ex3():
    x = 5
    y = 10
    print(x + y)

def ex4():
    x = 5
    y = 10
    z = x + y
    print(z)

def ex5():
    myfirst_name = "John"

def ex6():
    x = y = z = "Oranges"
    print(x, y, z)

def myfunc():
    global x
    x = "fantastic"

ex1()
ex2()
ex3()
ex4()
ex5()
ex6()

myfunc()
print(x)
