#!/usr/bin/env python3.6
from clean import title
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
    placed = input("Facebook,\n Twitter,\n Google,\n Instagram,\n Tinder,\n WhatsApp(you might be dumb to choose this)\nOr if you saved and want to view?type savedmenus \n")
    if placed == "Facebook" or placed=="facebook" or placed=="fb":
        emailfb = input("Please place you're email based on your facebook acc   ")
        passfb = input("pLace youre password   ")
        file = open("facebook.txt","a")
        file.write (emailfb)
        file.write (",")
        file.write (passfb)
        file.write("\n")
        file.close()

        print ("Your Facebook account has been saved bruv. ")
        print ("Now choose another criteria bruv.")
        print ("\n")
        print ("\n")
        savingprogress()

    elif placed == "Twitter" or placed=="twitter" or placed=="tweets":
        emailtw = input("Please place you're email based on your twitter acc")
        passtw = input("pLace youre password")
        file = open("twitter.txt","a")
        file.write (emailtw)
        file.write (",")
        file.write (passtw)
        file.write("\n")
        file.close()

        print ("Your twitter account has been saved bruv. ")
        print ("Now choose another criteria bruv.")
        print ("\n")
        print ("\n")
        savingprogress()

    elif placed == "google" or placed=="Google":
        emailgg = input("Please place you're email based on your facebook acc")
        passgg = input("pLace youre password")
        file = open("google.txt","a")
        file.write (emailgg)
        file.write (",")
        file.write (passgg)
        file.write("\n")
        file.close()
        print ("Your google account has been saved bruv. ")
        print ("Now choose another criteria bruv.")
        print ("\n")
        print ("\n")
        savingprogress()

    elif placed == "Instagram":
        emailig = input("Please place you're email or IG.handle based on your Instagram acc")
        passig = input("pLace youre password")
        file = open("instagram.txt","a")
        file.write (emailig)
        file.write (",")
        file.write (passig)
        file.write("\n")
        file.close()

        print ("Your Instagram account has been saved bruv. ")
        print ("Now choose another criteria bruv.")
        print ("\n")
        print ("\n")
        savingprogress()

    elif placed == "savedmenus":
        viewing()

    elif placed == "tinder" or placed == "Tinder":
        print("We dont do dating bruhh :-DD come on talk to chick stop being salty.....")
        print ("\n")
        print ("\n")
        savingprogress()

    elif placed == "whatsapp" or placed == "WhatsApp":
        print("NO....just no.....please..")
        print ("\n")
        print ("\n")
        savingprogress()

def viewing():
    print("Or would you like to view youre passcodes?")
    confirm=input("yes or no")
    if confirm == "yes":
        click=input("pick your acc fb, Ig, tweet or google")
        if click == "fb":
            facebk = open("facebook.txt","r")
            facedata = facebk.read()
            facedata.split("\n")
            if '' in facebk:
                facedata.remove('')
            facedata.close()
            email1 = input("place youre email to confirm")
            for linez in facedata:
                Logged_in = False
                emailfb, passfb = linez.split(",")
                print("here are your details")
                if Logged_in == emailfb == email1:
                    print(emailfb, passfb)

                
                        
    
    
        if click == "Ig":
            insta = open("instagram.txt","r")
            instadata = insta.readline()
            instadata.split("\n")
            if '' in instadata:
                instadata.remove('')
            instadata.close()
            insta1 = input("place youre handle to confirm")
            for linez in insta:
                Logged_in = False
                emailig, passig = linez.split(",")
                print("here are your details")
                if Logged_in == emailig == insta1:
                    print(emailig, passig)
    
    
        if click == "google":
            googl = open("google.txt","r")
            googledata = googl.readline()
            googledata.split("\n")
            if '' in googledata:
                googledata.remove('')
            googledata.close()
            email2 = input("place youre email to confirm")
            for linez in googledata:
                Logged_in = False
                emailgg, passgg = linez.split(",")
                print("here are your details")
                if Logged_in == emailgg == email2:
                    print(email2, passgg)

        if click == "tweet":
            tweett = open("twitter.txt","r")
            tweetdata = tweett.readline()
            tweetdata.split("\n")
            if '' in tweetdata:
                tweetdata.remove('')
            tweetdata.close()
            email3 = input("place youre email to confirm")
            for linez in tweetdata:
                Logged_in = False
                emailtw, passtw = linez.split(",")
                print("here are your details")
                if Logged_in == emailtw == email3:
                    print(email3, passtw)

    elif confirm == "no":
        savingprogress()                

                
            
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
if '' in UserData:
    UserData.remove('')

openfile.close()
def displayMenu():
    # print(UserData)
    title()
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