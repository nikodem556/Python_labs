# Napisac algorytm Dijkstry (przechodzenie najkrotszej sciezki w grafie)

# kolejka priorytetowa ktora zawsze ma najmniejszy (czyli o najwazniejsyzm priorytecie) element na poczatku
import heapq

def dijkstra(graph, start):
    # inicjalizacja zmiennych
    distances = {node: float('inf') for node in graph}  # najpierw dla każdego wierzchołka przypisujemy nieskończoność
    distances[start] = 0  # wierzcholek startowy ma zawsze dystans 0
    priority_queue = [(0, start)]  # para (odległość, wierzchołek)
    visited = set()  # tworzymy zbiór odwiedzonych - zbiory szybko dzialaja z komenda in

    # główna pętla - wykonywana poki mamy cos w kolejce
    while priority_queue:
        # heapq.heapop - bierze najmniejsza wartosc i wladowowywuje ja do current_dist i node
        current_distance, current_node = heapq.heappop(priority_queue)

        # gdybysmy mieli liczyc odleglosc do wierzchołka, który juz byl - breakujemy iteracje
        if current_node in visited:
            continue

        visited.add(current_node)  # zrobiony wierzchołek dodajemy do zuzytych

        # liczymy odległości dla sąsiednich wierzchołków
        # .items zwraca parę klucz-wartość, w tym wypadku sąsiadów i krawędzie
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # obliczamy odległość

            if distance < distances[neighbor]:  # jeśli znaleziona ścieżka jest krótsza
                distances[neighbor] = distance  # aktualizowanie odległości
                heapq.heappush(priority_queue, (distance, neighbor))  # dodawanie sasiada do kolejki

    return distances  # zwracanie najkrótszych dystansów

# test
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 4, 'D': 6},
    'C': {'A': 4, 'B': 5, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

start_node = 'D'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
