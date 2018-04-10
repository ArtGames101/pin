# (c) ArtGames101 2018
import sys, os, subprocess, time, requests, urllib.request, wget

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("Enter Package URL> ").lower().strip()

def main():
    clear_screen()
    print("pin v1.0        (c) ArtGames101 2018\n")
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
    
