class Point():
    """Representing a 2D point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


def reflect_x(p):
    p.x = p.x
    p.y = -p.y
    return p


def main():
    p1 = Point()
    p1.x = 3
    p1.y = 5
    print(reflect_x(p1))


main()
