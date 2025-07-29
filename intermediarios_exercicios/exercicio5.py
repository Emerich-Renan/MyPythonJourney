import pprint  # Importa o módulo para imprimir dados formatados e legíveis

"""
    Exercício 01 - Ordenação com Lambda
    - Ordena uma lista de dicionários contendo nome e nota de alunos.

    (a) Pela nota, em ordem decrescente.
    (b) Pelo nome, em ordem alfabética.
    (c) Crie uma função exibir_alunos(lista) que mostre cada aluno em uma linha.
"""

# Função para exibir listas de forma formatada


def exibir(valor):
    pprint.pprint(valor, sort_dicts=False, width=40)
    print()


# Lista de alunos com nome e nota
alunos = [
    {'nome': 'Carlos', 'nota': 7.5},
    {'nome': 'Amanda', 'nota': 9.2},
    {'nome': 'Bruno', 'nota': 6.8},
]

# (a) Ordena por nota (decrescente)
nota_alunos = sorted(alunos, reverse=True, key=lambda item: item['nota'])
exibir(nota_alunos)

# (b) Ordena por nome (ordem alfabética)
nome_alunos = sorted(alunos, key=lambda item: item['nome'])
exibir(nome_alunos)

"""
    Exercício 02 - List Comprehension com Condicional
    - Manipula uma lista de valores com condições usando list comprehension.
"""

valores = [5, 12, 18, 3, 7, 25, 9]

# (a) Multiplica por 2 somente os valores maiores que 10
novos_valores = [
    valor * 2 if valor > 10 else valor
    for valor in valores
]
exibir(novos_valores)

"""
    Exercício 03 - Função executa com Lambda
    - Usa função como parâmetro (funções de ordem superior) com lambdas.

    (a) Soma 3 números
    (b) Retorna o maior entre 3 valores
    (c) Cria uma função que triplica um número
"""

# Função que executa qualquer função passada como argumento


def executa(funcao, *args):
    return funcao(*args)


# (a) Soma 3 números: 2 + 5 + 7
exibir(executa(
    lambda x, y, z: x + y + z,
    2, 5, 7
))

# (b) Retorna o maior valor entre 1, 5 e 10
exibir(executa(
    lambda *args: max(args),
    1, 5, 10
))

# (c) Cria uma função que triplica valores e testa com 5
triplica = executa(lambda m: lambda n: n * m, 3)
exibir(triplica(5))

"""
    Exercício 04 - Empacotamento e Desempacotamento de Dicionários
    - Usa empacotamento para juntar dicionários e imprime pares chave:valor.
"""

# (a) Dois dicionários base
user = {'nome': 'Renan', 'idade': 19}
extra = {'cidade': 'Sua Cidade', 'altura': 1.80}

# Junta os dois dicionários usando desempacotamento
completo = {**user, **extra}

# (b) Função que imprime os dados recebidos via kwargs


def mostra_dados(**kwargs):
    for chave, valor in kwargs.items():
        exibir((f'{chave}: {valor}'))


# (c) Passa o dicionário completo desempacotado para a função
mostra_dados(**completo)
