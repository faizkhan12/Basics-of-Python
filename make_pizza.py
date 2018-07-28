#passing an arbitary number of arguments

def makePizza(*toppings):
    print("\nMaking a pizza with the toppings")
    for topping in toppings:
        print(topping)
makePizza('pepperoni')
makePizza('mushroms','Cheese')
