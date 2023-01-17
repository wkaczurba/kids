## Stuff for kids.

## Funkcje:

- `wypisz_pliki_audio()` - wypisuje wszystkie pliki audio ktore sa

- `graj( JAKISPLIK )` - gra plik audio JAKISPLIK, przyklady:

    ```python
    graj("a") # odtwarza literke "a".
    graj("dobrze") # odtwarza plik "dobrze"
    ```
    <b>UWAGA:</b> Plik musi istniec!

- `czytaj_klawisz()` - czeka na klawisz i zwraca jako wynik funkcji:

    ```python
    # przyklad 1:
    
    klawisz = czytaj_klawisz() # zapisuje pod zmienna klawisz wcisniety guzik

    # przyklad 2.:

    klawisz = czytaj_klawisz() # zapisuje pod zmienna klawisz wcisniety guzik
    print (klawisz) # wypisuje wcisniety guzik.
    ```        
  

## Zadanka:

1. Sprobuj kilka literek zeby przyczytal

    Czyli lecimy:

    ```python

    graj("a")
    graj("b")
    graj("c")
    graj("d")
    graj("e")
    graj("f")

    ```

2. Wypisz liste plikow audio

    Czyli lecimy:

    ```
    wypisz_pliki_audio()
    ```

3. Zagraj "wcisnij literke" a potem powiedz "d":

    ```python
    graj('wcisnij_literke')
    graj('g')
    ```

4. Zmien poprzednie na "wcisnij literke" a potem powiedz "a".

5. Zmien poprzednie na "wcisnij literke" a potem powiedz "p".

6. Zagraj "zle"

7. Zagraj "dobrze"   

8. Zagraj "wcisnij_literke2"

9. Zagraj "dobrze3"

10. Zagraj "dobrze7"

11. Wypisz na ekranie wcisniety guzik:

    ```python

    klawisz = czytaj_klawisz()
    print(f"Wcisnales guzik: {klawisz}")

    ```

12. Funkcja .lower() zmienia znak na maly:

    ```python

    zmienna = "A"
    print(zmienna.lower())

    ```

13. Zmien duzy wyraz: "LOLEK" na maly "lolek":

    ```python

    zmienna = "LOLEK"
    print(zmienna.lower())

    ```

14. Petla: 10 razy rob costam:

    <b>UWAGA:</b> Wciecia musza pozostac takie same!, czyli print wciety:

    ```python
    for i in range(0, 10):
        print("x")
    ```

15. Wypisz 5 razy "XD" zmieniajac petle powyzej    

16. Wypisz liczby od 0 do 9:

    ```python
    for i in range(0, 10):
        print(i)
    ```

17. Wypisz na ekranie 10 razy wcisniety guzik - w kolko:

    ```python
    for i in range(0, 10):
        klawisz = czytaj_klawisz().lower()
        print(f"Wcisnal(les/las) {klawisz}")
    ```

18. Wez guzik i zagraj:

    ```python
    klawisz = czytaj_klawisz().lower()
    graj(klawisz)
    ```

19. Dziesiec razy wez guzik i zagraj go:

    ```python
    for i in range(0, 10):
        klawisz = czytaj_klawisz().lower()
        graj(klawisz)
    ```

21. Pelny kod:


    ```python
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
    ```


