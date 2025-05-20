class Person:
    pass
class Bus:
    def __init__(self):
        self.maximum_passengers = 5
        self.passengers = []
    
    def get_in_the_bus(self):
        if len(self.passengers) < self.maximum_passengers:
            person = Person()
            self.passengers.append(person)
            print(f"A new person is in the bus")
        else:
            print("The bus is full, wait in the line. ")    
        
    def get_off_the_bus(self):
        if self.passengers:
            self.passengers.pop()
            print(f"A person has abandoned the bus")
        else:
            print("The bus is empty... ") 
    
    def menu(self):
        while True:
            option = int(input(("""
                            1. Get in..
                            2. Get off..
                            3. Finish the system
                            ------->  """)))
            
            if option == 1:
                self.get_in_the_bus()
                print(f"Current passengers {len(self.passengers)}/{self.maximum_passengers}")
            if option == 2: 
                self.get_off_the_bus()
                print(f"Current passengers {len(self.passengers)}/{self.maximum_passengers}")
            if option == 3:
                break 
  
my_bus_program = Bus()
my_bus_program.menu()
            