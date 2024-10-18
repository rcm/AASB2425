import math

class RegularPolygon:
    def __init__(self, num, size):
        self.num = num
        self.size = size
    def __repr__(self):
        return f"RegularPolygon(number of sizes = {self.num} sizes = {self.size})"
    def perimeter(self):
        return self.num * self.size

class EquilateralTriangle(RegularPolygon):
    def __init__(self, size):
        super().__init__(3, size)
    def __repr__(self):
        return f"EquilateralTriangle(sizes = {self.size})"
    def area(self):
        return math.sqrt(3) * self.size / 8 

