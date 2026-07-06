import time
import os 
import subprocess

if os.name == "nt":  
    os.system("taskkill /IM mpv.exe /F >nul 2>&1")
    os.system("taskkill /IM vlc.exe /F >nul 2>&1")


def playaudio():
    try: 

        base_dir = os.path.dirname(__file__)
        sound_path = os.path.join(base_dir, "assets", "hola.mp3")

        flags = 0
        if os.name == "nt":
            flags = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW

        player = subprocess.Popen(["mpv", "--no-video", "--loop", "--start=00:01", "--no-terminal", "--really-quiet", "--msg-level=all=no", sound_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=flags 
        )

        return player
      
                
    except FileNotFoundError:
        try:
            
            base_dir = os.path.dirname(__file__)
            sound_path = os.path.join(base_dir, "assets", "hello.mp3")

            flags = 0
            if os.name == "nt":
                flags = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW

            player = subprocess.Popen(["vlc", "--intf dummy", "--loop", "--start-time=00:02", "--no-video", sound_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=flags 
            )

            return player
        except FileNotFoundError:

            slow_print_white("Error: music file not found or mpv nor vlc is not installed")
            print()
            return None


def titulo():

    print("    _  __        __  _______  ______    ___             _         __    ")
    print("   / |/ /____ __/ /_/ ___/  |/  / _ \  / _ \_______    (_)__ ____/ /_   ")
    print("  /    / -_) \ / __/ /__/ /|_/ / // / / ___/ __/ _ \  / / -_) __/ __/   ")
    print(" /_/|_/\__/_\_\\__/\___/_/  /_/____/ /_/  /_/  \___/_/ /\__/\__/\__/    ")
    print("                                                  |___/                 ")
    print()

def eslogan():

    print("   _|_|_  _  ._  _  _|_  _ _ ._ _ ._ _  _.._  _| o _    ._  _|_ _     _     ")
    print("    |_| |(/_ | |(/_><|_ (_(_)| | || | |(_|| |(_| |_> |_||_)  |_(_) \/(_)|_| ")
    print("                                                        |          /        ")
    print()

def run():
    player = playaudio()
    titulo()
    eslogan()
    fast_print_white(
    "==============================\n"
    "\n"
    "A SIMPLE TERMINAL MENU\n"
    "-----------------------\n"
    "\n"
    "AUTHOR: Re:Alloc\n"
    "PROGRAMMING LANGUAGE: Python\n"
    "INSPIRED BY: fastfetch, neofetch, terminal menus in general\n"
    "PROYECT STARTED: December 2025\n"
    "\n"
    "SPECIAL THANKS TO:\n"
    "-A friend: he taught me how to program in Lua and common IT knowledge a long time ago and motivated me\n"
    "to becomen a dev. I also want to thank his dad because he also taught me things about Raspberry Pi\n"
    "-A, F & M: they're my classroom best friends and I'm glad I met them, because they are amazing friends\n"
    "-FreeCodeCamp: thanks to this website I learnt all the basics about Python. You can check it out if you\n"
    "want to start programming in Python but don't know how (It's not a sponsor btw)\n"
    "-You, the user: thank you for trying out this proyect\n"
    "\n"
    "================================\n"
    "\n"
    "WHY THIS PROYECT EXISTS\n"
    "------------------------\n"
    "\n"
    "This proyect exists because I want to become a pro developer in the future. Since I currently don't know C++ or Java, I decided\n"
    "to start learning programming with Python because it's one of the easiest languages out there"
    "\n"
    "I started learning Python at FreeCodeCamp (like I said before). I discovered this website a long time ago, and one of the coolest\n"
    "things this website has are the 'lab exercises', where they give you some requirements and you have to build a program that satisfies\n"
    "those requirements"
    "\n"
    "After I saw those exercises for the fist time, I said to myself:\n"
    "\n"
    "'Wouldn't it be awesome to create a menu where I can launch all the 'lab exercises' I've made?'\n"
    "\n"
    "After finishing the prototype of the calculator you can use on the menu, I decided that, instead of launching the 'lab exercises', I would\n"
    "launch my own apps. Then, I started researching and learning how to do a terminal menu, how to play multimedia on Python, etc. "
    "\n"
    "For the name of the proyect, I came up with 'NextCommand', but I thought it was too generic, and abbreviated it into 'NextCMD"
    "\n"
    "And that's how NextCMD was born\n"
    "\n"
    "================================\n"
    "\n"
    "WHAT AM I WORKING ON RIGHT NOW TO IMPROVE THE PROYECT\n"
    "-------------------------------------------------------\n"
    "\n"
    "Right now, I'm working on JSON files. with JSON files, I could store the exact episode and minute from the las anime I saw\n"
    "in the anime player. After working on JSON files, I will learn OOP (Object-Oriented Programming) in Python\n"
    "\n"
    "Finaly, I finished working on JSON files and now I'm learning OOP. I've applied some OOP in the main menu, and I'm proud of it\n"
    "\n"
    "Also, I've decided to learn C after learning OOP in Python because I wanted to try a new programming language. Right now, C is SO HARD\n"
    "for me to understad. There are a lot of new things different from Python, like pointer and more, but I'll adapt to them"
    "\n"
    "Basically, this is my first BIG python proyect, and that's why I want to learn all the most important things in Python so I can\n"
    "apply them on my project\n"
    "\n"
    "EDIT: ALL THIS INFO IS OUTDATED AND IT COMES FROM THE ORIGINAL VERSION. I JUST MADE SOME CHANGES AND RESUMED ALMOST EVERYTHING\n"
    "ALSO, SOME THINGS HAVE BEEN MODIFIED DUE TO PRIVACY THEMES AND COPYRIGHT NOT ONLY IN THESE CREDITS, BUT IN THE ENTIRE PROJECT\n"
    
  
                     )
    if not exit_credis():
        player.kill()
 

def exit_credis():
        slow_input_white("Press Enter to go back to the menu: ")
        slow_print_white("Thanks for watching the credits of the proyect!")
        time.sleep(1)
        clear()
            
    
          

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def slow_print_white(text, delay=0.01): 
    for char in text:
        print(f"\033[1;37m{char}\033[0m", end="", flush=True)
        time.sleep(delay)
    print()

def fast_print_white(text, delay=0.007): 
    for char in text:
        print(f"\033[1;37m{char}\033[0m", end="", flush=True)
        time.sleep(delay)
    print()

def slow_input_white(text, delay=0.01): 
    for char in text:
        print(f"\033[1;37m{char}", end="", flush=True)
        time.sleep(delay)
    return input()


if __name__ == "__main__":

    clear()
    run()
