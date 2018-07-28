currentUsers=['faiz','khan','mark','ross','sofie']
newUsers=['rachel','faiz','khan','joe','eric']
for newUser in newUsers:
    if newUser in currentUsers:
        print(newUser+" will have to enter a new username.")
    else:
        print(newUser+" is available.")
    
