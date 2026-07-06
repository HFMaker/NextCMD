import time
import os
import subprocess
import random

def loading_bar():
    total = 20
    for i in range(total + 1):
        barra = "#" * i + "-" * (total - i)
        print(f"\r\033[1;37m[{barra}] {i*5}%", end="")
        time.sleep(0.3)
    print()

words = ["sol", "pan", "ahí", "dos", "uno", "pez", "sal", "ver", "luz", "dar", "mil", "col", "fue", "del", "nos", "tus",
         "cual", "dios", "soñar", "gato", "coliflor", "macarrones", "anime"
         , "discutir", "estudiar", "reir", "felicidad", "castillo", "poker", "arbusto", "españa", "aula", "vaso", "hola", "persona"
         , "cine", "ayudar", "escucha", "porrista", "eloy", "pescado", "carne", "personal", "serie", "python", "esternocleidomastoideo"
         , "parrilla", "gerardo", "hotel", "bolas", "huevo", "militar", "que", "cuando", "chaval", "hierro", "física", "javascript", "nextcmd"
         , "jota", "pellejo", "animales", "boca", "verso", "poeta", "dios", "crucificar", "personaje", "principal", "coche", "moto", "avión"
         , "sartén", "mejilla", "gimnasio", "calistenia", "alboroto", "zancadilla", "flexión", "núcleo", "dominadas", "estrepitoso", "tostadora",
         "microondas", "hardware", "software", "antimateria", "molino", "universidad", "instituto", "pesadilla", "familia", "orden", "pensar", 
         "único", "diferente", "habitación", "álgebra", "guapo", "festín", "muletilla", "denuncia", "videojuego",
         "linux", "kernel", "ventilador", "disipador", "ram", "teclado", "ratón", "placa", "gráfica", "fuente", "alimentación", "paralelepípedo",
         "añoranza", "engreido", "supercalifragilisticoespialidoso", "otorrinolaringólogo", "sudadera", "colchón","perro",
         "cuadro", "museo", "edificio", "ventana", "apuesta", "cigarro", "caja", "porro", "gorra", "arco", "espada", "lanza", "mandoble", "general",
         "retumbar", "ganador", "puñetazo", "arrancar", "respuesta", "metralleta", "gazpacho", "horca", "tétrico", "escolar", "comodín", 
         "xilófono", "yegua", "zarandear", "sintético", "pendrive", "torre", "pared", "barra", "tortilla", "tomate", "mostaza", "paisaje", "notorio",
         "galopar", "ridículo", "decimal", "coma", "flotante", "asignación", "memoria", "espacio", "contiguo", "intérprete", "comandos" ,"tumbar",
         "internet", "redes", "locales", "fútbol", "rugby", "karate", "baloncesto", "manecilla", "reloj", "hora", "minutos", "segundos", "zorro", 
         "cable", "pelear", "babuino", "vela", "oscuridad", "racismo", "feminista" ,"árabe", "estadounidense", "infinito", "imaginario", "persiana",
         "lunático", "monitor", "soporte", "desarrollador", "china", "créditos", "sociales", "mancha", "gas", "judío", "yate", "pala", "caballero",
         "escalera", "color", "trío", "pareja", "dolores", "muerto", "mecanografía", "proceso", "introducir", "caracteres", "alfanuméricos", "medio",
         "escribir", "antigua", "grecia", "sócrates", "mi", "pasado", "entera", "buscando", "siguiente", "escalón", "convencido", "tejado", "lado",
         "vereda", "atrás", "marchar", "regadera", "hierba", "brotar", "campo", "soldados", "juguetes", "flores", "madera", "repartirse", "entierren",
          "muerte", "traicionera", "cajón", "sembrando", "algodón", "horas", "gente", "dentro", "televisor", "alguna", "canción", "sandeces", "amor",
           "ombligo", "marque", "harto", "dudas", "preguntarle", "viento", "ocupo", "salir", "beber", "rollo", "joder", "besos", "sube", "espantado",
            "nubes", "acuerdo", "nada", "colores", "flores", "toco", "suelo", "rallas", "día", "grupo", "metido", "casa", "saludan", "seguro", "perdido",
            "gastado", "empedrado", "humilde", "protesto", "abogado", "colgado", "ingeniería", "aeroespacial", "termodinámica", "filosofía", "paleta",
            "gordo", "flaco", "barco", "olla", "youtube", "destrozado", "retirado", "pastilla", "freno", "levantado", "energía", "cárcel", "salida",
            "historia", "malentendido", "risueño", "empalado", "electrocutación", "omega", "mango", "alfombrilla", "radiador", "mochila", "libro", "estuche",
            "peluche", "funda", "móvil", "hilo", "espátula", "barril", "mundo", "ensamblador", "compilador", "pañuelos", "coleccionable", "maestro", 
            "mensajes", "chatear", "meme", "operativo", "sábanas", "almohada", "pijama", "zapatillas", "moreno", "crema", "castaño", "feria", "buñuelos",
            "atracción", "globo", "azúcar", "artificiales", "programación", "sobrecarga", "progresivo", "respaldo", "asiento", "koala", "leche", "torrija",
            "mensuales", "débito", "tarjeta", "sonrisa", "amistades", "amigo", "romance", "aldeano", "paladín", "hechicero", "escudero", "mechero", "mando",
            "bolígrafo", "regla", "sacapuntas", "mercurio", "venus", "tierra", "marte", "júpiter", "saturno", "urano", "neptuno", "helio", "magnesio", "calcio",
            "azufre", "oro", "plata", "cristal", "esmeralda", "rutherfordio", "borio", "einstenio", "xeón", "kriptón", "litio", "potasio", "rubidio", "berilio",
            "estroncio", "wolframio", "yodo", "fósforo", "cloro", "depender", "profundos", "autoridad", "inclinación", "clases", "escritas", "captura", "curiosa",
            "termina", "sustancial","imaginaba", "regresó", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo", "moscas", "actualización", 
            "biblioteca", "auricular", "huesos", "quitar", "canal", "demostración", "contemplaba", "magdalena", "adhesión", "cooperación", "formada", "amarilla",
            "opera", "saludar", "abandono", "ediciones", "campañas", "tiendas", "logaritmo", "hipotenusa", "vacilase", "virus", "insoportable", "estallido", "guerra",
            "perdieron", "defendido", "enormemente", "griega", "mirador", "cubre", "inteligente", "cocción", "puertas", "enero", "febrero", "marzo", "abril", "mayo",
            "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre", "científicos", "casualidad", "espejo", "walkman", "ensalada", "ketchup", "bastión",
            "repetitivo", "contradicciones", "internacionalmente", "lógico", "mexicano", "referéndum", "asamblea", "palacio", "moncloa", "crónicas", "loco", "tierno", "sapo",
            "hombre", "libre", "sentimiento", "asco", "terror", "manga", "jalapeño", "gongonzola", "guardameta", "portero", "apartamento", "whisky", "ginebra", "vodka",
            "tomé", "elegir", "ibérico", "jamón", "habíamos", "adultos", "tormenta"]

english_words = [
    "hi", "hello", "world", "test", "code", "game", "play", "win", "lose", "time",
    "fast", "slow", "hard", "easy", "score", "combo", "level", "start", "end",
    "keyboard", "screen", "input", "output", "random", "value", "string", "number",
    "computer", "science", "python", "program", "developer", "engineer", "logic",
    "system", "memory", "process", "thread", "function", "variable", "loop",
    "condition", "object", "class", "method", "array", "list", "dictionary",
    "network", "server", "client", "internet", "protocol", "packet", "signal",
    "debug", "error", "exception", "compile", "execute", "binary", "decimal",
    "algorithm", "structure", "pointer", "reference", "stack", "queue",
    "performance", "optimization", "efficiency", "hardware", "software",
    "keyboard", "monitor", "mouse", "speaker", "microphone",
    "dragon", "sword", "magic", "wizard", "knight", "battle", "enemy", "boss",
    "attack", "defense", "power", "energy", "speed", "focus", "skill",
    "victory", "defeat", "danger", "shadow", "light", "fire", "water", "earth",
    "wind", "storm", "thunder", "ice", "flame", "darkness", "spirit",
    "adventure", "journey", "mission", "quest", "treasure", "map", "island",
    "forest", "desert", "mountain", "ocean", "river", "valley",
    "future", "past", "present", "dream", "reality", "vision", "mind",
    "thought", "idea", "creation", "design", "build", "destroy",
    "typing", "speed", "accuracy", "reaction", "challenge", "progress",
    "improve", "practice", "master", "expert", "legend", "ultimate", "racism", "kill",
    "trending", "topic", "amphersand", "youtube", "compiler", "realize", "redo", "hoverboard",
    "monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "january", "february",
    "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "welcome", 
    "paradise", "brain", "stew", "dreams", "boullevard", "building", "report", "hacker", "washing", "rotten", "carry",
    "usefull", "otter", "dolphin", "emulator", "console", "kernel", "logged", "humble", "sacred", "court", "attorney", "killer",
    "serial", "logical", "brotherhood", "madness", "path", "base", "directory", "dread", "burn", "local", "area", "hoodie", "flash", "before",
    "burning", "remember", "anything", "waking", "up", "see", "cannot", "truth", "wholesome", "store", "final", "fantasy", "over", "top", "jeans",
    "deodorant", "plaza", "sadness", "gym", "control", "potato", "water", "stupid", "idiot", "stick", "south", "north", "east", "west", "sponge",
    "star", "card", "shortcut", "beaber", "rust", "poster",  "database", "storage", "security", "access", "backup",
    "virtual", "digital", "automatic", "interactive",
    "challenge", "competition", "achievement", "success", "failure",
    "progression", "difficulty", "reaction", "precision",
    "keyboard", "typing", "letters", "words", "sentence",
    "practice", "training", "learning", "improvement",
    "fantasy", "monster", "creature", "warrior", "guardian",
    "legendary", "epic", "mythical", "invisible", "immortal",
    "galaxy", "planet", "universe", "gravity", "cosmic",
    "quantum", "energy", "particle", "dimension",
    "strategy", "tactics", "decision", "planning",
    "survival", "escape", "mission", "objective",
    "ultimate", "maximum", "minimum", "average",
    "randomize", "generate", "calculate", "simulate",
    "interface", "display", "render", "execute", "anchor", "blade", "shield", "helmet", "armor", "dagger",
    "charge", "strike", "impact", "slash", "pierce",
    "guardian", "sentinel", "champion", "fighter", "raider",
    "capture", "defend", "invade", "retreat", "advance",
    "checkpoint", "spawn", "respawn", "cooldown", "upgrade",
    "inventory", "equipment", "ability", "skilltree",
    "physics", "gravity", "velocity", "momentum", "friction",
    "neutron", "proton", "electron", "atom", "molecule",
    "calculus", "geometry", "equation", "formula", "matrix",
    "terminal", "command", "script", "shell", "processes",
    "multithread", "parallel", "concurrent", "runtime",
    "encryption", "decryption", "firewall", "malware",
    "firmware", "driver", "chipset", "bandwidth",
    "latency", "throughput", "compression", "decompression",
    "rendering", "animation", "texture", "polygon",
    "framework", "library", "dependency", "package",
    "installer", "repository", "versioning",
    "scripting", "automation", "integration",
    "feedback", "response", "interaction", "trigger",
    "difficulty", "scaling", "progression", "ranking",
    "leaderboard", "achievement", "milestone",
    "precision", "consistency", "endurance",
    "awareness", "reflex", "coordination",
    "strategy", "adaptation", "prediction",
    "dangerzone", "overdrive", "overheat",
    "critical", "overload", "limitbreak",
    "awakening", "berserk", "ultimateform",
    "hyperdrive", "teleport", "phase", "shift",
    "dimension", "portal", "rift", "void",
    "glitch", "bugfix", "hotfix", "patch",
    "sandbox", "openworld", "storymode",
    "hardcore", "casual", "arcade", "survivalmode",
    "checkpoint", "permadeath", "revive",
    "leader", "follower", "ally", "opponent",
    "spectator", "challenger", "contender",
    "reactiontime", "keypress", "keystroke",
    "accuracyrate", "inputlag", "frames",
    "framerate", "refresh", "sync", "tearing" "we", "you", "they", "them", "anxious", "discord", "apple", "banana",
    "hoppers", "poker", "straight", "flush", "technical", "issue", "apology", "loot", "scout", "doctor", "cartoon",
    "matress", "album", "one", "king","nothing", "lightning", "thunderstruck", "edge", "call", "anesthesia",
    "shenanigans", "battlegrounds", "valley", "spiral", "super", "activated", "grapes", "epstein", "diddy", "island",
    "new", "old", "stranger", "things", "walking", "death", "permaban", "structured", "millenial", "generations",
    "instagram", "meme", "six", "seven", "children", "family", "punch", "lunch", "colission", "latex", "sexy", "wuthering", "waves",
    "rail", "terminator", "yolk", "rare", "find", "escape", "facility", "flee", "mosquitoe", "goal", "reservation", "borderline",
    "amazon", "sweater", "jumper", "painting", "spacebar", "entry", "loading", "screen", "bastard", "waste", "timing", "recruit",
    "locked", "capable", "of", "windy", "foggy", "tracert", "packet", "sending", "waker", "schedule" ]
numbers = ["78", "11", "827", "28", "381", "54342", "0123", "923", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
           "67", "420", "21", "9999", "71892", "92", "1183", "8301", "10", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "22", "23", "24", "25", "26", "27", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42",
    "43", "44", "45", "46", "47", "48", "49", "50", "51", "52","53", "54", "55", "56", "57", "58", "59", "60", "61", "62",
    "101", "111", "123", "234", "345", "456", "567", "678", "789","147", "258", "369", "159", "357", "951", "753",
    "100", "200", "300", "400", "500", "600", "700", "800", "900", "1000", "2000", "3000", "4000", "5000",
    "2023", "2025", "1987", "1999", "2001", "2012", "1110", "2220", "3330", "4440", "5550","121", "131", "141", "151", "161", "171", "181", "191",
    "246", "864", "975", "531", "642", "7531","10000", "25000", "50000", "75000","31415", "27182", "16180", "14142",
    "123456", "654321", "112233", "221133", "334455", "98765", "87654", "76543", "65432", "54321", "102938", "564738", "918273", "837261" ,
    "63", "64", "65", "66", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "79", "80", "81", "82", "83", "84",
    "85", "86", "87", "88", "89", "90", "91", "93", "94", "95","96", "97", "98", "99",
    "124", "235", "346", "457", "568", "679", "781", "892","213", "324", "435", "546", "657", "768", "879",
    "110", "220", "330", "440", "660", "770", "880","2024", "2010", "2015", "1995", "1980", "1975","1221", "1331", "1441", "1551", "1661", "1771", "1881",
    "2112", "2332", "2442", "2552", "2662", "2772","4321", "6789", "7890", "8901", "9012",
    "1357", "2468", "97531", "86420","11111", "22222", "33333", "44444", "55555","10101", "20202", "30303", "40404", "50505",
    "123321", "456654", "789987","111222", "222333", "333444", "444555","9876543", "1234567", "7654321","246810", "1357911","314159", "271828", "161803",
    "99999", "88888", "77777", "66666","112358", "223344", "556677","100000", "200000", "300000","102", "103", "104", "105", "106", "107", "108", "109",
    "210", "310", "410", "510", "610", "710", "810", "910","432", "543", "654", "765", "876", "987","3210", "2109", "1098", "9087",
    "1112", "1222", "1333", "1444", "1555","1666", "1777", "1888", "1999","2111", "3222", "4333", "5444", "6555","1200", "1300", "1400", "1500", "1600",
    "1700", "1800", "1900","24680", "13579", "864209", "975310","10001", "20002", "30003", "40004", "50005","121212", "343434", "565656", "787878",
    "909090", "808080", "707070","111000", "222000", "333000", "444000","654987", "321654", "789123","147258369", "963852741","112211", "223322", "334433",
    "1000000", "2000000", "5000000","76543210", "87654321", "98765432","10101010", "20202020", "30303030","3141592", "2718281", "1618033",
    "9091", "8081", "7071", "6061","555666", "666777", "777888","43210", "543210", "6543210","1060", "1070", "1080", "1090","1160", "1170", "1180", "1190",
    "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009","2121", "2323", "2525", "2727", "2929","4141", "4343", "4545", "4747", "4949",
    "6161", "6363", "6565", "6767", "6969","8181", "8383", "8585", "8787", "8989","246246", "135135", "987987", "654654", "101001", "202002", "303003", "404004",
    "123123", "321321", "456456", "6546540", "100200", "200300", "300400", "400500", "567890", "678901", "789012", "890123","111222333", "222333444", "333444555",
    "12341234", "23452345", "34563456","80808", "90909", "70707", "60606","112244", "224466", "336688", "448800","999000", "888000", "777000", "666000",
    "10203040", "20304050", "30405060","111333", "222444", "333555", "444666","909192", "808182", "707172","654789", "789654", "321987", "987321",
    "555000", "444000", "3330000","24682468", "13571357","101112", "121314", "141516","10000000", "20000000", "30000000"]

def start_game(mode):
    time.sleep(1)
    refresh_screen()
    Media.start_loop_audio("hola.mp3")
    score = 0
    aciertos = 0
    errores = 0
    time_left = 60
    combo = 0
    max_combo = 0
    show_combo = "1.0X"
    combo_message = ""
    while time_left > 0:
        print(f"TIME LEFT: {int(time_left)}s")
        print(f"COMBO: {combo} ({show_combo}) {combo_message}")
        start_time = time.time()
        word_to_type = mode[random.randint(0, len(mode) - 1)]
        print(f"WORD: {word_to_type}")
        typed_word = input("Type the word: ")
        end_time = time.time()
        used_time = end_time - start_time
        time_left -= used_time
        if typed_word == word_to_type:
            if combo in [0,1,2,3,4]:
                Media.start_normal_audio("correct_sound.mp3")
                score += 100
                aciertos += 1
                time_left +=1
                combo += 1
                if combo > max_combo:
                    max_combo = combo
            elif combo in [5,6,7,8]:
                Media.start_normal_audio("correct_sound.mp3")
                score += 100 * 1.2
                aciertos += 1
                time_left +=1
                combo += 1
                show_combo = "1.2X"
                combo_message = "NICE 👍"
                if combo > max_combo:
                    max_combo = combo
            elif combo in [9,10,11,12]:
                Media.start_normal_audio("correct_sound.mp3")
                score += 100 * 1.5
                aciertos += 1
                time_left +=1
                combo += 1
                show_combo = "1.5X"
                combo_message = "GREAT 😎"
                if combo > max_combo:
                    max_combo = combo
            elif combo in [13,14,15,16]:
                Media.start_normal_audio("correct_sound.mp3")
                score += 100 * 2
                aciertos += 1
                time_left +=1
                combo += 1
                show_combo = "2.0X"
                combo_message = "INSANE 😈"
                if combo > max_combo:
                    max_combo = combo
            elif combo >= 17:
                Media.start_normal_audio("correct_sound.mp3")
                score += 100 * 2.5
                aciertos += 1
                time_left +=1
                combo += 1
                show_combo = "2.5X (MAX)"
                combo_message = "GODLIKE 🔥"
                if combo > max_combo:
                    max_combo = combo
                if combo >= 30:
                    combo_message = "NEXTCMD TIER 💻⚡"
                if combo >= 50:
                    combo_message = "COHÉN BURGERS TIER 🍔🍳"
                if combo >= 70:
                    combo_message = "CREATOR'S TIER 🐱🐈‍⬛"
            refresh_screen()
        else:
            Media.start_normal_audio("incorrect_sound.mp3")
            time_left -=4
            score -= 50
            errores += 1
            combo = 0
            show_combo = "1.0X"
            combo_message = ""
            refresh_screen()

    Media.kaboom_media()
    clear()
    game_over_titulo()
    palabras_totales = aciertos + errores
    display_mode = mode
    slow_print("=== RESULTS ===")
    time.sleep(1)
    if display_mode == words:
        slow_print("MODE: Word (Spanish)")
    elif display_mode == english_words:
        slow_print("MODE: Word (English)")
    elif display_mode == numbers:
        slow_print("MODE: Number")
    time.sleep(1)
    slow_print(f"FINAL SCORE: {int(score)}")
    time.sleep(1)
    slow_print(f"HIGHEST COMBO: {max_combo}")
    time.sleep(1)
    slow_print(f"TOTAL CORRECT WORDS: {aciertos}")
    time.sleep(1)
    slow_print(f"TOTAL ERRORS: {errores}")
    time.sleep(1)
    slow_print(f"PRECISION: {int((aciertos/palabras_totales)*100)}%")
    time.sleep(1)
  
def again_question(): 
    while True:
        again = slow_input("Would you like to go back to the TOTD menu? (y/n): ").lower()
        if again.lower() == "y":
            Media.kaboom_media()
            return True
        elif again.lower() == "n":
            shutdown()
            return False
        else:
            slow_print("[  ERROR  ] Invalid input. Try again")


def stop_typing_of_the_death_music():
    if os.name == "nt":  
        os.system("taskkill /IM mpv.exe /F >nul 2>&1")


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

    print("  ______          _                  ___  __  __         ___           __  __    ")
    print(" /_  __/_ _____  (_)__  ___ _  ___  / _/ / /_/ /  ___   / _ \___ ___ _/ /_/ /    ")
    print("  / / / // / _ \/ / _ \/ _ `/ / _ \/ _/ / __/ _ \/ -_) / // / -_) _ `/ __/ _ \   ")
    print(" /_/  \_, / .__/_/_//_/\_, /  \___/_/   \__/_//_/\__/ /____/\__/\_,_/\__/_//_/   ") 
    print("      /___/_/          /___/                                                     ")
    print()

def game_over_titulo():

   print("  ________   __  _______  ____ _   _________   ")
   print(" / ___/ _ | /  |/  / __/ / __ \ | / / __/ _ \  ")
   print("/ (_ / __ |/ /|_/ / _/  / /_/ / |/ / _// , _/  ")
   print("\___/_/ |_/_/  /_/___/  \____/|___/___/_/|_|   ")
   print()


   

def refresh_screen():
    clear()
    titulo()

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

    def start_normal_audio(name):
        the_audio = play_media(name, video=False, loop=False)
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
        slow_print("[ ERROR  ] File not found")
        return None
    except OSError:
        slow_print("[  ERROR  ] Error while trying to execute mpv")
    except Exception as e:
        slow_print(f"[  ERROR  ] An error occurred: {e}")
        return None

def shutdown():
    Media.kaboom_media()
    slow_print("[  INFO  ] Shutting down Typing of the Death...")
    loading_bar()
    slow_print("[  OK  ] Done!")
    time.sleep(1)
    slow_print("[  INFO  ] Thanks for playing Typing of the Death!")
    time.sleep(1)
    clear()
    return False

def run():
    def typing_of_the_death_menu():
        running = True
        while running:
            try:
                refresh_screen()
                print()
                options = {1: start_game, 2: start_game, 3: start_game, 4: shutdown}
                mode = {1: words, 2: english_words, 3: numbers, 4:"hola"}
                selection = int(slow_input("=== OPTIONS ===\n"
                            "1) Play Word Mode (Spanish)\n"
                            "2) Play Word Mode (English)\n"
                            "3) Play Number Mode\n"
                            "4) Exit\n" 
                            "Your choice: "))
                if selection in options and selection in mode:
                    if selection == 4:
                        options[selection]()
                        running = False
                        break
                    else:
                        Media.kaboom_media()
                        slow_print("[  INFO  ] Loading game...")
                        time.sleep(3)
                        options[selection](mode[selection])
                        
                        
                else:
                    slow_print("[  ERROR  ] Invalid option number. Please try again")
                    clear_screen()
                    continue
            except ValueError:
                slow_print("[  ERROR  ] Invalid input. Please try again")
                clear_screen()
                continue


            if not again_question():
                running = False
                break

    typing_of_the_death_menu()

if __name__ == "__main__":
    clear()
    run()
