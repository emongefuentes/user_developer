import math
from abc import ABC, abstractclassmethod

class Shape(ABC):
    pass

    @abstractclassmethod
    def calculate_perimeter ():
        pass
    
    def calculate_area ():
        pass
    
class Circle(Shape):
    def calculate_perimeter(self, radio):   
        result = 2 * math.pi * radio
        print(f"perimeter: {result}")
    
    def calculate_area(self, radio):
        result = math.pi * ( radio ** 2 )
        print(f"Area: {result}")
               
        
class Square(Shape):
    def calculate_perimeter(self, lado):
        result = lado * 4 
        print(f"perimeter: {result}")
        
    def calculate_area(self, lado):
        result = lado * lado
        print(f"Area: {result}") 

class Rectangle(Shape):
    def calculate_perimeter(self, lado, ancho):
        result = 2 * (lado + ancho)
        print(f"perimeter: {result}") 
        
    def calculate_area(self, lado, ancho):
        result = lado * ancho
        print(f"Area: {result}")         
print("_____Circulo")        
my_calcu = Circle()
my_calcu.calculate_perimeter(25)
my_calcu.calculate_area(25)
print("_____Cuadrado")  
my_calcu = Square()
my_calcu.calculate_perimeter(25)
my_calcu.calculate_area(25)  
print("_____Rectangulo")  
my_calcu = Rectangle() 
my_calcu.calculate_perimeter(25,50) 
my_calcu.calculate_area(20,50)      