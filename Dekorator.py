# Napisać obiektowo prosty dekorator na funkcji
# wypisującej jakiś string, a celem dekoratora jest zamiana liter w napisie na duże litery

# dekorator
class UpperCaseDecorator:
    # konstruktor ktory bedzie przyjmowal funkcje ktora dekorujemy
    def __init__(self, func):
        self.func = func

    # dzieki metodzie call mozemy opakowac inne funkcje
    def __call__(self, *args, **kwargs):
        # wywołanie oryginalnej funkcji wraz z pobraniem jej elemtnów, *args pobiera dowolna liczbe elementow jako tuple
        # **kwargs natomiast pobiera zmienna liczbe elementow jako słownik czyli pary klucz wartosc
        result = self.func(*args, **kwargs)

        # sprawdzamy czy result to napis
        if isinstance(result, str):
            # jesli tak to zmieniamy litery na duże
            return result.upper()

        # jesli nie jest napisem to go nie zmieniamy
        return result


# wywołanie dekoratora, ktory opakuje funkcje print message
@UpperCaseDecorator
def print_message():
    return "hello, world!"  # normalnie male napisy


# wywołanie tutaj funkcji będzie miało duże litery
print(print_message())
