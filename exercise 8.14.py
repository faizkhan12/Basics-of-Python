def make_car(Manufacturals,Mdelnames,**optional):
    profile={}
    profile['Manufactural']=Manufacturals
    profile['Mdelname']=Mdelnames
    for key,value in optional.items():
        profile[key]=value
    return profile
car=make_car('Subaru','Outback',color='blue',tow_package='True')
print(car)
