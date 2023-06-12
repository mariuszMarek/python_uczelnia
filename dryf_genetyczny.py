import random
import csv
from collections import Counter


class organizm:
    pola_genow = [["A", "a"], ["B", "b"], ["C", "c"], ["D", "d"]]
    kolejnosc_zapisu = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']
    ilosc_genow = len(pola_genow)
    ilosc_alleli = 2

    def __init__(self, dna_do_przekazania=[]):
        self.DNA = []
        self._uzupelnij_DNA(dna_do_przekazania)

    def _uzupelnij_DNA(self, dna_do_przekazania=[]):
        for gen in range(self.ilosc_genow):
            warian_genu = self._losuj_geny(gen, dna_do_przekazania)
            self.DNA.append(warian_genu)

    def licz_wystapienia_allela(self):
        liczba_wystapien = Counter(
            {klucz: 0 for klucz in self.kolejnosc_zapisu})
        liczba_wystapien.update("".join(self.DNA))
        return liczba_wystapien

    def _losuj_geny(self, numer_genu=0, lista_DNA=[]):
        if not lista_DNA:
            allel1 = self.pola_genow[numer_genu][random.randrange(
                0, self.ilosc_alleli)]
            allel2 = self.pola_genow[numer_genu][random.randrange(
                0, self.ilosc_alleli)]
        else:
            allel1 = lista_DNA[0][numer_genu][random.randrange(
                0, self.ilosc_alleli)]
            allel2 = lista_DNA[1][numer_genu][random.randrange(
                0, self.ilosc_alleli)]

        return allel1 + allel2

    def __str__(self):
        return f"{self.DNA[0]} {self.DNA[1]}  {self.DNA[2]}  {self.DNA[3]}"


def zamien_wartosci_na_proporcje(slownik_licznik):
    calkowita_suma = slownik_licznik.total()
    for klucze in slownik_licznik:
        slownik_licznik[klucze] /= calkowita_suma


if __name__ == "__main__":

    liczba_startowa = 20
    liczba_pokolen = 50
    liczba_dzieci = 2
    populacja_startowa = []
    suma_alleli = Counter()
    nazwa_pliky_wynikowego = "poklenia.csv"

    for _ in range(liczba_startowa):
        rodzic = organizm()
        populacja_startowa.append(rodzic)
        suma_alleli.update(rodzic.licz_wystapienia_allela())
    zamien_wartosci_na_proporcje(suma_alleli)
    with open(nazwa_pliky_wynikowego, "w", newline="") as plik_wynikowy:
        zapisuj = csv.writer(plik_wynikowy, delimiter=";")
        zapisuj.writerow(suma_alleli.keys())
        zapisuj.writerow(suma_alleli.values())

        for _ in range(liczba_pokolen):
            lista_pokoleniowa = []
            suma_alleli.clear()
            random.shuffle(populacja_startowa)
            try:
                kolejne_kojarzenie = 0
                while kolejne_kojarzenie < len(populacja_startowa):
                    for _ in range(liczba_dzieci):                        
                        dziecko = organizm([populacja_startowa[kolejne_kojarzenie].DNA, populacja_startowa[kolejne_kojarzenie+1].DNA])
                        lista_pokoleniowa.append(dziecko)
                        suma_alleli.update(dziecko.licz_wystapienia_allela())
                    kolejne_kojarzenie += 2
            except:
                pass
            zamien_wartosci_na_proporcje(suma_alleli)
            zapisuj.writerow(suma_alleli.values())
            populacja_startowa = lista_pokoleniowa
