class VirtualPet:
    """a representation of a pet"""
    
    #constructor - run when ever a new instance is created
    def __init__ (self, name):
        self.name = name
        print("I have been born - my name is {0}!".format(self.name))
        self.hunger = 5
        self.energy = 5
        self.thirst = 5
        self.dirty = 5
        
    #method
    def born(self):
        print("Hi, I'm your virtual pet!")

    def feed(self, food):
        self.hunger = self.hunger - 1
        self.energy = self.energy + 1

    def drink(self):
        self.thrist = self.thirst - 1
        # self.energy = self.energy + 1

    def wash(self):
        self.was = self.wash - 1

def welcome():
    print('========== Hello, welcome to the virtual pet game ==========')
    print('')
    name = input("Please enter a name for your pet: ")
    pet_one = VirtualPet(name) #creates and instance from the class
    pet_one.born() #calls talk method
    return pet_one

def menu():
    print('===== MENU =====')
    print('')
    print('')

def main():
    pet_one = welcome()
    print("my energy is {0}".format(pet_one.energy))
    pet_one.feed("Cake")
    print("My energy is now {0}".format(pet_one.energy))

if __name__ == "__main__":
    main()
