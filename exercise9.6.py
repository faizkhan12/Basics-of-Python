class Restaurant():      #making a class
    #defining  methods
    
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine

    def describe_restaurant(self):
        print(self.name +" is name of the restaurant.")
        print(self.name +" is famous for this "+self.cuisine+" food.")

    def open_restaurant(self):
        print(name+" is now open.")


class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine):
        super().__init__(name,cuisine)
        self.flavours=['vanilla','chocalate']

    def describe_flavours(self):
        print("This restaurant has " +str(self.flavours))

my_restaurant=IceCreamStand('Taj','Paneer')
my_restaurant.describe_restaurant()
my_restaurant.describe_flavours()
