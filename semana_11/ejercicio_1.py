import math
class Circle:
    def __init__(self):
        self.radius = int(input("Insert the circle's radius: "))
    
    def circle_area_method(self):
        return (self.radius**2)* math.pi
    
my_circle = Circle()
area = my_circle.circle_area_method()

print(f"The are of the circle iss : {area}")

