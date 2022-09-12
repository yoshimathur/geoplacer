from mimetypes import init
import random
import math

#classes
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
        if points == None: 
            self.points = []
            self.centroid = Point(0, 0)
        else: 
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
        oldCentroid = self.centroid
        sumX = oldCentroid * len(self.points)
        sumY = oldCentroid * len(self.points)

        self.points.append(point)
        sumX = sumX + point.x 
        sumY = sumY + point.y

        centroid = Point(sumX / i, sumY / i)
        self.centroid = centroid

class orgNode: 
    def __init__(self, point, top, down):
        self.point = point
        self.top = top
        self.down = down
    
    def setTop(self, top):
        self.top = top

    def setDown(self, down):
        self.down = down

# variables and constants
limit = 5
points = 10
space = [[Point(None, None) for x in range(limit)] for y in range(limit)]

test = Shape([Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 2), Point(2, 2), Point(2, 1), Point(2, 0), Point (1, 0)])

# point functions
def plotPoint(x, y):
    point = Point(x, y)
    space[y][x] = point

#shape functions
def orderPointsVertical(current, point):
    print("--current--")
    print(current)
    while True: 
        if current.down == None:
            if point.y < current.point.y:
                newNode = orgNode(point, current, None)
                current.setDown(newNode)
                return None
            elif point.y > current.point.y:
                newNode = orgNode(point, None, current)
                current.setTop(newNode)
                return newNode
            else: 
                print("Fatal Error: Repeated point ignored in organization!")
                return None
        else: 
            if point.y < current.point.y:
                orderPointsVertical(current.down, point)
            elif point.y > current.point.y:
                currentTop = current.top
                newNode = orgNode(point, currentTop, current)
                if currentTop != None: 
                    currentTop.setDown(newNode)
                    return None
                else:
                    return newNode
            else: 
                print("Fatal Error: Repeated point ignored in organization!")
                return None

def orderPointsLeft(shape):
    org = [None] * limit

    for point in shape.points: 
        i = point.x 
        print("--position--")
        print(i)
        current = org[i]
        if current == None: 
            print("Adding")
            org[i] = orgNode(point, None, None)
        else:
            print("Sorting")
            topNode = orderPointsVertical(current, point)
            print("--topNode--")
            print(topNode)
            if topNode != None: 
                org[i] = topNode


def orderPointsRight(shape):
    print("Filler")

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
orderPointsLeft(Shape(initial))