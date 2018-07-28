import json
number=input("What is your favourite number?")
filename='number.json'
with open(filename,'w')as file_object:
    json.dump(number,file_object)
    print(number)
