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
qtd_acertos = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)

    print()
    entrada = input('Digite uma opção: ')

    entrada_int = None
    qtd_opcoes = len(opcoes)
    acertou = False

    if entrada.isdigit():
        entrada_int = int(entrada)

    if entrada_int is not None:
        if entrada_int >= 0 and entrada_int < qtd_opcoes:
            if opcoes[entrada_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print('Acertou ✅')
        qtd_acertos += 1
    else:
        print('Errou ❌')

print(f'Você acertou {qtd_acertos} de {len(pergunta)} perguntas')
