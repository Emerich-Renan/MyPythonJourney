# Mapeamento de dados em list comprehension


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

# Exibe os produtos um por linha, com o desempacotamento do asterisco e separador '\n'
print(*novos_produtos, sep='\n')
