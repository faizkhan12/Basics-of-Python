#Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.
#Add an optional parameter to make_album() that allows you to store the
#number of tracks on an album. If the calling line includes a value for the number
#of tracks, add that value to the album’s dictionary. Make at least one new
#function call that includes the number of tracks on an album.

def make_album(Artist_name,Artist_title,trackNum=''):
    person={'name':Artist_name,'title':Artist_title}
    if trackNum:
        person['trackNum']=trackNum
    return person
Album=make_album('Eminem','Rap God',trackNum=17)
print(Album)
Album=make_album('EdSheren','Divide')
print(Album)
Album=make_album('Taylor Swift','Love Song')
print(Album)
print(Album)
