# Importy bibliotek:
# Depending on the OS - Windows or Linux - we pick getch (linux) or msvcrt.
from pygame import mixer
import time
import os
from glob import glob

from platform import system
if system() == 'Windows':
    from msvcrt import getch
else:
    from getch import getch

# import keyboard
# Audio = dzwiek

# Ustawienia dzwieku:
mixer.init()

def czytaj_klawisz():
    if system() == 'Windows':
        return getch().decode()
    else:
        return getch()


# Funkcja do grania dzwieków:
def graj(nazwa_pliku):
    filename_with_path = f"audio/{nazwa_pliku}.mp3";
    if ( glob(filename_with_path) == [] ):
        print (f"Blad: Nie znalazlem pliku: {nazwa_pliku}. Nie gram nic.")
        return
    #print (f"Gram {nazwa_pliku}")

    mixer.music.load(filename_with_path)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

# Wypisuje wszystkie pliki:
def wypisz_pliki_audio():
    pliki = glob("audio/*.mp3")
    pliki.sort()
    for plik in pliki:
        if system() == 'Windows':
            p = plik.replace("audio\\", "")
        else:
            p = plik.replace("audio/", "")
        p = p.replace(".mp3", "")
        print(p)
