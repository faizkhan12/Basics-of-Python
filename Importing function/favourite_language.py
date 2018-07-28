from collections import OrderedDict

favourite_language=OrderedDict()
favourite_language['Faiz']='Python'
favourite_language['Sheldon']='Java'

for name,value in favourite_language.items():
    print(name+ " 's favourite language is "+value)
