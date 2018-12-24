import random
import string
def pass_gen(choice):
    weak_list = [12345, 'admin', 'password', 'iloveyou', 'qwerty', 'asdfg', '12345678', 'aaaaaa', '111111', 'letmein',
                 'football', 'welcome','incorrect', 'login', 'passw0rd', 'hello', 'freedom', 'qazwsx', 'passwod1',
                 '123123', 'computer', '121212', 'amanda', 'charlie', 'maggie', 'test', 'p@ssword', 'dragon', 'starwars',
				 'whatever', 'trustno1', '654321', 'robert', 'matthew', '1qaz2wsx', 'sunshine', 'meandyou', 'admin123', 'name@123', '1q2w3e']
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