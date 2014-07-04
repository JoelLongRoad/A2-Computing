class Vehicle():

    #constructor
    def __init__(self,speed,top_speed,braking,acceleration,amount,driver):

        #private
        self._speed = speed
        self._top_speed = top_speed
        self._braking = braking
        self._acceleration = acceleration
        self._fuel = amount

        #public
        self.driver = driver

    def accelerate(self):
        self._speed += self._acceleration
        return self._speed
        
    def braking(self):
        self._speed = self._speed - self._braking
        return self._speed

    def add_fuel(self, amount):
        self._fuel += amount
        return self._fuel

#test program
def main():
    driver = input("Please enter your name: ")
    vehicle_one = Vehicle(5,50,2,6,2,driver)
    print()
    print(vehicle_one.driver, vehicle_one._speed, vehicle_one._top_speed, vehicle_one._braking, vehicle_one._acceleration, vehicle_one._fuel)
    print()
    print("Accelerating...")
    vehicle_one.accelerate()
    print("New speed is: {0}, Top speed is:{1}, Braking is: {2}, Acceleration is: {3}, Fuel is {4}".format(vehicle_one._speed, vehicle_one._top_speed, vehicle_one._braking, vehicle_one._acceleration, vehicle_one._fuel))
    print()
    print("Braking...")
    vehicle_one.braking()
    print("New speed is: {0}, Top speed is:{1}, Braking is: {2}, Acceleration is: {3}, Fuel is {4}".format(vehicle_one._speed, vehicle_one._top_speed, vehicle_one._braking, vehicle_one._acceleration, vehicle_one._fuel))
    print()
    amount = int(input("Please enter an amount of fuel(1-10): "))
    vehicle_one.add_fuel(amount)
    
if __name__ == "__main__":
    main()
