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
