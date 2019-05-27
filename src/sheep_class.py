from animal_class import *

class Sheep(Animal):
    """A generic Sheep"""

    #constructor
    def __init__(self,name):
        #call parent class constructor with default values for potato
        #growth rate = 1; food need = 3; water need = 6
        super().__init__(name,3,3,2)
        self._type = "Sheep"

    #overriding grow method for subclass
    def grow(self,food,water):
        if food > self._food_need:
            self._weight += self._growth_rate * 1.2
        elif food == self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

def get_name():
    valid = False
    while not valid:
        name = input("Please enter a name for the sheep: ")
        if len(name) > 0:
            valid = True
        else:
            print("Error! You need to enter a name for the sheep")
    return name

def main():
    name = get_name()
    #create a new sheep animal
    new_sheep = Sheep(name)
    #manually grow the animal
    manual_grow(new_sheep)
    print(new_sheep.report())
    manual_grow(new_sheep)
    print(new_sheep.report())

if __name__ == "__main__":
    main()
