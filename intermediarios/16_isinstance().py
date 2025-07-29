# isinstance() - para saber se o objeto é de determinado tipo

# Lista com diversos tipos de dados
lista = [
    'a',              # string
    1,                # inteiro
    1.1,              # float
    True,             # booleano
    [0, 1, 2],        # lista
    (0, 1),           # tupla
    {0, 1},           # conjunto (set)
    {'nome': 'Renan'}  # dicionário
]

# Loop para percorrer cada item da lista
for item in lista:
    # Verifica se o item é do tipo set
    if isinstance(item, set):
        print('SET')  # Informa que é um set
        item.add(5)   # Adiciona o número 5 ao set
        # Mostra o set atualizado e confirma o tipo
        print(item, isinstance(item, set))

    # Verifica se o item é do tipo string
    elif isinstance(item, str):
        print('STR')  # Informa que é uma string
        # Mostra a string em maiúsculas e confirma o tipo
        print(item.upper(), isinstance(item, str))

    # Verifica se o item é do tipo int ou float
    elif isinstance(item, (int, float)):
        print('NUM')           # Informa que é um número
        print(item, item * 2)  # Mostra o número e seu dobro

    # Caso não seja nenhum dos tipos anteriores
    else:
        print('OUTRO')  # Informa que é outro tipo de dado
        print(item)     # Mostra o item
