from grocery.add import add_item
from grocery.remove import remove_item
from grocery.view import view_list

students = []

while True:
    print("Options: Add, remove, View and Exit")
    user_input =input("Select the options above: ").lower()

    if user_input =="add":
        student = input("Enter the item to add: ").split()
        for s in student:
            add_item(students,s)

    elif user_input =="remove":
        student = input("Enter the item to remove: ").split()
        for s in student:
            remove_item(students,student)

    elif user_input =="view":
        view_list(students)        

    elif user_input =="exit":
        print("Bye!")
        break

    else:
        print("Invalid input!")

    


