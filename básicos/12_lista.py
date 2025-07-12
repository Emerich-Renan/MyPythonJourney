"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = ['João', 'Ana', 'Paulo', 'Gabriel', 'Lucas']
lista.append('Kalinka')
lista.insert(0,'Renan')
lista.pop()

indices = range(len(lista))

for nome in indices:
  print(f'{nome} - {lista[nome]}')
