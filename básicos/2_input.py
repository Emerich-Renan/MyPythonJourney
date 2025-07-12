# nome = input('Qual o seu nome?')

# print(f'O seu nome é: {nome}')

numero_1 = input('Digite um numero')
numero_2 = input('Digite outro numero')

if not numero_1.isdigit() or not numero_2.isdigit(): 
  print('Colocar apenas numeros!')
else:
  numero_1 = int(numero_1)
  numero_2 = int(numero_2)
  print(f'A soma dos numeros é {numero_1 + numero_2}')
