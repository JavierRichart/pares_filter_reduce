from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def pares(numero):
    if numero % 2 == 0:
        return True

    return False


def sumar(a, b):
    return a + b


numeros_pares = filter(pares, numeros)

lista_pares = list(numeros_pares)

print(f"Lista de números pares: {lista_pares}")

suma_pares = reduce(sumar, lista_pares)

print(f"Suma de los números pares {suma_pares}")
