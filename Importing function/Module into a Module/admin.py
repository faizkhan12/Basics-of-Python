from user import User

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
