People={
    'Shad':{
        'First':'Shad',
        'Last':'Ahamad',
        'Age':21,
        'City':'Kolkata',
        },
    'Faiz':{
        'First':'Faiz',
        'Last':'Khan',
        'Age':21,
        'City':'Patna',
        },
    }
for name,value in People.items():
    print("\nName: "+name)
    fullName=value['First'] + " " + value['Last']
    City=value['City']
    Age=value['Age']
    print("Full name: " + fullName)
    print("Age: " + str(Age))
    print("City: " + City)
