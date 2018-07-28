#creating a class Dog
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name +" is sitting.")

    def roll(self):
        print(self.name+" is rolling.")

#Making an instance from a class
my_dog=Dog('Tom',5)

print("My dog's name is "+my_dog.name+" and age is "+str(my_dog.age))
my_dog.sit()
my_dog.roll()
