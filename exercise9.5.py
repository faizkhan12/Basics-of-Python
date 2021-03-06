class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
        
    def describe_user(self):
        self.full_name=self.first_name+ ' '+self.last_name
        print(self.full_name+": first name is "+self.first_name+" and last name is "+self.last_name)

    def greet_user(self):
        print("Hello "+self.full_name)

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

myUser=User('Faiz','Khan')
print(myUser)
myUser.describe_user()

print("\nMaking 3 login attempts")
myUser.increment_login_attempts()
myUser.increment_login_attempts()
myUser.increment_login_attempts()
print("Login attempts: "+str(myUser.login_attempts))
print("\nResetting logic attempt")
myUser.reset_login_attempts()
print("Login attempts: "+str(myUser.login_attempts))
