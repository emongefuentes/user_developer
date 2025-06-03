import math
from abc import ABC, abstractmethod

class Shape(ABC):
    

    @abstractmethod
    def calculate_perimeter (self):
        #todas las figuras pueden calcular Perimetro
        #pero de diferentes formas
        pass
    
    @abstractmethod
    def calculate_area (self):
        #todas las figuras pueden calcular Area 
        #pero de diferentes formas
        pass
    
class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio 
    
    def calculate_perimeter(self):   
        result = 2 * math.pi * self.radio
        print(f"perimeter: {result:.2f}")
    
    def calculate_area(self):
        result = math.pi * ( self.radio ** 2 )
        print(f"Area: {result:.2f}")
               
        
class Square(Shape):
    def __init__(self, lado):
        self.lado = lado
        
    def calculate_perimeter(self):
        result = self.lado * 4 
        print(f"perimeter: {result}")
        
    def calculate_area(self):
        result = self.lado * self.lado
        print(f"Area: {result}") 

class Rectangle(Shape):
    def __init__(self, lado, ancho):
        self.lado = lado
        self.ancho = ancho
    
    
    def calculate_perimeter(self):
        result = 2 * (self.lado + self.ancho)
        print(f"perimeter: {result}") 
        
    def calculate_area(self):
        result = self.lado * self.ancho
        print(f"Area: {result}")  
               
print("_____Circulo")        
my_calcu = Circle(25)
my_calcu.calculate_perimeter()
my_calcu.calculate_area()

print("_____Cuadrado")  
my_calcu = Square(25)
my_calcu.calculate_perimeter()
my_calcu.calculate_area() 
 
print("_____Rectangulo")  
my_calcu = Rectangle(25, 50) 
my_calcu.calculate_perimeter() 
my_calcu.calculate_area()      