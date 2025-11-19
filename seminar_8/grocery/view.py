def view_list(shopping_list):
    if not shopping_list:
        print(f"Your shopping list is empty!")

    else:
        for index, item in enumerate(shopping_list,1):
            print(f"{index}. {item}")

