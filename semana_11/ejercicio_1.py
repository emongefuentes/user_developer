import math
class Circle:
    radius = int(input("Insert the circle's radius: "))
    
    def circle_area_method(self):
        print((self.radius**2)* math.pi)
        
    
my_circle = Circle()
my_circle.circle_area_method()

