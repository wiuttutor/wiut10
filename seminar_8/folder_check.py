import os

def folder_check():
    user_input = input("Enter a file name: ")

    if os.path.exists(user_input):
        print("You have this folder!")
    else:
        os.mkdir(user_input)
        print("The file has been created!")

folder_check()