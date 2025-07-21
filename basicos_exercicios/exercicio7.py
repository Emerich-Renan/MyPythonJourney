"""
Módulo de lista de compras

Permite inserir, apagar e listar itens.
Garante que não haja erros por índices inexistentes.
"""


import os


def clear_terminal():
    os.system('cls')


def insira_item():
    """
    Solicita um valor ao usuário e adiciona à lista de itens
    """
    valor_inserir = input('Valor para inserir: ').lower()
    lista_itens.append(valor_inserir)
    print(f'Valor: "{valor_inserir}" foi inserido com sucesso!')
    input('Pressione ENTER para continuar')


def apague_item():
    """
    Solicita ao usuário um valor para apagar da lista e apaga o item
    """
    valor_apagar = input('Valor para apagar: ').lower()

    if valor_apagar in lista_itens:
        lista_itens.remove(valor_apagar)
        print(f'Valor: "{valor_apagar}" foi apagado com sucesso!')
    elif valor_apagar.isdigit():
        valor_apagar = int(valor_apagar)
        if 0 <= valor_apagar < len(lista_itens):
            lista_itens.pop(valor_apagar)
            print(f'Índice: ({valor_apagar}) foi apagado com sucesso!')
        else:
            print('Índice inválido')
    else:
        print('Item não estava na lista')
    input('Pressione ENTER para continuar')


def mostre_lista():
    """
    Exibe os itens da lista ou informa que a lista está vazia.
    """
    if not lista_itens:
        print('Lista vazia')
    else:
        print('\nItens na lista: ')
        for indice, nome in enumerate(lista_itens):
            print(indice, nome)
        print()
    input('Pressione ENTER para continuar')


lista_itens = []
while True:
    clear_terminal()
    entrada = input('Selecione uma opção \n'
                    '[i]nserir [a]pagar [l]istar [s]sair: ').lower().strip()

    if entrada == 's':
        print('Você saiu com sucesso!')
        input('Pressione ENTER para fechar o programa...')
        break
    elif entrada not in 'ial' or len(entrada) > 1:
        clear_terminal()
        print('Digite apenas i, a ou l')
        continue
    elif entrada == 'i':
        insira_item()
    elif entrada == 'a':
        apague_item()
    elif entrada == 'l':
        mostre_lista()
