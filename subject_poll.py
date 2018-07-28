Responses={}
flag=True
while flag:
    #person's name and responses
    name=input("Enter your name:")
    response=input("Which subject you like?")
    #store the response in the dictionary
    Responses[name.title()]=response.title()
    #Find out if anyone else is going to take the test 
    repeat=input("Would you like to let another response? (yes/no)")
    if repeat=='no':
        flag=False  #or break
#Displayin the result
print("poll result")
for name,response in Responses.items():
    print(name+ " favourite subject is "+response)
