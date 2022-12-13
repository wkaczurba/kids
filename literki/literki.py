# Importy bibliotek:
# Depending on the OS - Windows or Linux - we pick getch (linux) or msvcrt.
from getch import getch
import time
import os
# import keyboard
from glob import glob

# Audio = dzwiek

# Ustawienia dzwieku:
mixer.init()

# Funkcja do grania dzwieków:
def graj(nazwa_pliku):
    filename_with_path = f"audio/{nazwa_pliku}.mp3";
    if ( glob(filename_with_path) == [] ):
        print (f"Blad: Nie znalazlem pliku: {nazwa_pliku}. Nie gram nic.")
        return
    print (f"Gram {nazwa_pliku}")

    mixer.music.load(filename_with_path)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

# Wypisuje wszystkie pliki:
def wypisz_pliki_audio():
    pliki = glob("audio/*.mp3")
    pliki.sort()
    for plik in pliki:
        p = plik.replace("audio/", "")
        p = p.replace(".mp3", "")
        print(p)

#
# Twoj kod:
# 
# Funkcje:
#   wypisz_pliki_audio() - wypisuje wszystkie pliki audio ktore sa
#
#   graj( JAKISPLIK ) - gra plik audio JAKISPLIK, 
#      przyklady:
#         graj("a") odtwarza literke "a".
#         graj("dobrze") - odtwarza plik "dobrze"
#
#
#   getch() - czeka na klawisz i zwraca jako wynik funkcji:
#
#         przyklad 1.:
#            klawisz = getch()  -  zapisuje pod zmienna klawisz wcisniety guzik
# 
#         przyklad 2.:
#            klawisz = getch()  -  zapisuje pod zmienna klawisz wcisniety guzik
#            print (klawisz) - wypisuje wcisniety guzik.
#
#
#         
#   

# Zadanka:
#    1. sprobuj kilka literek zeby przyczytal
#    2. wypisz liste plikow audio
#

graj("a")