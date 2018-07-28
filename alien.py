Aliens=[]
for Alien_number in range(50):#Make 50 aliens
    newAlien={'color':'red','point':5}
    Aliens.append(newAlien)

for Alien in Aliens[0:10]:
    if Alien['color']=='red':
             Alien['color']='Green'
             Alien['point']=10
    elif Alien['color']=='Green':
        Alien['color']='yellow'
        Alien['point']=15
        
#show first 20 aliens
for Alien in Aliens[:15]:
    print(Alien)

#Display how many Aliens have been created
print("Total number of Aliens: "+str(len(Aliens)))
