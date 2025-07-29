# Importa o módulo sys, usado aqui para medir o tamanho (em bytes) de objetos na memória
import sys

# Demonstrando diferença entre iteráveis, iteradores e geradores em Python

# iterable é uma lista comum — possui o método __iter__ e pode ser percorrida com for
iterable = ['Eu', 'Tenho', '__iter__']

# iterator é criado a partir do iterável — possui os métodos __iter__ e __next__
iterator = iter(iterable)

# Lista por compreensão — gera imediatamente todos os 10.000 números e os armazena na memória
lista = [n for n in range(10)]

# Generator expression — cria um objeto que gera os números sob demanda, sem armazenar tudo na memória
generator = (n for n in range(10))

# Exibe o tamanho em bytes ocupado pela lista completa
print(sys.getsizeof(lista))

# Exibe o tamanho em bytes ocupado pelo gerador (bem menor, pois não guarda tudo)
print(sys.getsizeof(generator))
