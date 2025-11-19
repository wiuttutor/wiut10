from add import add_item
from remove import remove_item
from view import view_list

shopping_list = []

while True:
    print("Options: Add, remove, View and Exit")
    user_input =input("Select the options above: ").lower()

    if user_input =="add":
        item = input("Enter the item to add: ").split()
        for item in item:
            add_item(shopping_list,item)

    elif user_input =="remove":
        item = input("Enter the item to remove: ").split()
        for item in item:
            remove_item(shopping_list,item)

    elif user_input =="view":
        view_list(shopping_list)        

    elif user_input =="exit":
        print("Bye!")
        break

    else:
        print("Invalid input!")

    


