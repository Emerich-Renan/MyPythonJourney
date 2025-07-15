
letras = set()
while True:
    letra = input('Digite: ').lower()
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns!! Você encontrou a letra misteriosa')
        break

    print(letras)
