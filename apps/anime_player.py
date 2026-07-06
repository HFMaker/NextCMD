import time
import os 
import subprocess
import json

if os.name == "nt":  
    os.system("taskkill /IM mpv.exe /F >nul 2>&1")
    os.system("taskkill /IM vlc.exe /F >nul 2>&1")

def slow_print_white(text, delay=0.02): 
    for char in text:
        print(f"\033[1;37m{char}\033[0m", end="", flush=True)
        time.sleep(delay)
    print()

playing_media = []

class Media:
    def __init__(self, name):
        self.name = name
    
    def start_loop_img(name):
        the_img = playmedia(name, video=True, loop=True)
        playing_media.append(the_img)
    
    def start_loop_audio(name):
        the_audio = playmedia(name, video=False, loop=True)
        playing_media.append(the_audio)
    
    def kaboom_media():
        for c in playing_media:
            c.kill()

def slow_input_white(text, delay=0.02): 
    for char in text:
        print(f"\033[1;37m{char}", end="", flush=True)
        time.sleep(delay)
    return input()

def obtener_episodios(anime_name):
    base_dir = os.path.dirname(__file__)
    try:
        anime_dir = os.path.join(base_dir, "animes", anime_name)
        episodes = [f for f in os.listdir(anime_dir) if f.endswith(".mp4")]
    
        episodes.sort(key=lambda ep: int(ep.split("E")[1].split(".")[0]))

        return episodes
    except FileNotFoundError:
        slow_print_white("[  ERROR  ] File not found")
        return None

def playanime(anime, episodio, video=True, save_position=True):
    try: 
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, "animes", anime, episodio)
        command = ["mpv"]

        flags = 0
        if os.name == "nt":
            flags = subprocess.CREATE_NEW_PROCESS_GROUP  | subprocess.CREATE_NO_WINDOW

        if save_position:
            command.append("--save-position-on-quit")

        command.append(path)

        player = subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=flags
        )
        player.wait()
    except FileNotFoundError:
        slow_print_white("[  ERROR  ] File not found")
        return None
    except OSError:
        slow_print_white("[  ERROR  ] Error while trying to execute mpv")
    except Exception as e:
        slow_print_white(f"[  ERROR  ] An error occurred: {e}")
        return None


def playmedia(archivo, video=False, loop=False):
    try: 
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, "assets", archivo)
        command = ["mpv"]

        flags = 0
        if os.name == "nt":
            flags = subprocess.CREATE_NEW_PROCESS_GROUP  | subprocess.CREATE_NO_WINDOW

        if not video:
            command.append("--no-video")
        if loop:
            command.append("--loop")

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
        slow_print_white(f"[ ERROR  ] An error occurred: {e}")
        return None

def select_episode_Rezero():

    clear()
    titulo()


    while True:
            
            menu = "=== AVAILABLE RE:ZERO EPISODES ===\n"
            episodios = obtener_episodios("ReZero")

            if not episodios:
                slow_print_white("No episodes detected")
                time.sleep(2)
                return False

            for idx, ep in enumerate(episodios):
                if ep[11] == ".":
                    menu += f"{idx+1}) Episode {ep[10]}\n"
                else:
                    menu += f"{idx+1}) Episode {ep[10:12]}\n"
                

            try:
                value = int(slow_input_white(menu + "Your choice: "))
            
            except ValueError:
                slow_print_white("[  ERROR  ] Invalid input. Please try again")
                time.sleep(1)
                clear()
                titulo()
                continue
    
            if value in range(1,7):
                slow_print_white(f"[  INFO  ] Loading Re:Zero Episode {value-1}...")
                loading_bar()
                Media.kaboom_media()
                slow_print_white("[  OK  ] Episode loaded!")
                playanime("ReZero", f"ReZero_T1E{value-1}.mp4")
                return False
            else:
                slow_print_white("[  ERROR  ] Inavalid input. Please try again")
                time.sleep(1)
                clear()
                titulo()
                            
def select_episode_SAO():

    clear()
    titulo()

    while True:
            
            menu = "=== AVAILABLE SAO EPISODES ===\n"
            episodios = obtener_episodios("SAO")

            if not episodios:
                slow_print_white("No episodes detected")
                time.sleep(2)
                return False

            for idx, ep in enumerate(episodios):
                if ep[8] == ".":
                    menu += f"{idx+1}) Episode {ep[7]}\n"
                else:
                    menu += f"{idx+1}) Episode {ep[7:9]}\n"
            
            try:
                value = int(slow_input_white(menu + "Your choice: "))
            
            except ValueError:
                slow_print_white("[  ERROR  ] Invalid input. Please try again")
                time.sleep(1)
                clear()
                titulo()
                continue
    
            if value in range(1,7):
                slow_print_white(f"[  INFO  ] Loading SAO Episode {value}...")
                loading_bar()
                Media.kaboom_media()
                slow_print_white("Episode loaded!")
                playanime("SAO",f"SAO_T1E{value}.mp4")
                return False
            else:
                slow_print_white("[  ERROR  ] Invalid input. Please try again")
                time.sleep(1)
                clear()
                titulo()

#--------------------------------
# FUNCION PARA LA MUSICA
#--------------------------------



def clear_screen():
    time.sleep(1)
    clear()
    titulo()

#-----------------------------------
# FUNCION PARA LIMPIAR LA TERMINAL
#-----------------------------------

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#--------------------------------
# FUNCION PARA LA BARRA DE CARGA
#--------------------------------

def loading_bar():

    total = 20

    for i in range(total + 1):
        barra = "#" * i + "-" * (total - i)
        print(f"\r\033[1;37m[{barra}] {i*5}%", end="")
        time.sleep(0.3)
    print()
   
def again_question(): 
    while True:

     
        again = slow_input_white("Would you like to go back to the anime selector? (y/n): ").lower()

        if again.lower() == "y":
            clear()
            return True
        
        elif again.lower() == "n":
            slow_print_white("[  INFO  ] Shutting down Anime Player...")
            loading_bar()
            print("[  OK  ] Done!")
            time.sleep(1)
            slow_print_white("[  INFO  ] Thanks for using Anime Player!")
            print()
            time.sleep(1)
            return False
        
        else:
            slow_print_white("[  ERROR  ] Invalid input. Please try again")
            clear_screen()
            
def titulo():

    print("   \ |           |    __|  \  | _ \\")
    print("  .  |  -_)\ \ /  _| (    |\/ | |  |")
    print(" _|\_|\___| _\_\\__|\___|_|  _|___/")
    print()
    print("   \       _)            _ \|")
    print("  _ \    \  |  ` \   -_) __/|  _` | |  |  -_)  _|")
    print("_/  _\_| _|_|_|_|_|\___|_| _|\__,_|\_, |\___|_|")
    print("                                   ___/")
    print()

#--------------------------------------------
# FUNCION QUE CORRE EL REPRODUCTOR DE ANIME
#--------------------------------------------

def run():
    
    def anime_player():

        Media.start_loop_audio("hola.mp3")
        running = True
        while running:

            while running:
                clear()
                titulo()

                try:
                    anime_select = int(slow_input_white("=== ANIME SELECTOR ===\n"
                    "1) SAO\n"
                    "2) Re:Zero\n" \
                    "3) Exit the anime player\n"
                    "Your choice: "))
                    
                    if anime_select in [1,2,3]:
                        break
                    else:
                        slow_print_white("[  ERROR  ] Invalid option. Please try again")
                        time.sleep(1)
                        clear()
                        continue
                except ValueError:
                    slow_print_white("[  ERROR  ] Invalid input. Please try again")
                    time.sleep(1)
                    clear()
                    continue

            while running:
        
                if anime_select in range (1,4):
                    
                        if anime_select == 1:
                            Media.kaboom_media()
                            select_episode_SAO()
                            if not again_question():
                                    running = False
                                    break
                            Media.start_loop_audio("hola.mp3")
                            break
                        if anime_select == 2:
                            Media.kaboom_media()
                            select_episode_Rezero()
                            if not again_question():
                                    running = False
                                    break
                            Media.start_loop_audio("hola.mp3")
                            break
                        if anime_select == 3:
                            Media.kaboom_media()
                            slow_print_white("[  INFO  ] Shutting down Anime Player...")
                            loading_bar()
                            slow_print_white("[  OK  ] Done!")
                            time.sleep(2)
                            slow_print_white("[  INFO  ] Thanks for using Anime Player!")
                            time.sleep(1)
                            running = False
                            clear()
                            break

                        if running:
                            if not again_question():
                                running = False
                                break
                
     
                                
    try:
        anime_player()
    finally:
        clear()
      
        

if __name__ == "__main__":
    clear()
    run()
