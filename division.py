#try:
 #   print(5/0)
#except ZeroDivisionError:
 #   print("you can't divide it by zero!")


print("Enter 2 number to divide")
print("Enter 'q' to quit")
flag=True
while flag:
    first_number=input("Enter the first number:")
    if first_number=='q':
        break
    second_number=input("Enter the second number:")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!!")
    else:
        print(answer)
