import getpass

username = "user123"
password = "password123"

isLogin = False

while isLogin == False:
    userInput = input("Type your username : ")
    passInput = getpass.getpass("Type your password : ")

    if userInput == username and passInput == password :
        isLogin = True
        print("LOGIN SUCCESS")
    else:
        IsLogin = False
        print("INCORRECT INFORMATION")