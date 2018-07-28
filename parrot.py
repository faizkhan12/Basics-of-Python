parrot="\nTell me something and i will write it back to you."
parrot+="\nEnter 'quit' to close the program:"
flag=True
while flag:
   message=input(parrot)
   if message=='quit':
        flag=False
   else:
        print(message)

