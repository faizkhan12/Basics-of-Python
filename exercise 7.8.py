sandwich_orders=['panner','chicken','mushroom']
finished_sandwiches=[]
while sandwich_orders:
    current_order=sandwich_orders.pop()
    print("Hello,I made your "+current_order+" sandwich.")
    finished_sandwiches.append(current_order)
print("\nThe sandwich that was made:")
for finished_sandwich in finished_sandwiches:
    print("\t"+finished_sandwich)
