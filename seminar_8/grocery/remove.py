def remove_item(shopping_list, item):
    if item not in shopping_list:
        print(f"The {item} not found!")
    else:
        shopping_list.remove(item)
        print(f"The {item} has been removed!")

