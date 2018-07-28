favLang={
    'Faiz':['Java','python'],
    'Sheldon':['C#'],
    'Eric':['C','C++'],
    'Khan':['Python'],
    'Walter':['Python'],
    }
#print("Sheldon's and Khan's favourite languages are "+
 #        favLang['Sheldon']+' and '+ favLang['Khan']+
  #       " respectively.")
#looping
#for name,language in favLang.items():
 #   print("\n"+name+"'s favourite language is "+
  #        language+".\n")
    
#printing only names 

#friends=['Faiz','Sheldon']
#for name in favLang:
#    print(name)
 #   if name in friends:
  #       print("Hi "+name+",your favourite language is "+
   #           favLang[name]+"!")

#SORTED
for name in sorted(favLang):
    print(name)

#only mention language

for language in favLang.values():
    print(language)

for Language in set(favLang.values()):
    print(Language)
for name,languages in favLang.items():
    print("\n"+name+"'s favourite language(s)is/ are:")
    for language in languages:
        print(language)
    
