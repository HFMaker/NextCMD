import time
import os 
import subprocess
from apps import calculator as calculator
from apps import rpg_maker as rpg_maker
from apps import anime_player as anime_player
from apps import system_info as system_info
from apps import credits as credits
from apps import notes as notes
from apps import typing_of_the_death as TOTD

def slow_print_white(text, delay=0.01): 
    for char in text:
        print(f"\033[1;37m{char}\033[0m", end="", flush=True)
        time.sleep(delay)
    print()

def slow_input_white(text, delay=0.01): 
    for char in text:
        print(f"\033[1;37m{char}", end="", flush=True)
        time.sleep(delay)
    return input()

def play_media(archivo, video=True, loop=False, start=None):
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

        player = subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=flags
        )
        return player
    except FileNotFoundError:
        slow_print_white("File not found")
        return None
    except OSError:
        slow_print_white("Error while trying to execute mpv")
    except Exception as e:
        slow_print_white(f"An error occurred: {e}")
        return None
    
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def loading_bar():

    total = 20

    for i in range(total + 1):
        barra = "#" * i + "-" * (total - i)
        print(f"\r\033[1;37m[{barra}] [{i*5}%]", end="")
        time.sleep(0.3)

    print()  

def titulo():

    print("   _  __        __  _______  ______")
    print("  / |/ /____ __/ /_/ ___/  |/  / _ \\")
    print(" /    / -_) \ / __/ /__/ /|_/ / // /")
    print("/_/|_/\__/_\_\\__/\___/_/  /_/____/")
    print()

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
    
    def kaboom_media():
        for c in playing_media:
            c.kill()

class App:
    def __init__(self, nombre, comando):
        self.nombre = nombre
        self.comando = comando
    def ejecutar(self):
        slow_print_white(f"[  INFO  ] Loading {self.nombre}...")
        loading_bar()
        slow_print_white("[  OK  ] Done!")
        time.sleep(2)
        clear()
        self.comando()
        clear()

def shutdown():
    Media.kaboom_media()
    slow_print_white("[  INFO  ] Shutting down...")
    loading_bar()
    slow_print_white("[  INFO  ] Done!")
    time.sleep(2)
    slow_print_white("[  INFO  ] Thanks for using NextCMD!")
    time.sleep(1)


def run():
    
    Media.start_loop_audio("hola.mp3")
    running = True
    while running:

            print()
            titulo()
    
            avaiable_apps = {"1": "Calculator", "2" : "Character Creator",
            "3" : "Anime Player", "4" : "Notes", "5" : "TOTD", "6" : "System Info", 
            "7" : "Credits", "8" : "hola", "./NextCMD_Secret.sh" : "LinuxForLive"}

            run_commands = {"1" : calculator.run, "2" : rpg_maker.run,
            "3" : anime_player.run, "4" : notes.run, "5" : TOTD.run, "6" : system_info.run, 
            "7" : credits.run, "8" : "hola", "./NextCMD_Secret.sh": "LinuxForLive"}

            try:
                app_select = slow_input_white("=== APP SELECTOR ===\n"
                "1) Calculator: the best calculator in the world\n"
                "2) RPG Character Creator: create your own RPG Character\n"
                "3) Anime Player: you can watch some animes here\n"
                "4) Notes: You can write all the notes you need in this app\n"
                "5) Typing of the Death: a funny typing game made by the NextCMD Developer\n" 
                "6) System Info: see your system info with NextCMD\n"
                "7) Credits: see the credits of this proyect\n"
                "8) Exit the menu\n"
                "Your choice: ")
                
                if app_select in avaiable_apps and app_select in run_commands:
                    if app_select == "8":
                        shutdown()
                        running = False
                        clear()
                        break
                    else:
                        selected_app = App(avaiable_apps[app_select], run_commands[app_select])
                        Media.kaboom_media()
                        selected_app.ejecutar()
                        Media.start_loop_audio("DS_Shop.mp3")
                   
                else:
                    slow_print_white("You have to put a valid number, you fucking jew")
                    time.sleep(1)
                    clear()
                    continue
            except ValueError:
                slow_print_white("You have to use numbers, you chinese dog eater")
                time.sleep(1)
                clear()
                continue

clear()
run()
