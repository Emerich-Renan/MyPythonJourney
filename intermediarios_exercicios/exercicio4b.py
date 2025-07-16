lista_de_lista_inteiros = [
    [1, 2, 4, 4, 6, 2, 8, 4, 1, 5],
    [5, 4, 3, 2, 1, 1, 2, 1, 4, 6],
    [2, 2, 9, 1, 5, 4, 8, 2, 0, 0],
    [3, 2, 4, 7, 6, 7, 8, 4, 4, 5],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [10, 8, 4, 7, 2, 3, 2, 4, 1, 4],
    [7, 4, 5, 3, 1, 7, 1, 4, 8, 9],
]


def encontrar_repetido_3x(lista_inteiros):

    numeros_checados = {}
    numero_repetido_3x = -1

    for numero in lista_inteiros:
        if numero in numeros_checados:
            numeros_checados[numero] += 1
            if numeros_checados[numero] == 3:
                numero_repetido_3x = numero
                break
        else:
            numeros_checados[numero] = 1

    return numero_repetido_3x


for lista in lista_de_lista_inteiros:
    print(lista, encontrar_repetido_3x(lista))
