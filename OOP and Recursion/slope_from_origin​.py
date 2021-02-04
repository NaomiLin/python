class Point():
    """Representing a 2D point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


def slope_from_origin(p):
    slope = p.y / p.x
    return slope


def main():
    p1 = Point()
    p1.x = 4
    p1.y = 10
    print(slope_from_origin(p1))


main()
