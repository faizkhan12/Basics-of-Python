import json
filename='number.json'
try:
    with open(filename)as file_object:
        number=json.load(file_object)
except FileNotFoundError:
    number=input("What is your favourite number?")
    with open(filename,'w')as file_object:
        json.dump(number,file_object)
        print("Hi,I will remember your favourite number. It's "+number)
else:
    print("I know your favourite number. It's "+number)
