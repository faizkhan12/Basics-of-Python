Alien={'x_position':0,'y_position':25,'Speed':'Medium'}
print("Original position of x:"+str(Alien['x_position']))
if Alien['Speed']=='Slow':
    x_position=1
elif Alien['Speed']=='Medium':
    x_position=2
elif Alien['Speed']=='Fast':
    x_position=3
Alien['x_position']=Alien['x_position']+x_position
print("New position of x:" +str(Alien['x_position']))

#Removing 'y_position'

del Alien['y_position']
print(Alien)
