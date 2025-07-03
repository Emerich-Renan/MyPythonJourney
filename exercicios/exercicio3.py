"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_digitado = input('Digite um número inteiro: ')

if not numero_digitado.isdigit():
  print('Esse valor não é válido') 
  exit()

numero_digitado_int = int(numero_digitado) 


if numero_digitado_int % 2 == 0:
  print('Seu número é par')
else:
  print('Seu número é ímpar')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

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


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual o seu primeiro nome? ')

if len(nome) <= 4:
  print('Seu nome é pequeno')
elif  5 <= len(nome) <= 6:
  print('Seu nome é médio')
else:
  print('Seu nome é grande') 


       

