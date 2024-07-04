# to find area and perimeters of the circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # find the area 
    def area(self):
        return (22/7) * self.radius ** 2

    # find the perimeter 
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)

print(c1.area())
print(c1.perimeter())