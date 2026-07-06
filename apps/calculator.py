import time
import os
import subprocess
import sys

if os.name == "nt":  
    os.system("taskkill /IM mpv.exe /F >nul 2>&1")
    os.system("taskkill /IM vlc.exe /F >nul 2>&1")


#------------------------------------
# FUNCION PARA LIMPIAR LA TERMINAL
#------------------------------------

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#--------------------------------
# FUNCIONES PARA INPUTS Y TEXTOS
#--------------------------------

def slow_input(prompt, delay=0.02):
    for char in prompt:
        print(f"\033[1;37m{char}", end="", flush=True)
        time.sleep(delay)
    return input()

def slow_print(text, delay=0.02):
    for char in text:
        print(f"\033[1;37m{char}\033[0m", end="", flush=True)
        time.sleep(delay)
    print()

def loading_bar():
    total = 20
    for i in range(total + 1):
        barra = "#" * i + "-" * (total - i)
        print(f"\r\033[1;37m[{barra}] [{i*5}%]", end="")
        time.sleep(0.3)



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

        return subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=flags
        )
    except FileNotFoundError:
        slow_print("File not found")
        return None
    except OSError:
        slow_print("Error while trying to execute mpv")
    except Exception as e:
        slow_print(f"An error occurred: {e}")
        return None

def ask_number(number):
    while True:
        try:     
            num = float(slow_input(f"Choose your {number} number: "))
            return num
        except ValueError:
            slow_print("[  ERROR  ] Invalid input. Try again")
            time.sleep(1)
            clear()
            titulo()
            continue

playing_media = []

#--------------------------------------------
# FUNCION PARA SEGUIR USANDO LA CALCULADORA
#--------------------------------------------

def again_question(): 
    while True:

     
        again = slow_input("Do you want to continue? (y/n): ").lower()

        if again.lower() == "y":
            clear()
            titulo()
            return True
        
        elif again.lower() == "n":
            Media.kaboom_media()
            slow_print("[  INFO  ] Shutting down Calculator...")
            loading_bar()
            print()
            slow_print("[  OK  ] Done!")
            time.sleep(1)
            slow_print("[  INFO  ] Thanks for using Calculator!")
            print()
            time.sleep(1)
            return False
        
        else:
            slow_print("[  ERROR  ] Invalid input. Try again")
            clear_screen()

def clear_screen():
    time.sleep(1)
    clear()
    titulo()


def add(n1, n2):
    try: 
        return n1 + n2
    except OverflowError:
        slow_print("[  ERROR  ] Overflow Error has occurred")
def substract(n1,n2):
   try: 
        return n1 - n2
   except OverflowError:
        slow_print("[  ERROR  ] Overflow Error has occurred")
    
def multiply(n1,n2):
    try: 
        return n1 * n2
    except OverflowError:
        slow_print("[  ERROR  ] Overflow Error has occurred")
   
def divide(n1,n2):
    try: 
        return n1 / n2
    except ZeroDivisionError:
        slow_print("[  ERROR  ] Cannot divide by zero")
        return False
      
def module(n1,n2):
    try: 
        return n1 % n2
    except ZeroDivisionError:
        slow_print("[  ERROR  ] Cannot divide by zero")
        return False
       
def exponent(n1,n2):
    try: 
        return n1 ** n2
    except OverflowError:
        objection()
        
def ask_operation(num1, num2):
    while True: 
       
        try:
            value = int(slow_input(
        "--- OPERATIONS ---\n"
        "(1) Add\n"
        "(2) Substract\n"
        "(3) Multiply\n"
        "(4) Divide\n"
        "(5) Module\n"
        "(6) Exponent\n"
        "Your choice: "
    ))
          
            operations = {1: add, 2: substract, 3: multiply, 4: divide, 5: module, 6: exponent}
                
            if value not in operations:
                slow_print("[  ERROR  ] Invalid input. Try again")
                time.sleep(1)
                clear()
                titulo()
                continue
            else:
                slow_print("[  INFO  ] Calculating...")
                loading_bar()
                print("\n")
                result = operations[value](num1, num2)
                if result == None:
                    slow_print("The result is: you are an idiot")
                    time.sleep(1)
                    while True:
                        asnwer = slow_input("Type 'I admit I'm wrong' to continue: ")
                        if asnwer == "I admit I'm wrong":
                            slow_print("I think it's too late for you to admit that you're wrong, you know?")
                            time.sleep(2)
                            slow_print("Don't ever try to put a number like that in this calculator. Goodbye")
                            time.sleep(2)
                            sys.exit("The calculator has been closed due to a severe objection!")
                            break
                        else:
                            slow_print("No! Try again!")
                            time.sleep(1)
                else:
                    slow_print(f"The result is: {result}")
                time.sleep(1)
                return result
        except ValueError:
            slow_print("[  ERROR  ] Invalid input. Try again")
            clear_screen()
            continue


def objection_titulo():
    print("   ____  ____      ____________________________  _   ____ ")
    print("  / __ \/ __ )    / / ____/ ____/_  __/  _/ __ \/ | / / / ")
    print(" / / / / __  |_  / / __/ / /     / /  / // / / /  |/ / /  ")
    print("/ /_/ / /_/ / /_/ / /___/ /___  / / _/ // /_/ / /|  /_/   ")
    print("\____/_____/\____/_____/\____/ /_/ /___/\____/_/ |_(_)    ")

def objection():
    clear()
    Media.kaboom_media()
    objection_titulo()
    print()
    time.sleep(1)
    musica = play_media("ObjectionSong.mp3", video=False, loop=True)
    slow_print("Dear user, how dare you to put such a huge number in my sacred calculator!\n" 
    "¿Don't you know that numbers have limits, that universe itself cannot hold such mathematic mounstrosity?\n" 
    "We're talking about figures that would make atoms feel intimidated, about power that could unleash the IT error gods!\n" 
    "This court of logic and numerical order cannot allow such outrage. Every digit you've introduced is a direct affront to\n" 
    "logic itself, the fundamental laws of arimtetics and my dignity as a developer. A simple operation shouldn't\n" 
    "become into a cataclism of numbers! If you still want to stay in this mathematical madness path, may I tell you that not\n" 
    "only the software, but also the calculation fabric itself would colapse due to such abuse. That's why, I exhort, beg and\n" 
    "force you politely to think again about your choices, to go back to the path of reasonable numbers, and never, I repeat,\n" 
    "NEVER, to submit to such excessive numerical strength test. OBJECTION! EXTREME OBJECTION! Mathematical justice has\n" 
    "spoken, and your input has been considered invalid, unapropiated and offensive for this humble calculator. Take note\n" 
    "and amend your behaviour before the algorithm court decides to act harshly!", delay=0.02)
    time.sleep(3)
    clear()
    titulo()


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
        
        
#------------------------------------
# FUNCION PARA CORRER LA CLACULADORA
#------------------------------------

def titulo():
    print(" _   _           _    ____ __  __ ____     ____      _")
    print("| \ | | _____  _| |_ / ___|  \/  |  _ \   / ___|__ _| | ___")
    print("|  \| |/ _ \ \/ / __| |   | |\/| | | | | | |   / _` | |/ __|")
    print("| |\  |  __/>  <| |_| |___| |  | | |_| | | |__| (_| | | (__")
    print("|_| \_|\___/_/\_\\__|\____|_|  |_|____/   \____\__,_|_|\___|")
    print()

def run(): 
    Media.start_loop_img("DiddyBlud.png")
    Media.start_loop_audio("intro.mp3")
    titulo()
    print()
    def calculator():
        running = True

        while running: 
            number1 = ask_number("first")
            print()
            number2 = ask_number("second")
            print()
            ask_operation(number1, number2)

            if not again_question(): 
                    running = False
                    break  
                    
    try:
        calculator()
    finally:
        clear()

if __name__ == "__main__":
    clear()
    run()
