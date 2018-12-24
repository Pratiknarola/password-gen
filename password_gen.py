import random
import string
def pass_gen(choice):
    if choice == "1":
        return random.choice(list(open('files/password.txt', 'r')))
    elif choice == '2':
        length = input("enter length: ")
        return "".join(random.choice(string.ascii_lowercase+string.ascii_uppercase+ string.digits + "!@#$%&*+") for _ in range(int(length)))
    else:
        print("incorrect input!!")
        return False
cont = True
print("Welcome to password generator!!!")
while cont:
    print("Choose any option:")
    choice = input("1. weak password\n2. strong password\n3. exit\n=> ")
    if choice == '3':
        cont = False
        break
    else:
        password = pass_gen(choice)
        if password == False:
            pass
        else:
            print('generated password is => ' + password)
