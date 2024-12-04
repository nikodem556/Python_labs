# 4. Zaimplementowac algorytm Aho-Corasick

class AhoCorasick:
    def __init__(self):
        # trie root - poczatkowy wezel
        self.tree = [{}]  # lista slownikow ktora bedzie reprezentowac przejscia w tree
        self.fail = [-1]  # tablica przejsc fail dla kazdego wezla
        self.output = [[]]  # tablica wynikow mowiaca ktore wzorce koncza sie w danym wezle

    def add_pattern(self, pattern, index):
        # dodawanie wzorca do tree
        current_state = 0
        for char in pattern:
            # tworzenie nowego węzła, jeśli ten nie istnieje
            if char not in self.tree[current_state]:
                self.tree[current_state][char] = len(self.tree) # dzieki temu zawsze bedzie to kolejny wezel
                self.tree.append({})  # dodanie nowego węzła jako słownik do listy
                self.fail.append(-1)  # domyślne przejście fail
                self.output.append([])  # pusty wynik dla nowego węzła
            current_state = self.tree[current_state][char]
        # dodajemy indeks wzorca do wyniku koncowego wzorca
        self.output[current_state].append(index)

    def build(self):
        # budowanie mechanizmu fail dla naszego Trie
        queue = []

        # ustawienie przejść `fail` dla pierwszego poziomu drzewa
        for char, state in self.tree[0].items():
            self.fail[state] = 0  # korzeń Trie jkest pierwszym wezlem i nie ma poprzednikow
            queue.append(state)

        # przetwarzanie kolejnych wezlow drzewa
        while queue:
            current_state = queue.pop(0)

            for char, next_state in self.tree[current_state].items():
                queue.append(next_state)  # dodajemy dziecko wezla do kolejki

                # znalezienie stanu do ktorego bedziemy wracac w razie niepowodzenia
                fail_state = self.fail[current_state]
                while fail_state != -1 and char not in self.tree[fail_state]:
                    fail_state = self.fail[fail_state]
                # jeśli nie znajdziemy żadnego prefiksu to wracamy do korzenia
                self.fail[next_state] = self.tree[fail_state][char] if fail_state != -1 else 0
                # łączymy wyniki z węzła fali
                self.output[next_state].extend(self.output[self.fail[next_state]])

    def search(self, text):
        # wyszukiwanie wzorców w tekscie
        current_state = 0  # zaczynamy od korzenia
        results = []

        for i, char in enumerate(text):
            # jeśli nie znajdujemy przejścia dalej wykonujemy fail
            while current_state != -1 and char not in self.tree[current_state]:
                current_state = self.fail[current_state]
            if current_state == -1:  # przy powrocie do korzenia, reset stanu
                current_state = 0
                continue
            # przejście do kolejnego węzła
            current_state = self.tree[current_state][char]
            # jeśli jakieś wzorce kończą się tutaj - dodajemy wynik
            if self.output[current_state]:
                for pattern_index in self.output[current_state]:
                    results.append((i, pattern_index))  # (pozycja w tekście, indeks wzorca)
        return results # zwracanie wyników


# test
aho_corasick = AhoCorasick()

# dodawanie wzorców do algorytmu
patterns = ['nik', 'sza', 'as']
for i, pattern in enumerate(patterns):
    aho_corasick.add_pattern(pattern, i)

# budowanie drzewa trie, inicjalizacja failów
aho_corasick.build()

# szukanie wzorców w tekście
text = "szaniknikszabas"
matches = aho_corasick.search(text)

# wyniki (pozycja w tekscie, indeks wzorca)
print(matches)
