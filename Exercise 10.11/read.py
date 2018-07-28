import json
filename='number.json'
with open(filename)as file_object:
    number=json.load(file_object)
    print("I know your favourite number.It's "+number)
