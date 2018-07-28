#9-3. Users: Make a class called User. Create two attributes called first_name
#  and last_name, and then create several other attributes that are typically stored
#  in a user profile. Make a method called describe_user() that prints a summary
#  of the user’s information. Make another method called greet_user() that prints
#  a personalized greeting to the user.
#  Create several instances representing different users, and call both methods
#  for each user.

#           Author name: Faiz Khan

class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def describe_user(self):
        self.full_name=self.first_name+ ' '+self.last_name
        print(self.full_name+": first name is "+self.first_name+" and last name is "+self.last_name)

    def greet_user(self):
        print("Hello "+self.full_name)

my_users=User('Faiz','Khan')
print(my_users.first_name)
print(my_users.last_name)
my_users.describe_user()
my_users.greet_user()
