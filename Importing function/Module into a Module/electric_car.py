from car import Car
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"KWh battery.")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    

