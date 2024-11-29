#2. Napisac prosta klase przechowujaca np. dane osobowe (imie, nazwisko, adres zamieszkania, kod pocztowy, pesel)
# i metode zapisujaca obiekty typu tej klasy do json, oraz metode odczytuja json'a i ladujace
# dane do klasy

import json # konieczne do zapisu i odczytu


# klasa spelniajaca warunki klasy osobowej
class DaneOsobowe:
    def __init__(self, imie, nazwisko, adres, kod_pocztowy, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.kod_pocztowy = kod_pocztowy
        self.pesel = pesel

    # metoda ktora zapisuje plik do json, argumentem jest sciezka pliku
    def zapisz_do_json(self, scicezka_pliku):
        with open(scicezka_pliku, 'w') as plik:
            json.dump(self.__dict__, plik, indent=4) # indent = wciecie (ilosc spacji), uzywamy jako obiektu typu dict

    # metoda odczytujaca plik json z danej sciezki
    @classmethod        #class method to metoda ktora jest wywolywana dla konkretnej klasy, nie ma ona self, a cls
    def wczytaj_z_json(cls, sciezka_pliku):
        with open(sciezka_pliku, 'r') as plik:
            dane = json.load(plik)
        return cls(**dane) # tworzymy nowy obiekt przekazujące dane do konstruktora

# test
osoba1 = DaneOsobowe("Nikodem", "Szafran", "Warszawa", "00-001", "12345678901")
osoba1.zapisz_do_json("C:/Users/nikod/Desktop/STUDIA/sem5/Python/laby3/tak123.json")

# musimy wywolac dla konkretnej klasy
osoba2 = DaneOsobowe.wczytaj_z_json("C:/Users/nikod/Desktop/STUDIA/sem5/Python/laby3/nie321.json")
print(osoba2.__dict__)
