# Mapeamento de dados em list comprehension

import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# Lista de produtos, cada um representado por um dicionário com nome e preço
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

# Criação de uma nova lista de produtos usando list comprehension
# Se o preço for maior que 20, aumenta em 5%
# Caso contrário, mantém o produto original
novos_produtos = [
    # Desempacota todos os dados do produto original e altera apenas o 'preco' se for > 20
    {**produto, 'preco': produto['preco'] * 1.05}
    # Se o preço não for maior que 20, mantém como está
    if produto['preco'] > 20 else {**produto}
    for produto in produtos  # Itera sobre todos os produtos
]


# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(11) if n > 0]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]
p(novos_produtos)
