"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
----------------------------------------

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import re
import sys

# Primeiro Dígito
while True:
  entrada = input('Digite seu cpf: ').replace('.', '').replace('-', '')
  cpf_usuario = re.sub(r'[^0-9]', '', entrada)
  

  if len(cpf_usuario) > 11:
    print('CPF inválido')
    continue

  entrada_e_sequencial = entrada == entrada[0] * len(entrada)
  if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()


  nove_digitos = cpf_usuario[:9]
  multiplo10 = 10
  resultado_primeiro_digito = 0

  for primeiro_digito in nove_digitos:
    resultado_primeiro_digito += int(primeiro_digito) * multiplo10
    multiplo10 -= 1
    
  primeiro_digito = (resultado_primeiro_digito * 10) %  11
  primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0 


  # Segundo Dígito
  dez_digitos = cpf_usuario[:10]
  multiplo11 = 11
  resultado_segundo_digito = 0

  for segundo_digito in dez_digitos:
    resultado_segundo_digito += int(segundo_digito) * multiplo11
    multiplo11 -= 1

  segundo_digito = (resultado_segundo_digito * 10) % 11
  segundo_digito = segundo_digito if segundo_digito <= 9 else 0 
  cpf_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

  cpf_formatado = f'{cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}'

  if cpf_usuario == cpf_calculo:
    print(f'Seu CPF {cpf_formatado} é válido')
  else:
    print('Sei CPF é inválido')  