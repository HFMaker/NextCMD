import time
import os 
import subprocess
import platform
import psutil
import shutil
import socket


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

def exit_sysinfo():
    while True:
        slow_input_white("Press Enter to go back to the menu: ").lower()
        Media.kaboom_media()
        slow_print_white("[  INFO  ] Thanks for using System Info!")
        time.sleep(1)
        clear()
        return False

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

def slow_input_white(text, delay=0.02): 
    for char in text:
        print(f"\033[1;37m{char}\033[0m", end="", flush=True)
        time.sleep(delay)
    return input()


def titulo():

   print("  _  _         _    ___ __  __ ___    ___         ___       __       ")
   print(" | \| |_____ _| |_ / __|  \/  |   \  / __|_  _ __|_ _|_ _  / _|___   ")
   print(" | .` / -_) \ /  _| (__| |\/| | |) | \__ \ || (_-<| || ' \|  _/ _ \\ ")
   print(" |_|\_\___/_\_\\__|\___|_|  |_|___/  |___/\_, /__/___|_||_|_| \___/  ")
   print("                                          |__/                         ")
   print()


def run():
    titulo()
    print("OS:", platform.system(), platform.release())
    print("Architecture:", platform.machine())
    print("Hostname:", platform.node())
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("IP Address:", ip_address)
    print("Physical CPUs:", psutil.cpu_count(logical=False))
    print("Logical CPUs:", psutil.cpu_count(logical=True))
    ram = psutil.virtual_memory()
    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery: {battery.percent}% {'Charging' if battery.power_plugged else 'Not Charging'}")
    print("RAM:", round(ram.used / (1024**3), 2), "GB /", round(ram.total / (1024**3), 2), "GB")
    disk = shutil.disk_usage("/")
    print("Disk:", round(disk.used / (1024**3), 2), "GB /", round(disk.total / (1024**3), 2), "GB")

    if not exit_sysinfo():
        return False
   
if __name__ == "__main__":
    clear()
    run()
   
   
