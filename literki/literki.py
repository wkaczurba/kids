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

from funkcje import *

# while(True):
#     klawisz = getch().lower()
#     print(f"Wcisnal(les/las) {klawisz}")
#     graj(klawisz.decode())


for i in range(0, 10):
    print(i)

graj('dobrze7')
