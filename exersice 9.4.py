

#      Author's name : Faiz Khan

"""making class"""
class Restaurant():
    
    #defining  methods
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
        self.number_served=0

    def describ(self):
        print(self.name +" is name of the restaurant.")
        print(self.name +" is famous for this "+self.cuisine+" food.")

    def read_number_served(self):
        print("Number of customers that restaurant have served is "+str(self.number_served))
        
    #Adding a new methd to update value of 'number_served'
    def set_number_served(self,number):
        self.number_served=number

    def increment_number_served(self,day):
        self.number_served+=day
        
restaurant=Restaurant('Taj','paneer')
restaurant.describ()

restaurant.set_number_served(20)
restaurant.read_number_served()

restaurant.increment_number_served(10)
restaurant.read_number_served()
                        
