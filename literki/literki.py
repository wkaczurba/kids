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

#graj("a")
import random

from funkcje import *

literki = ['a','b','c','d','e','f','g','h',
           'i','j','k','l','m','n','o','p',
           'q','r','s','t','u','w','x','y','z']

dobrze=0
zle=0

dzwieki_dobrze = ['dobrze','dobrze1',
            'dobrze2','dobrze3','dobrze4',
            'dobrze5','dobrze6','dobrze7','dobrze8']

for i in range(0, 2):
    print(f"Proba nr: {i}")

    losowa_literka = random.choice(literki)
    print(f"Losowa literka: {losowa_literka}")

    graj("wcisnij_literke")
    graj(losowa_literka)
    klawisz = czytaj_klawisz().lower()
    
    if (klawisz == losowa_literka):
        losowe_dobrze = random.choice(dzwieki_dobrze)
        graj(random.choice(dzwieki_dobrze))
        dobrze+=1
    else:
        graj('zle')
        zle+=1
    # if
    # graj(klawisz)

print("Wyniki:")
print(f"  dobrze: {dobrze}")
print(f"  zle: {zle}")
