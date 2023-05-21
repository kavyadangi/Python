class Point:
    def __init__(a, x, y):
        a.x = x
        a.y = y
    def __str__(a):
        return f'({a.x}, {a.y})'
    def __add__(a, o):
        if isinstance(o, Point):
            return Point(a.x + o.x, a.y + o.y)
        else:
            raise TypeError("Addition not supported for the given type.")
P1 = Point(10, 20)
P2 = Point(12, 15)
P3 = P1 + P2
print(f'P1: {P1}')
print(f'P2: {P2}')
print(f'P3: {P3}')
