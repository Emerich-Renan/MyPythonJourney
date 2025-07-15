# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '8', '12', '5'],
        'Resposta': '5',
    },
]

letras = ['a', 'b', 'c', 'd']
qtd_acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        letra = letras[i]
        print(f'{letra})', opcao)

    print()
    entrada = input(
        'Digite uma opção (a, b, c, d) ou a resposta: ').lower().strip()

    acertou = False

    if entrada in letras:
        indice = letras.index(entrada)
        if opcoes[indice] == pergunta['Resposta']:
            acertou = True
    elif entrada == pergunta['Resposta'].lower():
        acertou = True

    if acertou:
        print('Acertou ✅')
        qtd_acertos += 1
    else:
        print('Errou ❌')

print(f'Você acertou {qtd_acertos} de {len(pergunta)} perguntas')
