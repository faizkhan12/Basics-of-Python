def print_models(unprinted_design,completed_models):
    while unprinted_design:
        current_design=unprinted_design.pop()
        print("Printing model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe models that have been printed:")
    for completed_model in completed_models:
        print(completed_model)

