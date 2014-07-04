from Vehical import *

class RaceCar(Vehicle):

    #constructor
    def __init__(self,driver,boost_energy,race_number):
        super().__init__(5,120,2,6,2,driver)
        #private
        self._boost_energy = boost_energy

        #public
        self.race_number = race_number

    def accelerate(self):
        if self._speed < 30:
            self._speed += self._acceleration
        elif self._speed >= 30 and self._speed <= self._top_speed:
            self._speed += self._acceleration * 1.2
        elif self._speed < self._top_speed:
            self._speed += self._acceleration * 0.9
        if self._speed > self._top_speed:
            self._speed = self._top_speed

    def braking(self):
        recovered_energy = (self._speed - (self._speed - self._braking)) * 0.1
        self._speed = self._speed - self._braking
        self._boost_energy += recovered_energy
        return self._boost_energy

    def boost(self):
        if self._boost_energy > 5:
            self._boost_energy -= 0.1
            self._speed += 10

#test program
def main():
    driver = input("Please enter your name: ")
    print()
    boost_energy = int(input("Please enter a boost value (1-10): "))
    print()
    race_number = int(input("Please enter a car number (1-12): "))
    print()
    race_car_one = RaceCar(driver, boost_energy, race_number)
    print()
    print("Driver: {0}, Car number: {1}, Speed is: {2}, Boost energy level is :{3}, Top speed is:{4}, Braking is: {5}, Acceleration is: {6}, Fuel is {7}".format(race_car_one.driver, race_car_one.race_number, race_car_one._speed, race_car_one._boost_energy, race_car_one._top_speed, race_car_one._braking, race_car_one._acceleration, race_car_one._fuel))
    print()
    print("Accelerating...")
    race_car_one.accelerate()
    print("New speed is: {0}, Boost energy level is :{1}, Top speed is:{2}, Braking is: {3}, Acceleration is: {4}, Fuel is {5}".format(race_car_one._speed, race_car_one._boost_energy, race_car_one._top_speed, race_car_one._braking, race_car_one._acceleration, race_car_one._fuel))
    print()
    print("Braking...")
    race_car_one.braking()
    print("New speed is: {0}, Boost energy level is :{1}, Top speed is:{2}, Braking is: {3}, Acceleration is: {4}, Fuel is {5}".format(race_car_one._speed, race_car_one._boost_energy, race_car_one._top_speed, race_car_one._braking, race_car_one._acceleration, race_car_one._fuel))
    print()
    print("Boost...")
    race_car_one.boost()
    print("New speed is: {0}, Boost energy level is :{1}, Top speed is:{2}, Braking is: {3}, Acceleration is: {4}, Fuel is {5}".format(race_car_one._speed, race_car_one._boost_energy, race_car_one._top_speed, race_car_one._braking, race_car_one._acceleration, race_car_one._fuel))
    print()
    amount = int(input("Please enter an amount of fuel(1-10): "))
    race_car_one.add_fuel(amount)

if __name__ == "__main__":
    main()
