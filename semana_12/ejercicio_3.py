class Animal:
    pass

class Land(Animal):
    def walk(self, name):
        print(f"A/an {name} is an aquatic animal ")

class Water(Animal):
    def swim(self, name):
        print(f"A/an {name} is an aquatic animal.")
        
class Amphibian (Land, Water):
    pass
#esto es herencia normal
new_animal = Land()
new_animal.walk('elefant')

new_animal_2 = Water()
new_animal_2.swim('salmon')
# y este es el ejemplo de herencia multiple, 
#la idea en si, es que una clase pueda heredar de 2 clases, por eso coloqué el ejmeplo
#de un animal que se mueva en dos tipos de terreno, acuatico y terrestre.
new_animal_3 = Amphibian()
new_animal_3.swim('salamander')
new_animal_3.walk('salamander')