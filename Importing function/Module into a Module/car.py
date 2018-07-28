class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
        

    def descrip(self):
        print(self.make+' ' +self.model+' ' +str(self.year))

    def read_odometer(self):
        print("This car has "+str(self.odometer))

    def update_odometer(self,mileage):
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print("you can't roll back")

    def increment_odometer(self,miles):
        self.odometer+=miles
