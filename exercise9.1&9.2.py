#9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.
#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each instance.

#      Author's name : Faiz Khan

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

    #making 3 instance
my_restaurant=Restaurant('Tai Hotel','Thai')
my_restaurant1=Restaurant('Valyaka','Turkey chicken')
my_restaurant2=Restaurant('Shambhu','Paneer')

print(my_restaurant.name)
print(my_restaurant.cuisine)
my_restaurant.describe_restaurant()

print("\n"+my_restaurant1.name)
print(my_restaurant1.cuisine)
my_restaurant1.describe_restaurant()

print("\n"+my_restaurant2.name)
print(my_restaurant2.cuisine)
my_restaurant2.describe_restaurant()
