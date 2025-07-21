# Enumerate - enumera iteráveis (índices)

lista = ['Renan', 'Ana', 'Clara']
lista.append('Gabi')

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
# [(0, 'Renan'), (1, 'Ana'), (2, 'Clara'), (3, 'Gabi')]


lista_enumerada = list(enumerate(lista, start=20))
print(lista_enumerada)
# [(20, 'Renan'), (21, 'Ana'), (22, 'Clara'), (23, 'Gabi')]

# Aqui ele pega a tupla
for item in enumerate(lista):
    print(item)

# Aqui ele faz o unpack da tupla
for indice, nome in enumerate(lista):
    print(indice, nome)
