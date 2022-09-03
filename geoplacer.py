import random
import math

class Point:
    def __init__(self, x, y):
        if x == None:
            self.x = None
        else:
            self.x = x

        if y == None:
            self.y = None
        else:
            self.y = y

    def distanceFrom(self, point):
        xdistance = abs(point.x - self.x)
        ydistance = abs(point.y - self.y)
        diff = math.pow(xdistance, 2) - math.pow(ydistance, 2)
        dist = math.sqrt(diff)

        return dist

class Shape:
    def __init__(self, points):
        self.points = points

        sumX = 0
        sumY = 0
        i = len(self.points)
        for point in points:
            sumX = sumX + point.x
            sumY = sumY + point.y

        centroid = Point(sumX / i, sumY / i)
        self.centroid = centroid

    def addPoint(self, point):
        self.points.append(point)

# variables and constants
limit = 5
points = 3
space = [[Point(None, None) for x in range(limit)] for y in range(limit)]

test = Shape([Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 2), Point(2, 2), Point(2, 1), Point(2, 0), Point (1, 0)])

# point functions
def plotPoint(x, y):
    point = Point(x, y);
    space[y][x] = point;

#display
def printShape(shape):
    print("\n")

    global space
    space = [[Point(None, None) for x in range(limit)] for y in range(limit)]

    for point in shape.points:
        plotPoint(point.x, point.y)

    for subspace in space[::-1]:
        for point in subspace:
            if point.x == None and point.y == None:
                print("·", end="    ")
            else:
                print("●", end="    ")
        print("\n")
    print(f"Centroid: ({shape.centroid.x}, {shape.centroid.y})")
    print("\n")

# main
initial = []
for i in range(points):
    x = random.randint(0, limit - 1)
    y = random.randint(0, limit - 1)
    initial.append(Point(x, y))

printShape(Shape(initial))
printShape(test)
