def count_words(filename):
    """count the approximate number of words"""
    try:
        with open(filename) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        pass #telling to ignore the filenotfound exception message
    else:
        words=contents.split()
        num_words=len(words)
        print(str(num_words))
filenames=['alice.txt','aadsda.txt']
for filename in filenames:
    count_words(filename)
