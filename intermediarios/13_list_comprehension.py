"""
    List comprehension em Python

    List comprehension é uma forma rápida e elegante
    de criar listas a partir de iteráveis (como range, listas, strings, etc).
"""

# Exemplo básico de como criar uma lista com números de 0 a 9
# print(list(range(10)))  # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Forma tradicional (sem list comprehension):
lista = []
for numero in range(10):
    lista.append(numero)  # Adiciona os números de 0 a 9 na lista
# print(lista)  # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Usando list comprehension (forma reduzida e elegante)
lista = [
    numero * 2        # expressão: dobra cada número
    for numero in range(10)  # iterável: de 0 a 9
]
print(lista)  # Saída: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
