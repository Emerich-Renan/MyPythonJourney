# Cria um conjunto vazio para armazenar as letras digitadas (sem repetição)
letras = set()

# Loop infinito que só termina quando a letra 'l' for digitada
while True:
    # Solicita uma letra do usuário e converte para minúscula
    letra = input('Digite: ').lower()

    # Adiciona a letra digitada ao conjunto
    letras.add(letra)

    # Verifica se a letra misteriosa 'l' foi encontrada
    if 'l' in letras:
        print('Parabéns!! Você encontrou a letra misteriosa')
        break  # Encerra o loop

    # Exibe todas as letras digitadas até o momento
    print(letras)
