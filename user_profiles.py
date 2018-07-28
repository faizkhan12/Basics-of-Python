def build_profile(first,last,**user):
    profile={}
    profile['first name']=first
    profile['last name']=last
    for key,value in user.items():
        profile[key]=value
    return profile
user=build_profile('Faiz','Khan',city='patna',country='India')
print(user)
