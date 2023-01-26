def ex1():
    x = "Hello World"
    print(len(x))

def ex2():
    txt = "Hello World"
    x = txt[0]
    print(x)

def ex3():
    txt = "Hello World"
    x = txt[2:5]
    print(x)

def ex4():
    txt = " Hello World "
    x = txt.strip()
    print(x)

def ex5():
    txt = "Hello World"
    txt = txt.upper()
    print(txt)

def ex6():
    txt = "Hello World"
    txt = txt.lower()
    print(txt)

def ex7():
    txt = "Hello World"
    txt = txt.replace("H", "J")
    print(txt)

def ex8():
    age = 36
    txt = "My name is John, and I am {}"
    print(txt.format(age))

ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()