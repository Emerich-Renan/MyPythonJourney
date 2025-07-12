# Iterando strings com while

nome = 'Maria Helena'

tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < tamanho_nome:
  letra = (nome[indice] + '*')
  novo_nome += letra
  indice += 1

print(novo_nome)

# Calculadora com While
while True:

  numero_1 = input('Digite um numero: ')
  numero_2 = input('Digite outro numero: ')
  operador = input('Digite um operador (+ - * /): ')

  num_1_float = 0
  num_2_float = 0

  numeros_validos = None
  try:
    num_1_float = float(numero_1)
    num_2_float = float(numero_2)
    numeros_validos = True
  except:
    numeros_validos = None

  if numeros_validos is None:
    print('Um ou ambos os números digitados são inválidos!')
    continue

  operadores_permitidos = '+-*/'

  if operador not in operadores_permitidos:
    print('Operador inválido!')
    continue

  if len(operador) > 1:
    print('Digite apenas um operador!')
    continue

  if operador == '+':
    print(f'A soma de {num_1_float} + {num_2_float} é', num_1_float + num_2_float)
  elif operador == '-':
    print(f'A subtração de {num_1_float} - {num_2_float} é', num_1_float - num_2_float)
  elif operador == '*':
    print(f'A multiplicação de {num_1_float} * {num_2_float} é', num_1_float * num_2_float)
  elif operador == '/':    
    print(f'A divisão de {num_1_float} / {num_2_float} é', num_1_float / num_2_float)
  else:
    print('Isso não deveria acontecer...')  



  sair = input('Quer sair? [s]im: ').lower().startswith('s')

  if sair is True:
   break