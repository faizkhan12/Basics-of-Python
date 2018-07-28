class Restaurant():      #making a class
    #defining  methods
    
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine

    def describe_restaurant(self):
        print(self.name +" is name of the restaurant.")
        print(self.name +" is famous for this "+self.cuisine+" food.")

    def open_restaurant(self):
        print(self.name+" is now open.")



