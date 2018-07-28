#Modifying an Attribute's value directly

#class Car():
 #   def __init__(self,model,make):
  #      self.model=model
   #     self.make=make
    #    self.odometer_reading=0

    #def descrip(self):
    #    print("model of car is "+self.model+ " and make is "+self.make)
        
   # def read_odometer(self):
    #     print("This car has " + str(self.odometer_reading) + " miles on it.")
         
#my_car=Car('Audi','a4')
#my_car.descrip()
#my_car.odometer_reading=21  
#my_car.read_odometer()

#Modifying an Attribute's value through a Method

#class Car():
    #def __init__(self,model,make):
       # self.model=model
      #  self.make=make
     #   self.odometer_reading=20

    #def descrip(self):
     #   print("model of car is "+self.model+ " and make is "+self.make)
        
    #def read_odometer(self):
     #    print("This car has " + str(self.odometer_reading) + " miles on it.")
    #def update_odometer(self,mileage):
    #    if mileage>=self.odometer_reading:
   #         self.odometer_reading=mileage
  #      else:
 #           print("No")

#my_car=Car('Audi','a4')
#my_car.descrip()
#my_car.update_odometer(21)
#my_car.read_odometer()

#Modifying an Attribut's value through increament

class Car():
    def __init__(self,model,make):
        self.model=model
        self.make=make
        self.odometer=20

    def descrip(self):
        print("model of car is "+self.model+" and make is "+self.make)

    def read_odometer(self):
        print("This car has "+str(self.odometer)+" miles on it.")

    def update_odometer(self,mileage):
        self.odometer=mileage
    
    def increament_odometer(self,miles):
        self.odometer+=miles

my_car=Car('Audi','a4')
my_car.descrip()
my_car.update_odometer(2500)
my_car.read_odometer()
my_car.increament_odometer(500)
my_car.read_odometer()

        
