from random import randrange
import sys, os

liczba_gier      = 100000
konto_alicji     = 0
konto_piotra     = 0
liczba_wygranych = {"Alicja":0, "Piotr":0}

def nie_drukuj():
    sys.stdout = open(os.devnull, 'w')
def drukuj():
    sys.stdout = sys.__stdout__

def rzuty_kostka(limit_rzotow=3):
    licznik_rzutow = 0
    wynik_kosci1   = 0
    wynik_kosci2   = 0
    suma_z_rzutow  = 0
    rzut_za_1      = 0

    while rzut_za_1 == 0 and limit_rzotow > licznik_rzutow:        
        wynik_kosci1 = randrange(1,6,1)
        wynik_kosci2 = randrange(1,6,1)
        licznik_rzutow += 1
        suma_z_rzutow += wynik_kosci1 + wynik_kosci2
        rzut_za_1 = 1 if wynik_kosci1 == 1 or wynik_kosci2 == 1 else 0
    return suma_z_rzutow if rzut_za_1 == 0 else 0 

def piotr(konto_piotra,konto_alicji):
    if konto_alicji >= 100:
        print("Alicja zwyciężyła! kończymy grę")
        return "Alicja"
    else:
        konto_piotra += rzuty_kostka()
        return alicja(konto_alicji=konto_alicji,konto_piotra=konto_piotra)
    
def alicja(konto_alicji, konto_piotra):    
    if konto_piotra >= 100:
        print("Piotr zwyciężył! kończymy grę")
        return "Piotr"
    else:
        limit_rzutow = 2 if konto_alicji > konto_piotra else 3
        konto_alicji += rzuty_kostka(limit_rzotow=limit_rzutow)

        return piotr(konto_alicji=konto_alicji,konto_piotra=konto_piotra)

if liczba_gier > 3 : nie_drukuj()
for nr_gry in range(liczba_gier):
    wygrana_osoba = alicja(konto_alicji=konto_alicji,konto_piotra=konto_piotra)
    liczba_wygranych[wygrana_osoba] += 1
drukuj()
print(f"liczba wygranych na {liczba_gier} wynosi {str(liczba_wygranych)} \nEfektywniejszy gracz to {max(liczba_wygranych, key=liczba_wygranych.get)}")