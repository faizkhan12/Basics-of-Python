#Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that
#information, call make_album() with the user’s input and print the dictionary
#that’s created. Be sure to include a quit value in the while loop.

def make_album(Artist_name,Artist_title):
    person={'name':Artist_name,'title':Artist_title}
    return person
while True:
    print("\nEnter the album's artist:")
    print("(Enter 'q' at any time)")
    print("\nEnter the album's title:")
    print("(Enter 'q' at any time)")
    Name=input("Artist Name:")
    if Name=='q':
        break
    Title=input("Album Title:")
    if Title=='q':
        break
    Album=make_album(Name,Title)
    print(Album)
    
