#Make a list of magician’s names. Pass the list to a function
#called show_magicians(), which prints the name of each magician in the list.

#def show_magician(names):
 #   print("Magician names:")
  #  for name in names:
   #     print("\t"+name)

#Magician=['Faiz','Khan','Margot']
#show_magician(Magician)

#Start with a copy of your program from Exercise 8-9.
#Write a function called make_great() that modifies the list of magicians by adding
#the phrase the Great to each magician’s name. Call show_magicians() to
#see that the list has actually been modified.

def show_magician(names): #defining a function show_magician with parameter 'names'
    print("Magician names:") 
    for name in names:
        print("\t"+name)

def make_great(names): #defining another function make_great with parameter 'names'
    great_magicians=[] #making an empty list 
    while names:
        name=names.pop() #making temporarily variable 'name' and storing the value of 'names' on it
        great_magician=name+' the great.' #Now storing in the variable 'great_magician'
        great_magicians.append(great_magician) #storing all the values in 'great_magicians'
    for great_magician in great_magicians:
        names.append(great_magician) #storing the statement 'the great.' in names along with the name with it
names=['Faiz','Khan','Margot']
make_great(names)
show_magician(names[:])

    
