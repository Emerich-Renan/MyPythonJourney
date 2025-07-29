# Dictionary Comprehension
# Dicionário original com informações de um produto
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

# Cria um novo dicionário (dc) a partir de 'produto',
# onde:
# - Se o valor for string (verificado com isinstance), transforma para maiúsculas com .upper()
# - Caso contrário, mantém o valor original (ex: preço, que é float)
dc = {
    chave: valor.upper()  # converte string para maiúscula
    # mantém valor original se não for string
    if isinstance(valor, str) else valor
    for chave, valor  # itera sobre cada par chave-valor do dicionário produto
    in produto.items()
}

# Imprime o novo dicionário modificado
print(dc)

# Set Comprehension
# Cria um conjunto (set) com potências de 2 de 2^0 até 2^9
s1 = {2 ** i for i in range(10)}

# Imprime o conjunto ordenado (sorted converte set para lista ordenada)
print(sorted(s1))
