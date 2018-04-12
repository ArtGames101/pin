# (c) ArtGames101 2018
try:
    import sys, os, subprocess, time, requests, urllib.request, wgetyt
except:
    import sys, os
    print("Error: ImportError")
    print("\n"
                 "1. Install Requirements\n"
                "0. Exit")
    su = input("Option> ").lower().strip()
    if su == "1":
        import subprocess
        subprocess.call((sys.executable, "req.py"))

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("Enter Package URL> ").lower().strip()

def user_choicefol():
    return input("Enter disired folder name> ").lower().strip()

def main():
    clear_screen()
    print("pin 2.0        (c) ArtGames101 2018\n")
    choice = user_choice()
    try:
        print("Connecting to {}...".format(choice))
        time.sleep(2)
        wget.download(choice)
        print("\nDownloaded!")
    except:
        input("Unable to connect!")
    sys.exit()

main()
    
