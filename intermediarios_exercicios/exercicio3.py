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


# Lista de perguntas do quiz, cada uma com opções e a resposta correta
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

vidas = 3         # número inicial de vidas do jogador
pontos = 0        # pontuação do jogador
letras = ['a', 'b', 'c', 'd']  # letras correspondentes às opções

# Loop principal que percorre cada pergunta
for numero, pergunta in enumerate(perguntas, start=1):
    print(f'Pergunta {numero} de {len(perguntas)}')
    print(pergunta['Pergunta'])  # exibe o enunciado da pergunta

    opcoes = pergunta['Opções']  # pega as alternativas da pergunta

    # Exibe as opções com as letras (a, b, c, d)
    for i, opcao in enumerate(opcoes):
        letra = letras[i]
        print(f'{letra})', opcao)

    # Pede ao jogador uma entrada
    escolha = input(
        'Digite uma opção (a, b, c, d) ou a resposta:').strip().lower()

    acertou = False  # assume que o jogador errou até que se prove o contrário

    if escolha in letras:
        # Se o jogador digitou uma letra válida
        indice = letras.index(escolha)
        if opcoes[indice] == pergunta['Resposta']:
            # Se a letra escolhida corresponde à resposta correta
            acertou = True
            pontos += 1
            print('Acertou ✅')
        else:
            # Letra válida, mas resposta errada
            vidas -= 1
            print('\tErrou ❌')

    elif escolha == pergunta['Resposta'].lower():
        # Se o jogador digitou diretamente a resposta correta
        acertou = True
        pontos += 1
        print('\tAcertou ✅')
    else:
        # Qualquer outra entrada que não seja válida ou correta
        vidas -= 1
        print('\tErrou ❌')

    # Verifica se o jogador perdeu todas as vidas
    if vidas <= 0:
        print('\nVocê perdeu todas as vidas!!')
        break
    else:
        # Mostra o status atual
        print(f'\tVidas: {vidas} | pontos: {pontos}')

# Limpa a tela (no Windows) para exibir o fim do jogo
os.system('cls')

print('\n\tFIM DO JOGO!')
print(f'Você acertou {pontos} de {len(perguntas)} perguntas!')

# Exibe a mensagem de vitória ou derrota
if vidas > 0:
    print('Parabéns!! Você venceu! 🎉✨')
else:
    print('Você ficou sem vidas! Tente novamente! 😥')

print(f'Pontuação final: {pontos}')
