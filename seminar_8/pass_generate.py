import random as rn

def pass_generate(repetiton=None):
    predefined = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''

    if repetiton is not None:
        rn.seed(repetiton)

    for ch in range(8):
        password += rn.choice(predefined)
    return password


user_input = input("Do you want to get repetitice password: Y/N: ").lower()

if user_input =="y":
    repeated_pass = input(f"Enter any number: ")
    print(f"Repeated pass: {pass_generate(repeated_pass)}")
else:
    print(f"Random pass: {pass_generate()}")