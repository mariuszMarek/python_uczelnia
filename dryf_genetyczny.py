import random
class organizm:
    wariant_genu = ['A','a']
    limit = len(wariant_genu)
    def __init__(self) -> None:
        self.DNA = []
        
        self.DNA.append(self.wariant_genu[random.randrange(0,self.limit)])
        self.DNA.append(self.wariant_genu[random.randrange(0,self.limit)])

if __name__ == "__main__":
    i = 0
    populacja = {}
    while i < 100: 
        osobnik = organizm()
        populacja[osobnik] = osobnik.DNA
        i += 1
    print (i)
    