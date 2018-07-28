#10-6. Addition: One common problem when prompting for numerical input
#occurs when people provide text instead of numbers. When you try to convert
#the input to an int, you’ll get a TypeError. Write a program that prompts for
#two numbers. Add them together and print the result. Catch the TypeError if
#either input value is not a number, and print a friendly error message. Test your
#program by entering two numbers and then by entering some text instead of a
#number

print("Enter 2 numbers to add")
print("Enter 'q' to quit")
flag=True
while flag:
    first_number=input("\nEnter 1st number:")
    if first_number=='q':
        break
    second_number=input("\nEnter 2nd number:")
    if second_number=='q':
        break
    try:
        answer=int(first_number)+int(second_number)
    except ValueError:
        print("I needed a number")
    else:
        print(answer)
    
