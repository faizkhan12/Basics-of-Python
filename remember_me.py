#import json
#username=input("What is your name?")
#filename='username.json'
#with open(filename,'w') as file_object:
 #   json.dump(username,file_object)
  #  print("See you soon, "+username)

#REFACTORING
#import json
#def get_stored_username():
 #   """Greet the stored user by name"""
  #  filename='username.json'
   # try:
    #    with open(filename)as file_object:
     #       username=json.load(file_object)
    #except FileNotFoundError:
     #   return None #if the filename 'username' does not exist it will return None
    #else:
     #   return username
#def greet_user():
 #   """Greet the user with name"""
  #  username=get_stored_username()
   # if username:
    #    print("Welcome back, "+username)
    #else:  #if there is no response before 
     #   username=input("What is your name?")
      #  filename='username.json'
       # with open(filename,'w')as file_object:
        #    json.dump(username,file_object)
        #    print("We wil remember you, "+username)
#greet_user()

 #ANOTHER VERSION
import json
def get_stored_username():
    """Greet the user name which is already exist"""
    filename='username.json'
    try:
        with open(filename)as file_object:
            username=json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """It stores the new username if it is not exist"""
    username=input("What is your name?")
    filename='username.json'
    with open(filename,'w')as file_object:
        json.dump(username,file_object)
    return username

def greet_user():
    """Greet user by name"""
    username=get_stored_username()
    if username:
        correct=input("Are you "+username+"?(y/n)")
        if correct=='y':
            print("Welcome back "+username)
            return
        else:
            username=get_new_username()
            print("We will remember you next time "+username)
    else:
        username=get_new_username()
        print("We will remeber you next time, "+username)
greet_user()
