value=input("What is your name")
print(value)

prompt= "If you tell us who you are, we can personalize the messages you see."
prompt+= "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

Age=int(input("Enter the age"))
print(Age)
if Age>=18:
    print('True')
else:
    print('False')
