from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        return randint(1,self.sides)

d6=Die()
results=[]
for num in range(10):
    result=d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sides die:")
print(result)
