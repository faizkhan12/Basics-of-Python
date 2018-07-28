Cities={
    'Patna':{
        'Country':'India',
        'Population':1400000,
        'Fact':'Very ancienct city',
        },
    'Mumbai':{
        'Country':'India',
        'Population':1300000,
        'Fact':'Bollywood city',
        },
    'Sydney':{
        'Country':'Australia',
        'Population':900000,
        'Fact':'Capital of Country',
        },
    }
for name,value in Cities.items():
    print("\nName of city: "+name)
    Country=value['Country']
    Population=value['Population']
    Fact=value['Fact']
    print("\t"+name +" is the city of "+Country+".It has a popualtion of over "+str(Population)+".It is a "+Fact+".")
