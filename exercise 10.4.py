#10-4. Guest Book: Write a while loop that prompts users for their name. When
#they enter their name, print a greeting to the screen and add a line recording
#their visit in a file called guest_book.txt. Make sure each entry appears on a
#new line in the file.

filename='guest_bk.txt'
print("Enter quit when you are finished.")
flag=True
while flag:
    name=input("\nEnter your name")
    if name=='quit':
        break
    else:
        with open(filename,'a')as file_object:
            file_object.write(name)
        print("Hi "+name+ ",you have been added to the book.")  
