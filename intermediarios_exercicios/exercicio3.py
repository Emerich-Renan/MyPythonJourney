# # Exercício - sistema de perguntas e respostas

import os

# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '8', '12', '5'],
#         'Resposta': '5',
#     },
# ]

# letras = ['a', 'b', 'c', 'd']
# qtd_acertos = 0

# for pergunta in perguntas:
#     print(pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']

#     for i, opcao in enumerate(opcoes):
#         letra = letras[i]
#         print(f'{letra})', opcao)

#     print()
#     entrada = input(
#         'Digite uma opção (a, b, c, d) ou a resposta: ').lower().strip()

#     acertou = False

#     if entrada in letras:
#         indice = letras.index(entrada)
#         if opcoes[indice] == pergunta['Resposta']:
#             acertou = True
#     elif entrada == pergunta['Resposta'].lower():
#         acertou = True

#     if acertou:
#         print('Acertou ✅')
#         qtd_acertos += 1
#     else:
#         print('Errou ❌')

# print(f'Você acertou {qtd_acertos} de {len(pergunta)} perguntas')


perguntas = [
    {
        'Pergunta': 'Quanto é 3*3 ?',
        'Opções': ['6', '9', '1', '12'],
        'Resposta': '9',
    },
    {
        'Pergunta': 'Quanto é 20-10 ?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '10',
    },
    {
        'Pergunta': 'Quanto é 10/2 ?',
        'Opções': ['4', '8', '12', '5'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 5! ?',
        'Opções': ['120', '240', '100', '200'],
        'Resposta': '120',
    },
    {
        'Pergunta': 'Qual o meu nome ?',
        'Opções': ['Renan', 'Rennan', 'Renann', 'Reenan'],
        'Resposta': 'Renan',
    },
    {
        'Pergunta': 'Qual a inicial do nome da minha namorada?',
        'Opções': ['A', 'C', 'G', 'K'],
        'Resposta': 'A',
    },
]

vidas = 3
pontos = 0
letras = ['a', 'b', 'c', 'd']


for numero, pergunta in enumerate(perguntas, start=1):
    print(f'Pergunta {numero} de {len(perguntas)}')
    print(pergunta['Pergunta'])

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        letra = letras[i]
        print(f'{letra})', opcao)

    escolha = input(
        'Digite uma opção (a, b, c, d) ou a resposta:').strip().lower()

    acertou = False

    if escolha in letras:
        indice = letras.index(escolha)
        if opcoes[indice] == pergunta['Resposta']:
            acertou = True
            pontos += 1
            print('Acertou ✅')
        else:
            vidas -= 1
            print('\tErrou ❌')
    elif escolha == pergunta['Resposta'].lower():
        acertou = True
        pontos += 1
        print('\tAcertou ✅')
    else:
        vidas -= 1
        print('\tErrou ❌')

    if vidas <= 0:
        print('\nVocê perdeu todas as vidas!!')
        break
    else:
        print(f'\tVidas: {vidas} | pontos: {pontos}')

os.system('cls')
print('\n\tFIM DO JOGO!')
print(f'Você acertou {pontos} de {len(perguntas)} perguntas!')
if vidas > 0:
    print('Parabéns!! Você venceu! 🎉✨')
else:
    print('Você ficou sem vidas! Tente novamente! 😥')

print(f'Pontuação final: {pontos}')
