#passing a list

def greetUsers(names):
    for name in names:
        message="Hello "+name+"!"
        print(message)
people=['Faiz','Khan','Sheldon']
greetUsers(people)
