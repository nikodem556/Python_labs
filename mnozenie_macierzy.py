# Napisac program realizujacy mnozenie macierzy (gdzie macierze sa reprezentowane przez listy)


def multiply_matrices(A, B):
    # wymiary macierzy - length(A) zwraca ilosc wierszy, a len(A[0]) bierze liczbe cyfr z pierwszego wiersza
    # czyli liczbe kolumn
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # warunek na mnożenie
    if cols_A != rows_B:
        raise ValueError("Nie mozna pomnozyc macierzy: niezgodne wymiary.")

    # robimy wynikowa macierz zer
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # operacja mnożenia
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# przykladowe macierze
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# test
result = multiply_matrices(A, B)
# printujemy kolejne listy
for row in result:
    print(row)