from dataclasses import dataclass
import json

# Tworzymy dataclass, która automatycznie generuje metodę __init__
@dataclass
class DaneOsobowe:
    imie: str
    nazwisko: str
    adres: str
    kod_pocztowy: str
    pesel: str

    # Metoda zapisująca obiekt do pliku JSON
    def zapisz_do_json(self, sciezka_pliku):
        with open(sciezka_pliku, 'w') as plik:
            json.dump(self.__dict__, plik, indent=4)

    # Metoda wczytująca obiekt z pliku JSON
    @classmethod
    def wczytaj_z_json(cls, sciezka_pliku):
        with open(sciezka_pliku, 'r') as plik:
            dane = json.load(plik)
        return cls(**dane)  # Tworzymy nowy obiekt klasy, przekazując dane do konstruktora
