class person:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def __str__(self):
        return (f"{self.name} {self.age} {self.gpa}")

    def hello(self):
        return "Hello, my name is " + self.name


    x = 5


p1 = person("Zhanserik", 17, 3.42)
print(p1.name, p1.age, p1.gpa)
print("-----------------")
print(p1)

print(p1.hello())


del p1.age # we delete age

print(p1.age)


