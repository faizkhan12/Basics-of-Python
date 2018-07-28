myPizzas=['Subhraj','Oliver','Dominos']
frndPizzas=myPizzas[:]
myPizzas.append('pizzahut')
frndPizzas.append('cheeseburst')
print("My favourite pizzas are:")
for myPizza in myPizzas:
    print(myPizza)
print("\nMy friend's favourite pizzas are:")
for frndPizza in frndPizzas:
    print(frndPizza)
