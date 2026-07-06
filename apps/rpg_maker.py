import time
import os
import subprocess
import pyfiglet
from pyfiglet import Figlet

if os.name == "nt":  
    os.system("taskkill /IM mpv.exe /F >nul 2>&1")
    os.system("taskkill /IM vlc.exe /F >nul 2>&1")


playing_media = []

class Media:
    def __init__(self, name):
        self.name = name
    
    def start_loop_img(name):
        the_img = play_media(name, video=True, loop=True)
        playing_media.append(the_img)
    
    def start_loop_audio(name):
        the_audio = play_media(name, video=False, loop=True)
        playing_media.append(the_audio)
    
    def start_video_on_a_certain_time(name,tiempo):
        the_video_on_a_certain_time = play_media(name, video=True, loop=False, start=tiempo)
        playing_media.append(the_video_on_a_certain_time)
    def kaboom_media():
        for c in playing_media:
            c.kill()


full_dot = '●'
empty_dot = '○'

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def slow_print_white(text, delay=0.02): 
    for char in text:
        print(f"\033[1;37m{char}\033[0m", end="", flush=True)
        time.sleep(delay)
    print()

def slow_input_white(prompt, delay=0.02):
    for char in prompt:
        print(f"\033[1;37m{char}", end="", flush=True)
        time.sleep(delay)
    return input()

def loading_bar():

    total = 20

    for i in range(total + 1):
        barra = "#" * i + "-" * (total - i)
        print(f"\r\033[1;37m[{barra}] [{i*5}%]", end="")
        time.sleep(0.3)

    print()  

def ask_name():
    while True:      
        name = slow_input_white("Insert the character's name (12 characters max): ").capitalize()
        if len(name) > 12 or " " in name or len(name) <= 0:
            slow_print_white("[  ERROR  ] Invalid input. Try again")
            time.sleep(1)
            clear()
            hola()
            continue
        else:
            print()
            return name


def ask_last_name():
    while True:
        last_name = slow_input_white("Insert the character's last name (12 characters max): ").capitalize()
        if len(last_name) > 12 or " " in last_name or len(last_name) <= 0:
            slow_print_white("[  ERROR  ] Invalid input. Try again")
            time.sleep(1)
            clear()
            hola()
            continue
        else:
            print()
            return last_name

def play_media(archivo, video=False, loop=False, start=None):
    try:
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, "assets", archivo)
        command = ["mpv"]
        flags = 0
        if os.name == "nt":
            flags = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW

        if not video:
            command.append("--no-video")
        if loop:
            command.append("--loop")
        if start:
            command.append(f"--start={start}")

        command.append(path)

        return subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=flags
        )
    except FileNotFoundError:
        slow_print_white("[  ERROR  ] File not found")
        return None
    except OSError:
        slow_print_white("[  ERROR  ] Error while trying to execute mpv")
    except Exception as e:
        slow_print_white(f"[  ERROR  ] An error occurred: {e}")
        return None

def ask_age():
    while True: 
        try:
            age = int(slow_input_white("Insert the character's age (100 years max): "))
            if age > 100 or age < 1:
                slow_print_white("[  ERROR  ] Invalid age. Try again")
                time.sleep(1)
                clear()
                hola()
                continue
            else:
                print()
                return age
        except ValueError:
            slow_print_white("[  ERROR  ] Invalid input. Try again")
            time.sleep(1)
            clear()
            hola()
            continue

def ask_stats(stat):
     while True: 
        try:
            stat_points= int(slow_input_white(f"Insert the character's {stat} points (10 points max): "))
            if stat_points > 10 or stat_points <= 1:
                slow_print_white("[  ERROR  ] Invalid points. Try again")
                time.sleep(1)
                clear()
                hola()
                continue
            else:
                print()
                return stat_points
        except ValueError:
            slow_print_white("[  ERROR  ] Invalid input. Try again")
            time.sleep(1)
            clear()
            hola()
            continue

def show_character_info(name, last_name, age, strength, intelligence, charisma):
    fullname = f"{name} {last_name}"
    slow_print_white("This is the info of your character")
    slow_print_white(f"""
    {fullname}
    Age: {age}
    STR: {make_bar(strength)}
    INT: {make_bar(intelligence)}
    CHA: {make_bar(charisma)}
    """)

def again_question(): 
    while True:

     
        again = slow_input_white("Would you like to create a new character?? (y/n): ").lower()

        if again.lower() == "y":
            print()
            clear()
            hola()
            return True
        
        elif again.lower() == "n":
            Media.kaboom_media()
            slow_print_white("[  INFO  ] Shuting down the Character Creator...")
            loading_bar()
            slow_print_white("[  OK  ] Done!")
            time.sleep(2)
            slow_print_white("[  INFO  ] Thanks for using Character Creator!")
            print()
            time.sleep(1)
            return False
        
        else:
            slow_print_white("[  ERROR  ] Invalid input. Please try again")

def make_bar(value):
    return full_dot * value + empty_dot * (10 - value)

def hola():

    print(" _   _           _   _____ ___  ________  ____________ _____   ")
    print("| \ | |         | | /  __ \|  \/  |  _  \ | ___ \ ___ \  __ \\ ")
    print("|  \| | _____  _| |_| /  \/| .  . | | | | | |_/ / |_/ / |  \/  ")
    print("  . ` |/ _ \ \/ / __| |    | |\/| | | | | |    /|  __/| | __"   )
    print("| |\  |  __/>  <| |_| \__/\| |  | | |/ /  | |\ \| |   | |_\ \\ ")
    print("\_| \_/\___/_/\_\\__|\____/\_|  |_/___/   \_| \_\_|    \____/  ")

def run(): 
    
    hola()
    print()

    def rpg_maker():
        running = True

        while running: 
            
            name = ask_name()
            last_name = ask_last_name()    
            age = ask_age()
            strength_points = ask_stats("strength")
            intelligence_points = ask_stats("intelligence")
            charisma_points = ask_stats("charisma")
            show_character_info(name, last_name,  age, strength_points, intelligence_points, charisma_points)
            
            if not again_question():
                running = False
                break         
            else:
                Media.kaboom_media()
           
    try:
        rpg_maker()
    finally:
        clear()
   
if __name__ == "__main__":
    clear()
    run()
    
