import math


class strings:
    def getString(self):
        self.string = input()
    def printString(self):
        return self.string.upper()


class Shape:
    def __init__(self, length):
        self.length = length
        self.area = 0
    def getarea(self):
        return self.area

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width
    def calculatearea(self):
        self.area = self.length * self.width

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, point):
        dist = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return dist

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, depo):
        self.balance += depo

    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
        else:
            print("Error : Withdraw > balance")

number = [x for x in range(1000)]
prime = lambda x: False if x == 0 or x == 1 else all(x % y != 0 for y in range(2, x) )
number = list(filter(prime, number))
print(number)

print(all([0]))









# first = Account('zhanserik', 1000)
# first.deposit(1000)
# first.withdraw(2001)
# print(first.balance)
# point1 = point(0, 0)
# poin2 = point(3,4)
# point1.dist(poin2)
# r1 = Rectangle(15, 4)
#
# r1.calculatearea()
# print(r1.getarea())
#
# s1 = Square(16)
# print(s1.getarea())

# stringer = strings()
# stringer.getString()
# print(stringer.printString())