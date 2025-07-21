# Troca de valores entre variáveis
a, b = 1, 2
a, b = b, a  # agora a = 2, b = 1
# print(a, b)  # 2 1

# Exemplo comentado de como desempacotar um dicionário usando items()
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# Também poderíamos iterar assim:
# for chave, valor in pessoa.items():
#     print(chave, valor)

# Dicionário com informações básicas da pessoa
pessoa = {
    'nome': 'Renan',
    'sobrenome': 'Emerich',
}

# Outro dicionário com dados adicionais
dados_pessoa = {
    'idade': 16,
    'altura': 1.8,
}

# Empacotamento (merge) de dois dicionários usando o operador `**`
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
# Saída: {'nome': 'Renan', 'sobrenome': 'Emerich', 'idade': 16, 'altura': 1.8}

# --------------------------------------
# *args e **kwargs
# *args → argumentos não nomeados (tupla)
# **kwargs → argumentos nomeados (dicionário)


def mostro_argumentos_nomeados(*args, **kwargs):
    # Mostra os argumentos posicionais (não nomeados)
    print('NÃO NOMEADOS: ', args)

    # Itera pelos argumentos nomeados (chave: valor)
    for chave, valor in kwargs.items():
        print(chave, valor)

# Exemplos comentados:
# mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoa_completa)


# Outro exemplo usando um dicionário com vários argumentos nomeados
configs = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

# Aqui passamos os valores de `configs` como argumentos nomeados via desempacotamento
mostro_argumentos_nomeados(**configs)
