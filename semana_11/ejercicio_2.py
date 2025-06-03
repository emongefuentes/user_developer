class Person:
    pass

class Bus:
    maximum_passengers = 5
    counter = 0
    
    def get_in_the_bus(self):
        if self.counter < self.maximum_passengers:
            self.counter += 1
            print(f"Current amount of passengers is {self.counter}")
        else:
            print("The bus is full, wait in the line. ")    
        
    def get_off_the_bus(self):
        if self.counter > 0:
            self.counter -= 1
            print(f"Current amount of passengers is {self.counter}")
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
                print(f"Current passengers {self.counter}/5")
            if option == 2: 
                self.get_off_the_bus()
                print(f"Current passengers {self.counter}/5")
            if option == 3:
                break       
            
my_bus_program = Bus()
my_bus_program.menu()
            