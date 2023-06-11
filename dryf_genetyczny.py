import random
import itertools


class organizm:
    pola_genow = [["A", "a"], ["B", "b"], ["C", "c"], ["D", "d"]]
    ilosc_genow = len(pola_genow)
    ilosc_alleli = 2

    def __init__(self, dna_do_przekazania=[]):
        self.DNA = []
        self._uzupelnij_DNA(dna_do_przekazania)

    def _uzupelnij_DNA(self, dna_do_przekazania=[]):
        for gen in range(self.ilosc_genow):
            warian_genu = self.losuj_geny(gen, dna_do_przekazania)
            self.DNA.append(warian_genu)

    def licz_wystapienia_allela(self):
        liczba_wystapien = {}
        for gen in self.DNA:            
            allele = str(gen)
            for allel in allele:                
                if allel in liczba_wystapien: liczba_wystapien[allel] += 1
                else: liczba_wystapien[allel] = 1
        return liczba_wystapien

    
    def losuj_geny(self,numer_genu=0, lista_DNA=[]):
        indeks_genu = random.randrange(0, self.ilosc_genow)
        if not lista_DNA:            
            allel1 = self.pola_genow[numer_genu][random.randrange(0, self.ilosc_alleli)]
            allel2 = self.pola_genow[numer_genu][random.randrange(0, self.ilosc_alleli)]
        else:
            allel1  = lista_DNA[0][numer_genu][random.randrange(0, self.ilosc_alleli)]
            allel2  = lista_DNA[1][numer_genu][random.randrange(0, self.ilosc_alleli)]            
        
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

    print(f"indeks {indeks} {calkowita_populacja[indeks].licz_wystapienia_allela()}")
