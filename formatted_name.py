#Returning a simple value
#def get_formatted_name(fName,lName):
  #  full_name=fName+' ' +lName
 #   return full_name
#musician=get_formatted_name('Faiz','Khan')
#print(musician)


#making an argument optional

#def get_formatted_name(fName,lName,mName=''):
    #if mName:
   #     full_name=fName+' '+mName+ ' '+lName
  #  else:
#     full_name=fName+' '+lName
 #   return full_name

#musician=get_formatted_name('Walter','Juniour')
#print(musician)

#musician=get_formatted_name('Hank','Payne','Lee')
#print(musician)

#returning dictionary
#def get_formatted_name(fName,lName,mName=''):
 #   person={'first':fName,'last':lName}
  #  if mName:
   #     person['mName']=mName
    #return person
#musician=get_formatted_name('Faiz','Khan',mName='Muhammad')
#print(musician)

def get_formatted_name(fName,lName):
    full_name=fName+' '+lName
    return full_name
flag=True
while flag:
    print("\nWhat is your name???")
    fName=input("Enter your first name")
    if fName=='q':
        break
    lName=input("Enter your last name")
    if lName=='q':
        break
    person=get_formatted_name(fName,lName)
    print("\nHello, "+person)
