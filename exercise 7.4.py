Topping="\nEnter a series of pizza topping"
Topping+="\nEnter 'quit' to exit the program:"
flag=True
while flag:
    message=input(Topping)
    if message=='quit':
        break
    else:
        print("Add "+message+" To this pizza.")
