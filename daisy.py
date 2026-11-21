from colorama import init, Fore, Back
import os, time

init(autoreset=True)

print("starting operation 'mainfunctions'")
def flush():
    try:
        os.system("cls")
    except:
        os.system("clear")

def showinfo(msg):
    print("[" + Fore.LIGHTBLUE_EX + "INFO" + Fore.RESET + "] : " + str(msg))

def showerr(msg):
    print("[" + Fore.RED + "ERR" + Fore.RESET + " ] : " + Fore.RED + str(msg))

def showok(msg):
    print("[" + Fore.GREEN + " OK " + Fore.RESET + "] : " + str(msg))

def showbad(msg):
    print("[" + Fore.RED + "BAD" + Fore.RESET + " ] : " + str(msg))

def shownull(msg, patch=True):
    if patch == True:
        print("[    ] : " + str(msg))
    if patch == False:
        print("[PATCH]: " + str(msg))

def showwarn(msg):
    print("[" + Fore.YELLOW + "WARN" + Fore.RESET + "] : " + Fore.YELLOW + str(msg))

def showcount(index, msg):
    if len(str(index)) == 0:
        print("[     " + Fore.GREEN + str(index) + Fore.RESET + "] : " + str(msg))
    elif len(str(index)) == 1:
        print("[    " + Fore.GREEN + str(index) + Fore.RESET + "] : " + str(msg))
    elif len(str(index)) == 2:
        print("[   " + Fore.GREEN + str(index) + Fore.RESET + "] : " + str(msg))
    elif len(str(index)) == 3:
        print("[  " + Fore.GREEN + str(index) + Fore.RESET + "] : " + str(msg))
    elif len(str(index)) == 4:
        print("[ " + Fore.GREEN + str(index) + Fore.RESET + "] : " + str(msg))
    else:
        print("[" + Fore.GREEN + str(index) + Fore.RESET + "] : " + str(msg))

print("starting operation 'mainimports'")
import json
print("starting operation 'libimports'")
import libs.hashray
print("searching usr data...")
with open("usr/usrd.json", "r", encoding="utf-8") as f:
    data = json.load(f)
flush()
showwarn("Login Required")

def login():
    while True:
        for usrs in range(len(data["users"])):
            if data["users"][usrs]["hid"] == False :
                print(str(usrs) + ". " + data["users"][usrs]["name"])
            else:
                print("#.Hidden")
        usrname = input("username~/ ")
        targetusrname = None
        for usr in data["users"]:
            if usr["name"] == usrname:
                targetusrname = usr
        if targetusrname is None and usrname.isdigit() and int(usrname) < len(data["users"]):
            targetusrname = data["users"][int(usrname)]
        if targetusrname is not None:
            break
        showerr("Can't find user by username, try again")

    passxd = 0

    while True:
        usrpass = input("password~/ ")
        if libs.hashray.bypassQ(usrpass, targetusrname["pass"]) == True :
            passxd = 0
            break
        else:
            showerr("password is incorrect, try again")
            passxd += 1
            if passxd > 3 :
                showerr("brute force protection... wait 10 seconds")
                for timeoutx in range(10):
                    showerr("..." + str(timeoutx))
                    time.sleep(1)

login()
