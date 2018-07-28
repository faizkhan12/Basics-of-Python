Responses={}
flag=True
while flag:
    name=input("\nWhat is your name?")
    response=input("\nIf you have a choice to go one place, where would you go?")
    Responses[name]=response
    repeat=input("Would you like another response???(yes/no)") 
    if repeat=='no':
        break

print("\n----pollling results-----")
for name,response in Responses.items():
    print(name+ " woud like to go to "+response+"as his favourite destination.")
