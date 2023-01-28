from collections import OrderedDict, namedtuple

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# x, y, z = 0, 0, 0
# Point = OrderedDict()

# Point = namedtuple()

# Point = dict

p1 = Point(x=2, y=3, z=4)


print(type(p1))
print(p1.x)
print(p1.y)
print(p1.z)

Marks = namedtuple('Marks', 'Physics Chemistry Math English')
marks = Marks(90, 85, 95, 100)
print(marks)
# Marks(Physics=90, Chemistry=85, Math=95, English=100)