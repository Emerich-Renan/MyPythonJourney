# Introdução ao desempacotamento + tuplas (tuples)

# Pack
nomes = ['Maria', 'José', 'Pedro']
nome1, nome2, nome3 = nomes
print(nome1)

# Unpack
# O underscore age como uma variável não utilizável, então usamos para servir de complementação
_, nome_2, *_ = ['João', 'Renan', 'Lucas']
print(nome_2)

# Tupla. É uma lista imutável.

nomes = ['Ana', 'Clara', 'Renan']
# Ou não utilizar [] na variavel que já cria uma tuple sem usar o método tuple()
nomes = tuple(nomes)

print(nomes[1])
