class Car():
    def __init__(self,make,model,year,gas_tank):
        self.make=make
        self.model=model
        self.year=year
        self.gas_tank=gas_tank
        self.odometer=0
        

    def descrip(self):
        print(self.make+' ' +self.model+' ' +str(self.year))
    def fill_gas_tank(self):
        print("This car need "+self.gas_tank)

    def read_odometer(self):
        print("This car has "+str(self.odometer))

    def update_odometer(self,mileage):
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print("you can't roll back")

    def increment_odometer(self,miles):
        self.odometer+=miles

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"KWh battery.")

    def get_range(self):
        if self.battery_size==70:
            Range=200
        elif self.battery_size==80:
            Range=240
        print("This car can go "+str(Range)+" miles.")


class ElictriCar(Car):
    def __init__(self,make,model,year,gas_tank):
        super().__init__(make,model,year,gas_tank)
        self.battery=Battery()

    def fill_gas_tank(self):
        print("This car does not need")

    

myCar=ElictriCar('Tesla','a4',2016,'gas')
myCar.descrip()
myCar.battery.describe_battery()
myCar.fill_gas_tank()
myCar.battery.get_range()
                                        
