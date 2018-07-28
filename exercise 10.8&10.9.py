filenames=['cat.txt','dog.txt']
for filename in filenames:
    #print("\nReading files.."+filename)
    try:
        with open(filename) as file_object:
            contents=file_object.read()
            #print(contents)
    except FileNotFoundError:
        #print("Sorry the file "+filename+" does not exist.")
        pass
    else:
        print("\nReading files.."+filename)
        print(contents)
