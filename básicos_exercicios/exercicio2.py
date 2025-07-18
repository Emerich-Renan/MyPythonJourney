"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input('Digite sua idade: ')

if nome and idade:
    nome_invertido = nome[::-1]
    espaco_nome = ' ' in nome
    tam_nome = len(nome)
    P_nome = nome[0]
    U_nome = nome[-1]
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')

    if espaco_nome == True:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {tam_nome} letras')
    print(f'A primeira letra do seu nome é: {P_nome}')
    print(f'A última letra do seu nome é: {U_nome}')
else:
    print('Desculpe, você deixou campos vazios!')
