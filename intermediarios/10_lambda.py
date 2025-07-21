"""
    Função lambda em Python

    A função lambda é uma função como qualquer
    outra em Python. Porém, são funções anônimas
    que contêm apenas uma linha. Ou seja, tudo
    deve ser contido dentro de uma única
    expressão.
"""

# Lista de dicionários, cada um representando uma pessoa com 'nome' e 'sobrenome'
lista = [
    {'nome': 'Renan', 'sobrenome': 'Emerich'},
    {'nome': 'Ana', 'sobrenome': 'Coelho'},
    {'nome': 'Jorrene', 'sobrenome': 'Garcia'},
    {'nome': 'Clara', 'sobrenome': 'Coelho'},
]

# Exemplo comentado de como ordenar números (não usado aqui):
# lista = [4, 500, 3, 20, 8, 12, 45, 0, 1, 84, 123, 465, 200, 11]
# lista.sort(reverse=True)
# print(lista)

# Exemplo comentado de função tradicional para ordenação por nome:
# def ordena(item):
#     return item['nome']

# Ordena a lista de dicionários por 'nome' usando função lambda
l1 = sorted(lista, key=lambda item: item['nome'])

# Ordena a lista de dicionários por 'sobrenome' usando função lambda
l2 = sorted(lista, key=lambda item: item['sobrenome'])

# Função que exibe cada item da lista no terminal


def exibir(lista):
    for item in lista:
        print(item)


# Exibe a lista ordenada por nome
exibir(l1)

# Exibe a lista ordenada por sobrenome
exibir(l2)
