Ticket="\nWhat is your age:"
Ticket+="\nEnter 'quit' when you are finished:"
flag=True
while flag:
    message=input(Ticket)
    if message=='quit':
        break
    message=int(input(Ticket))
    if message<3:
        print("The ticket is free.")
    elif message>=3 and message<=12:
        print("The ticket is $10.")
    elif message>12:
        print("The ticket is $15.")
        
