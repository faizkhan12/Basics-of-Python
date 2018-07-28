Pets={
    'Tommy':{
        'Animal':'Dog',
        'Owner':'Faiz',
        },
    'Catty':{
        'Animal':'Cat',
        'Owner':'Eric',
        },
    }

for name,value in Pets.items():
    print("\nName of the pet: " + name)
    Animal=value['Animal']
    Owner=value['Owner']
    print("\tThis is the " + Animal+ " and I love him the most."+Owner+ " is the owner of this "+Animal+'.')
    
    
