import time
import os
import json
import subprocess
import random

def loading_bar():
    total = 20
    for i in range(total + 1):
        barra = "#" * i + "-" * (total - i)
        print(f"\r\033[1;37m[{barra}] [{i*5}%]", end="")
        time.sleep(0.3)
    print()

plus_social_credits_keywords = ["i love china","i only play games for 2h", "nothing happened on tiananmen square",
                                "my social credit score is perfect", "i respect authority all the time", "i follow all the rules", "i do not critizice anything"]

minus_social_credits_keywords = ["china is bad", "i blame people for my problems", "i don't help my family", "i don't want to visit china", "i don't like huawei",
                                "i don't follow any rules", "my social credit socre is ass", "i always critizice", "i hate helping others", "i'm not a doctor yet",
                                "i'm racist"]

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
        slow_print("[  ERROR  ] File not found")
        return None
    except OSError:
        slow_print("[  ERROR  ] Error while trying to execute mpv")
    except Exception as e:
        slow_print(f"[  ERROR  ] An error occurred: {e}")
        return None


if os.name == "nt":  
    os.system("taskkill /IM mpv.exe /F >nul 2>&1")
    os.system("taskkill /IM vlc.exe /F >nul 2>&1")

def clear_screen():
    time.sleep(1)
    clear()
    titulo()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def slow_print(text, delay=0.02):
    for char in text:
        print(f"\033[1;37m{char}", end="", flush=True)
        time.sleep(delay)
    print()

def slow_input(text, delay=0.02):
    for f in text:
        print(f"\033[1;37m{f}", end="", flush=True)
        time.sleep(delay)
    return input()

def titulo():

    print("   _  __        __  _______  ______    _  __     __        ")
    print("  / |/ /____ __/ /_/ ___/  |/  / _ \  / |/ /__  / /____ ___")
    print(" /    / -_) \ / __/ /__/ /|_/ / // / /    / _ \/ __/ -_|_-<")
    print("/_/|_/\__/_\_\\__/\___/_/  /_/____/ /_/|_/\___/\__/\__/___/")
    print()

archivo_notas = "note_logger.json"

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, archivo_notas)

def show_notes(notas):
    if not notas:
        slow_print("[  INFO  ] No notes found.")
        clear_screen()
        return
    else:
        refresh_screen()
        slow_print("== ALL NOTES ==")
        for i, n in enumerate(notas, 1):
            ts = time.localtime(n["timestamp"])
            fecha = time.strftime("%Y-%m-%d %H:%M:%S", ts)
            slow_print(f'{i}. [{fecha}] {n["nota"]}', delay=0.004)
        slow_input("Press Enter to go back to the menu: ")
        return 

def delete_note(notes):
    if not notes:
        slow_print("[  INFO ] No notes found to delete")
        clear_screen()
        return
    else:
        refresh_screen()
        slow_print("== ALL NOTES ==")
        for i, n in enumerate(notes, 1):
            ts = time.localtime(n["timestamp"])
            fecha = time.strftime("%Y-%m-%d %H:%M:%S", ts)
            slow_print(f'{i}. [{fecha}] {n["nota"]}', delay=0.004)
        while True:
            try:
                deleted_note = int(slow_input("Which note number would you like to delete?: "))
                if 1 <= deleted_note <= len(notes):
                    while True:
                        confirmation = slow_input("Are you sure you want to delete the note? (y/n): ")
                        if confirmation.lower() == "y":
                            slow_print("[  INFO  ] Deleting note...")
                            time.sleep(2)
                            notes.pop(deleted_note -1)
                            save_notes(notes)
                            slow_print("[  OK  ] Note succesfully deleted!")
                            if notes:
                                if len(notes) > 1:
                                    slow_print(f"[  INFO  ] There are {len(notes)} notes left")
                                else:
                                    slow_print("[  INFO  ] There is one note left")
                            else:
                                slow_print("[  INFO  ] There are no notes left")
                            slow_input("Prees Enter to go back to the menu")
                            return 
                        elif confirmation == "n":
                            slow_print("[  INFO  ] Aborting...")
                            time.sleep(1)
                            return 
                        else:
                            slow_print("[  ERROR  ] Invalid input. Try again")
                else:
                    slow_print("[  ERROR  ] Note number not in registered notes. Please try another note number")
            except ValueError:
                slow_print("[  ERROR  ] Invalid input, please try again")

def refresh_screen():
    clear()
    titulo()

def load_notes():
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def shutdown():
    Media.kaboom_media()
    slow_print("[  INFO  ] Shutting down Notes...")
    loading_bar()
    slow_print("[  OK  ] Done!")
    time.sleep(1)
    slow_print("[  INFO  ] Thanks for using NextCMD Notes!")
    time.sleep(1)
    clear()

def save_notes(notes):
    with open(path, "w") as f:
        json.dump(notes, f, indent=2)

def new_note(notes):
    text = slow_input("Write your note here: ")
    if text.lower() in plus_social_credits_keywords:
        Media.kaboom_media()
        music = play_media("ChineseMusic.mp3", video=False)
        image = play_media("+social_credits.png", video=True, loop=True)
        music.wait()
        music.terminate()
        image.terminate()
    elif text.lower() in minus_social_credits_keywords:
        Media.kaboom_media()
        music = play_media("siren_meme.mp3", video=False)
        image = play_media("no_social_credits.png", video=True, loop=True)
        music.wait()
        music.terminate()
        image.terminate()
    note = {"nota": text, "timestamp": time.time()}
    notes.append(note)
    save_notes(notes)
    slow_print("Note saved!")
    clear_screen()

def run():
    def notas_menu():
        notes = load_notes()
        while True:
            try:
                refresh_screen()
                options = {1: show_notes, 2: new_note, 3: delete_note}
                selection = int(slow_input("=== CHOOSE AN OPTION ===\n"
                            "1) Show notes\n"
                            "2) New note\n" \
                            "3) Delete note\n"
                            "4) Exit\n"
                            "Your choice: "))
                if selection in options:
                    options[selection](notes)
                else:
                    if selection == 4:
                        shutdown()
                        return False
                    else:
                        slow_print("[  ERROR  ] Invalid option number. Please try again")
                        clear_screen()
            except ValueError:
                slow_print("[  ERROR  ] Invalid input. Please try again")
                clear_screen()

    notas_menu()

if __name__ == "__main__":
    run()
