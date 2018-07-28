import json
numbers=[2,4,6,7,9]

filename='numbers.json'
with open(filename,'w')as file_object:
    json.dump(numbers,file_object)
