#10-5. Programming Poll: Write a while loop that asks people why they like
#programming. Each time someone enters a reason, add their reason to a file
#that stores all the responses.

filename='programming_poll.txt'
print("Enter quit when you are done")
responses=[]

flag=True
while flag:
    responses=input("\nWhy do you like prgramming?")
    responses.append(response)
    if responses=='quit':
        break
with open(filename,'a') as file_object:
    for response in responses:
        file_object.write(response)
