# Hello, I'm Maruf Hasan, the developer of this short and simple project. This is a password generating project.
# The specialty of this project is generating passwords based on user interrogation. User can also be able to generate random passwords.
# This is project is free to use everywhere and modifiable.
# Don't forget to visit my GITHUB - @the-psycoder, FACEBOOK - @psyman.one
# Thank you for reading!

import os
try:
    from colorama import Fore as color
    pass
except:
    os.system('pip install colorama')
    from colorama import Fore as color
    pass
import random as rd
import string

hint1 = color.CYAN + "Type 1 or 2 to proceed >> "
hint2 = color.CYAN + "\nLength of your password? (8-80 Char) >> "
hint3 = color.CYAN + "\nPassword Generated >> "
hint4 = color.CYAN + "What is your name? >> "
hint5 = color.CYAN + "How old are you? >> "
hint6 = color.CYAN + "What is your favourite number? >> "
hint7 = color.CYAN + "What is your favourite color? >> "
items = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
ranlist = []
ranlist.extend(list(items))

def run():
    print(color.CYAN + "\n\n1. Generate a random password\n2. Generate a password based on some questions related to you\n")
    mode = str(input(hint1 + color.YELLOW))
    if mode == "1":
        rangen()
    elif mode == "2":
        quegen()
    elif mode == "exit":
        print(color.RESET)
        exit(1)
    else:
        print(color.RED + "\nInvalid input, please try again!\n")
        run()

def rangen():
    passlen = int(input(hint2 + color.YELLOW))
    if passlen >= 8 and passlen <= 80:
        rd.shuffle(ranlist)
        password = "".join(ranlist[0:passlen])
        print(hint3 + color.GREEN + password, passpower(password))
        print(color.BLUE + "\nThank you for using this tool\nMaruf Hasan (@the-psycoder)\n")
        run()
    elif passlen < 8:
        print(color.RED + "\nYou have entered less length amount, less length amount of your password can be hacked!\nTry again!\n")
        rangen()
    elif passlen > 150:
        print(color.RED + "\nYou have entered too much length amount, try 8 - 80\n")
        rangen()
    else:
        print(color.RED + "\nInvalid input, try again!\n")
        rangen()
    
def quegen():
    print(color.BLUE + "\nNOTE : This password generating system has developed by Maruf Hasan (@the-psycoder) named 'Interrogation Based Password Generator'.\nIt generates super strong passwords based on some questions related to user and the generated password is easy to memorize.\n")
    que1 = str(input(hint4 + color.YELLOW)).upper()
    que2 = str(input(hint5 + color.YELLOW))
    que3 = str(input(hint6 + color.YELLOW))
    que4 = str(input(hint7 + color.YELLOW)).lower()
    try:
        numcomb = (int(que2)+80-8)/int(que3)*8
    except ValueError as e:
        print(color.RED + "\nInvalid input, try again!\n")
        quegen()
    numlist = list(str(float(numcomb)))
    rd.shuffle(numlist)
    numranmize = "".join(numlist[:])
    password = f">1@M~{que1}~C0dE~{numranmize}~&1@M~{que2}0LD~IL0vE{que4}<"
    print(hint3 + color.GREEN + password, passpower(password))
    print(color.BLUE + "\nThank you for using this tool\nMaruf Hasan (@deepwave-coder)\n")
    run()

def passpower(password):
    passlength = len(password)
    result1 = color.YELLOW + "[ Weak ]" + color.RESET
    result2 = color.CYAN + "[ Strong ]" + color.RESET
    result3 = color.BLUE + "[ Super strong ]" + color.RESET

    if passlength >= 8 and passlength <= 15: return result1
    elif passlength > 15 and passlength <= 35: return result2
    elif passlength > 35 and passlength <= 80: return result3
       
run()