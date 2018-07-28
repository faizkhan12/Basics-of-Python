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

class Privileges():
    def __init__(self,privileges=[]):
        self.privileges =['can reset passwrd','can suspend accunts']

    def show_privileges(self):
        print("\nAdmin has follwing privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)
        else:
            print("This user has no privileges")

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=Privileges()
