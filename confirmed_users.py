unconfirmed_users=['Faiz','Khan','Sheldon']
confirmed_users=[]
while unconfirmed_users:
    currentUser=unconfirmed_users.pop()
    print("Verifying user: "+currentUser)
    confirmed_users.append(currentUser)

print("\nThe following users have benn confirmed.")
for confirmed_user in confirmed_users:
    print(confirmed_user)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while  'cat' in pets:
    pets.remove('cat')
print(pets)
