guestList=['Amit','Prashant','Shad','Basit']
print(guestList)
print("Dear "+guestList[0],"You are invited to my party.")
print("Dear "+guestList[1],"You are invited to my party.")
print("Dear "+guestList[2],"You are invited to my party.")
print("Dear "+guestList[3],"You are invited to my party.")
print("Dear guests,I found a bigger table which can easily accomadate all of you")
guestList.insert(0,'John')
guestList.insert(3,'Micheal')
guestList.append('Heath')
print(guestList)
print("Dear "+guestList[0],"You are invited to my party.")
print("Dear "+guestList[3],"You are invited to my party.")
print("Dear "+guestList[6],"You are invited to my party.")
print("Unfortunately my dining table could not arrive in time so I can have only two people")
poppedGuest=guestList.pop()
print(guestList)
print("Dear "+poppedGuest,"I am sorry I could not have you.")
poppedGuest=guestList.pop()
print(guestList)
print("Dear "+poppedGuest,"I am sorry I could not have you.")
poppedGuest=guestList.pop()
print(guestList)
print("Dear "+poppedGuest,"I am sorry I could not have you.")
poppedGuest=guestList.pop()
print(guestList)
print("Dear "+poppedGuest,"I am sorry I could not have you.")
poppedGuest=guestList.pop()
print(guestList)
print("Dear "+poppedGuest,"I am sorry I could not have you.")
print("Dear "+guestList[0],"You are still invited to my party.")
print("Dear "+guestList[1],"You are still invited to my party.")
del guestList[1]
del guestList[0]

print(guestList)
