#!/usr/bin/env python3.6
def newUser():
        print("Yippeeee......we love visitors and due to that slight note..")
        print("\n")
        createLogin = input("Create login name:")
        if createLogin in UserData:
            print("Login name already exist!")

        else:
            name = input("Please reenter to confirm. ")
        

        username = name
        print ("Your username has been created and is", username, ".")

        password = input("Now please create a password. ")



        file = open("Login.txt","a")
        file.write (username)
        file.write (",")
        file.write (password)
        file.write("\n")
        file.close()

        print ("Your login details have been saved. ")
        print ("Now log in")
        oldUser()
        

def oldUser():
        login = input("Enter login name: ")
        passw = input("Enter password: ")
        logged_in = False
        for line in UserData:
            username, password = line.split(',')
            print(username, password)
            if username == login:
                logged_in = password == passw      
                break
        if logged_in: 
            print ("Login successful!")
            savingprogress()
        else:
            print ("User doesn't exist or wrong password")

def savingprogress():
    print('In this application we save your progress for later use!!!')
    print('PLease choose which account type you want us to save for you. ')
    print("\n")
    placed = input("Facebook,\n twitter,\n google,\n instagram,\n tinder,\n whatsApp(you might be dumb to choose this)\n")
    if placed == "Facebook":
        emailfb = input("Please place you're email based on your facebook acc")
        passfb = input("pLace youre password")
        file = open("facebook.txt","a")
        file.write (emailfb)
        file.write (",")
        file.write (passfb)
        file.write("\n")
        file.close()

        print ("Your Facebook account has been saved bruv. ")
        print ("Now choose another criteria bruv.")


def tryagain():
    status2 = input("Are you a registered user?yes or no?")
    if status2 == "yes":
        oldUser()

    elif status2 == "no":
        newUser()
    
    elif status2 != "yes" or "no":
        print("Am sorry,you wanna hack us bruh??")
        print("reaaaallllYYYYY??please answer the question.")
        terminate()


    
filename = 'Login.txt'
openfile = open(filename,"r")
UserData = openfile.readline()
UserData = UserData.split('\n')
openfile.close()
def displayMenu():
    # print(UserData)
    print("Welcome To The Password Locker Application!")
    print("\n")
    print("We have alot in stored for you....like literally we store passwords... ")
    print("\n")
    status = input("Are you a registered user?yes or no?")
    if status == "yes":
        oldUser()

    elif status == "no":
        newUser()
    
    elif status != "yes" or "no":
        print("Am sorry,you wanna hack us bruh??")
        print("reaaaallllYYYYY??please answer the question.")
        print('\n')
        tryagain()


def terminate():
    print('\n')
    print("And because once bitten twice shy....am closing this terminal men.")
    exit()
if  __name__ == "__main__":
    displayMenu()