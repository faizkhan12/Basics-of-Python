""" A class that can be used to represent a car."""
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0

    def describ(self):
        print(self.make +" "+ self.model+" "+ str(self.year))

    def read_odometer(self):
        print("This car has "+str(self.odometer)+" miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer=mileage
        else:
            print("You cant roll back")

    def increament_odometer(self,miles):
        self.odometer+=miles

class Battery():
    """A class that is used to attempt a battery model"""
    def __init__(self,battery_size=60):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size))

    
    def get_range(self):
        if self.battery_size==70:
            range=240

        elif self.battery_size==85:
            range=270

        print("This car can go" +str(range)+" miles.")


class ElicticCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
