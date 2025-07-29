"""
    Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
    Mútaveis [] {} set()
    Imutáveis () "" 0 0.0 None False range(0,10)
"""

# Definição de vários tipos de dados com valores "falsy" ou "vazios"
lista = []               # Lista vazia → falsy
dicionario = {}          # Dicionário vazio → falsy
conjunto = set()         # Conjunto vazio → falsy
tupla = ()               # Tupla vazia → falsy
string = ''              # String vazia → falsy
inteiro = 0              # Número inteiro zero → falsy
flutuante = 0.0          # Número float zero → falsy
nada = None              # None (ausência de valor) → falsy
falso = False            # Booleano falso → falsy
intervalo = range(0, 10)  # Um range de 0 até 9 (não é vazio) → truthy


# Função que verifica se o valor é considerado "falsy" ou "truthy" em Python
def falsy(valor):
    return 'Falsy' if not valor else 'Truthy'


# Testes individuais com a função, usando f-strings para exibir variáveis e resultados
print(f'TESTE', falsy('TESTE'))                  # String não vazia → truthy
print(f'{lista=}', falsy(lista))                 # []
print(f'{dicionario=}', falsy(dicionario))       # {}
print(f'{conjunto=}', falsy(conjunto))           # set()
print(f'{tupla=}', falsy(tupla))                 # ()
print(f'{string=}', falsy(string))               # ''
print(f'{inteiro=}', falsy(inteiro))             # 0
print(f'{flutuante=}', falsy(flutuante))         # 0.0
print(f'{nada=}', falsy(nada))                   # None
print(f'{falso=}', falsy(falso))                 # False

# range(0, 10) → truthy porque contém valores
print(f'{intervalo=}', falsy(intervalo))
