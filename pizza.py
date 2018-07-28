availToppings=['cheese','panner','chicken','olive'] #Available topping
requesToppings=['cheese','mushrm','olive'] #REquested topping from customer
for requesTopping in requesToppings:
    if requesTopping in availToppings:
        print("Adding "+requesTopping+".")
    else:
        print("Sorry, we dont have "+requesTopping+'.')        
print("\nFinished making pizza")
