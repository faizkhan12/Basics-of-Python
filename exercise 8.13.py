def buildProfile(first,last,**user_info):
    person={}
    person['first name']=first
    person['last name']=last
    for key,value in user_info.items():
        person[key]=value
    return person

user_profile=buildProfile('Faiz','Khan',city='Patna',country='India',Hobby='Reading books')
print(user_profile)
