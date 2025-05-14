class Animal :
    def __init__(self,habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(f"Animal habitat is {self.habitat}")
    
    def sound (self):
        print("Animal sound")

class Dog (Animal):
    def __init__(self):
        super().__init__("Kennel")
    
    def sound (self):
        print("Dog barks")
class Cat (Animal):

    def __init__(self):
        super().__init__("House")
    
    def sound(self):
        print("Cat meows")