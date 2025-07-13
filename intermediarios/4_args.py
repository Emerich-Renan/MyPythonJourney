"""
  args - Argumentos não nomeados
  * - *args (empacotamento e desenpacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4, 5
# print(x, y, resto)

# def soma(x, y):
#   return x + y


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


numeros = 1, 2, 3, 4, 5, 6, 7

print(sum(numeros))

print(*numeros)

outra_soma = soma(*numeros)
print(soma(*numeros))
print(outra_soma)
