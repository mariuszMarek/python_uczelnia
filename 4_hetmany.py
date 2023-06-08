import doctest
import pprint
import string


class CzteryHetmany():
    '''Klasa do badania problemu czterech hetmanów:

    https://pl.wikipedia.org/wiki/Problem_czterech_hetman%C3%B3w

    Przykłady:

    Utworzenie obiektu:
    >>> h4 = CzteryHetmany('a1 c7 e3 g5')

    Wyświetlanie szachownicy:
    >>> h4.pokaż_szachownicę() # doctest: +NORMALIZE_WHITESPACE
      ---+---+---+---+---+---+---+---
    8    |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    7    |   | H |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    6    |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    5    |   |   |   |   |   | H |   
      ---+---+---+---+---+---+---+---
    4    |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    3    |   |   |   | H |   |   |   
      ---+---+---+---+---+---+---+---
    2    |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    1  H |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
       a | b | c | d | e | f | g | h 

    Pokaż szachowane pola na szachownicy i zmień literę oznaczającą hetmana:
    >>> h4.pokaż_szachownicę(szach='*', hetman='Q') # doctest: +NORMALIZE_WHITESPACE
      ---+---+---+---+---+---+---+---
    8  * | * | * | * | * |   | * | * 
      ---+---+---+---+---+---+---+---
    7  * | * | Q | * | * | * | * | * 
      ---+---+---+---+---+---+---+---
    6  * | * | * | * | * | * | * | * 
      ---+---+---+---+---+---+---+---
    5  * | * | * | * | * | * | Q | * 
      ---+---+---+---+---+---+---+---
    4  * |   | * | * | * | * | * | * 
      ---+---+---+---+---+---+---+---
    3  * | * | * | * | Q | * | * | * 
      ---+---+---+---+---+---+---+---
    2  * | * | * | * | * | * | * | * 
      ---+---+---+---+---+---+---+---
    1  Q | * | * | * | * | * | * | * 
      ---+---+---+---+---+---+---+---
       a | b | c | d | e | f | g | h 

    >>> h4.ile_pod_szachem()
    62
    >>> h4.ile_poza_szachem()
    2

    Tu i niżej odpowiednie pola są wyświetlane w porządku rosnącym
    w tabelce po 8 w rzędzie:
    >>> h4.które_poza_szachem() # doctest: +NORMALIZE_WHITESPACE
    b4 f8
    >>> h4.które_pod_szachem() # doctest: +NORMALIZE_WHITESPACE
    a1 a2 a3 a4 a5 a6 a7 a8
    b1 b2 b3 b5 b6 b7 b8 c1
    c2 c3 c4 c5 c6 c7 c8 d1
    d2 d3 d4 d5 d6 d7 d8 e1
    e2 e3 e4 e5 e6 e7 e8 f1
    f2 f3 f4 f5 f6 f7 g1 g2
    g3 g4 g5 g6 g7 g8 h1 h2
    h3 h4 h5 h6 h7 h8

    Przestaw hetmana z e3 na d4:
    >>> h4.przestaw_hetmana('e3 d4')
    >>> h4.pokaż_szachownicę() # doctest: +NORMALIZE_WHITESPACE
      ---+---+---+---+---+---+---+---
    8    |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    7    |   | H |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    6    |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    5    |   |   |   |   |   | H |   
      ---+---+---+---+---+---+---+---
    4    |   |   | H |   |   |   |   
      ---+---+---+---+---+---+---+---
    3    |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    2    |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
    1  H |   |   |   |   |   |   |   
      ---+---+---+---+---+---+---+---
       a | b | c | d | e | f | g | h 
    '''
    start = 1
    koniec = 9
    wysokosc_planszy = [i for i in range(start, koniec)]
    szerokosc_planszy = [j for j in range(start, koniec)]
    znaki_alfabetu = {indeks+1: znak for indeks,
                      znak in enumerate(list(string.ascii_lowercase)[0:koniec-start])}
    alfabet_na_cyfry = {v: k for k, v in znaki_alfabetu.items()}

    def __init__(self, hetmany=""):
        self.hetmany = hetmany.split()
        self.znaki_yx = {}
        self.pozycje_H = {}
        self.znak_pusty = "   "
        self.ileSzachow = 0

    def czysc_plansze(self):
        self.pozycje_H.clear()
        for kolumna in self.szerokosc_planszy:
            for wiersz in self.wysokosc_planszy:
                self.znaki_yx[f"{kolumna}{wiersz}"] = self.znak_pusty

    def zapisz_pozycje_H(self):
        try:
            for pozycjaH in self.hetmany:
                kolumna, wiersz = pozycjaH
                kolumna = self.alfabet_na_cyfry[kolumna]
                self.pozycje_H[f"{kolumna}{wiersz}"] = self.znak_hetmana
            self.znaki_yx.update(self.pozycje_H)
        except:
            pass

    def ile_pod_szachem(self):
        return sum((zamalowane == self.znak_szach or zamalowane == self.znak_hetmana) for zamalowane in self.znaki_yx.values())

    def ile_poza_szachem(self):
        return sum(puste == self.znak_pusty for puste in self.znaki_yx.values())

    def które_pod_szachem(self):
        pod_szachem = self.generuj_liste_pozycji_od_znaku(
            self.znak_szach, self.znak_hetmana)
        self.drukuj_pozycje(pod_szachem)

    def generuj_liste_pozycji_od_znaku(self, *szukane):
        for pozycja, wartosc in sorted(self.znaki_yx.items()):
            if wartosc in szukane:
                wiersz, kolumna = int(pozycja[0]), pozycja[1]
                litera = self.znaki_alfabetu[wiersz]
                yield f"{litera}{kolumna}"

    def drukuj_pozycje(self, lista_do_druku):
        licznik_pozycji = 0
        for pozycje in lista_do_druku:
            licznik_pozycji += 1
            znak_konca = "\n" if licznik_pozycji > 0 and licznik_pozycji % 8 == 0 else " "
            print(pozycje, end=znak_konca)
        print()

    def które_poza_szachem(self):
        poza_szachem = self.generuj_liste_pozycji_od_znaku(self.znak_pusty)
        self.drukuj_pozycje(poza_szachem)

    def przestaw_hetmana(self, kod_przestawienia):
        skad, dokad = kod_przestawienia.split()
        self.hetmany.remove(skad)
        self.hetmany.append(dokad)        

    def dodaj_szach(self, kolumna, wiersz):
        try:
            if self.znaki_yx[f"{kolumna}{wiersz}"] != self.znak_hetmana and self.znaki_yx[f"{kolumna}{wiersz}"] != self.znak_szach:
                self.znaki_yx[f"{kolumna}{wiersz}"] = self.znak_szach
        except:
            pass

    def gdzie_szach(self):
        for pozycje_Hetmana, znakHetmana in self.pozycje_H.items():
            kolumna, wiersz = pozycje_Hetmana

            kolumna = int(kolumna)
            wiersz = int(wiersz)

            for liczba in range(self.start, self.koniec):
                wyliczone_KP = liczba + kolumna
                wyliczone_KL = kolumna - liczba

                wyliczone_WG = liczba + wiersz
                wyliczone_WD = wiersz - liczba

                self.dodaj_szach(liczba, wiersz)
                self.dodaj_szach(kolumna, liczba)

                self.dodaj_szach(wyliczone_KP, wyliczone_WG)
                self.dodaj_szach(wyliczone_KP, wyliczone_WD)
                self.dodaj_szach(wyliczone_KL, wyliczone_WG)
                self.dodaj_szach(wyliczone_KL, wyliczone_WD)

    def print_znak_planszy(self, wiersz=0, kolumna=0):
        znak = self.znaki_yx[f"{kolumna}{wiersz}"]
        if kolumna == self.start:
            znak = f"{wiersz} " + znak
        return znak

    def pokaż_szachownicę(self, hetman='H', szach=' '):
        self.znak_hetmana = f" {hetman} "
        self.znak_szach = f" {szach} "
        self.czysc_plansze()
        self.zapisz_pozycje_H()

        linia_rozdzielajaca = "  " + "---+" * \
            (self.koniec-(self.start*2)) + "---\n"
        znak = ""

        if szach != " ":
            self.gdzie_szach()
        for poz_y in reversed(self.wysokosc_planszy):  # wiersze
            znak += linia_rozdzielajaca
            tab_znakow = []
            for poz_x in self.szerokosc_planszy:  # kolumny
                tab_znakow.append(self.print_znak_planszy(poz_y, poz_x))
            znak += "|".join(tab_znakow) + "\n"
        znak += linia_rozdzielajaca
        znak += "   "+" | ".join([kolejna_litera
                                 for _, kolejna_litera in self.znaki_alfabetu.items()])

        print(f"{znak}")


if __name__ == "__main__":
  doctest.testmod()