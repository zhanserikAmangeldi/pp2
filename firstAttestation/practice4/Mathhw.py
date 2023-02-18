import math


def degreeToRadian(degree):
    return (degree * math.pi) / 180

def areaOfTrapezoid(height, firstBase, secondBase):
    return (firstBase + secondBase) / 2 * height

def areaOfRegularPolygon(lenght, sides):
    return (lenght*sides) * (lenght/(2*math.tan(degreeToRadian(180/sides)))) / 2

def areaOfParallelogram(lenght, height):
    return lenght * height
print(areaOfRegularPolygon(10, 6))
