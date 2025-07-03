# Exercício 1
numero_digitado = input('Digite um número inteiro: ')

if not numero_digitado.isdigit():
  print('Esse valor não é válido') 
  exit()

numero_digitado_int = int(numero_digitado) 


if numero_digitado_int % 2 == 0:
  print('Seu número é par')
else:
  print('Seu número é ímpar')


# Exercicio 2
entrada = input('Informe a hora atual: ')

try:
  hora = int(entrada)

  if hora >= 0 and hora <= 11:
    print('Bom dia!!')
  elif hora >= 12 and hora <= 17:
    print('Boa tarde!!')
  elif hora >= 18 and hora <= 23:
    print('Boa noite!!')
  else:
    print('Não conheço essa hora')
except ValueError:
  print('Por favor, digite apenas números inteiros!')


# Exercicio 3
nome = input('Qual o seu primeiro nome? ')

if len(nome) <= 4:
  print('Seu nome é pequeno')
elif  5 <= len(nome) <= 6:
  print('Seu nome é médio')
else:
  print('Seu nome é grande') 


       

