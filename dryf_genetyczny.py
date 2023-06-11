import random
import itertools


class organizm:
    pola_genow = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd']]
    ilosc_genow = len(pola_genow)
    ilosc_alleli = 2

    def __init__(self, dna_do_przekazania=[]):
        self.DNA = []

        if not dna_do_przekazania:
            self._uzupelnij_DNA()
        else:
            self._losuj_gen_rodzicow(dna_do_przekazania)
            pass

    def _uzupelnij_DNA(self):
        for gen in range(self.ilosc_genow):
            warian_genu = self._losuj_gen_1_generacji()
            self.DNA.append(warian_genu)

    def _losuj_gen_rodzicow(self, lista_DNA):
        zestaw1 = lista_DNA[0]
        zestaw2 = lista_DNA[1]
        for gen in range(self.ilosc_genow):
            pierwszy_allel = zestaw1[gen][random.randrange(
                0, self.ilosc_alleli)]
            drugi_allel = zestaw2[gen][random.randrange(0, self.ilosc_alleli)]            
            self.DNA.append(pierwszy_allel+drugi_allel)
    def licz_wystapienia_allela(self):
        pass
    def _losuj_gen_1_generacji(self):
        indeks_genu = random.randrange(0, self.ilosc_genow)
        allel1 = self.pola_genow[indeks_genu][random.randrange(
            0, self.ilosc_alleli)]
        allel2 = self.pola_genow[indeks_genu][random.randrange(
            0, self.ilosc_alleli)]
        return allel1 + allel2

    def __str__(self):
        return f"{self.DNA[0]} {self.DNA[1]}  {self.DNA[2]}  {self.DNA[3]}"


if __name__ == "__main__":

    liczba_startowa = 10
    liczba_pokolen = 10
    populacja_startowa = []
    calkowita_populacja = []

    for kolejny_osobnik in range(liczba_startowa):
        rodzic = organizm()
        populacja_startowa.append(rodzic)
    calkowita_populacja = populacja_startowa

    unikalne_indeksy_bez_powtorzen = list(range(liczba_startowa))
    random.shuffle(unikalne_indeksy_bez_powtorzen)

    for numer_generacji in range(liczba_pokolen):
        lista_pokoleniowa = []
        for kolejne_kojarzeni in range(int(liczba_pokolen/2)):

            indeks_rodzic1 = unikalne_indeksy_bez_powtorzen[kolejne_kojarzeni]
            indeks_rodzic2 = unikalne_indeksy_bez_powtorzen[kolejne_kojarzeni+1]

            rodzic1 = populacja_startowa[indeks_rodzic1]
            rodzic2 = populacja_startowa[indeks_rodzic2]

            potomekA = organizm([rodzic1.DNA,rodzic2.DNA])
            potomekB = organizm([rodzic1.DNA,rodzic2.DNA])

            lista_pokoleniowa.append(potomekA)
            lista_pokoleniowa.append(potomekB)

        calkowita_populacja = calkowita_populacja + lista_pokoleniowa
        populacja_startowa = lista_pokoleniowa

for indeks in range(len(calkowita_populacja)):
    print(f"indeks {indeks} {calkowita_populacja[indeks]}")
