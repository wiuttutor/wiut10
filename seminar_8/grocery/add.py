def add_item(shopping_list, item):
    if item in shopping_list:
        print(f"You hav this {item}")
    else:
        shopping_list.append(item)
        print(f"The {item} has been added!")