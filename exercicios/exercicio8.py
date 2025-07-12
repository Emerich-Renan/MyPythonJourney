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

# Bloco do Primeiro Dígito
while True:
  entrada = input('Digite seu cpf: ').replace('.', '').replace('-', '')
  cpf_usuario = re.sub(r'\D', '', entrada)
  
  # Verifica se o CPF tem exatamente 11 dígitos numéricos
  if len(cpf_usuario) != 11:
    print('CPF inválido: Deve conter exatamente 11 dígitos')
    continue
  
  # Verifica se todos os dígitos do CPF são iguais (ex: 11111111111)
  entrada_e_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
  if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

  # Extrai os 9 primeiros dígitos para calcular o primeiro dígito verificador
  nove_digitos = cpf_usuario[:9]
  multiplica10 = 10
  resultado_digito1 = 0

  # Multiplica cada dígito pelo peso decrescente de 10 a 2 e soma os resultados
  for digito in nove_digitos:
    resultado_digito1 += int(digito) * multiplica10
    multiplica10 -= 1

 # Calcula dígito1: se (soma * 10) % 11 > 9, então 0; senão, mantém o valor
  digito1 = (resultado_digito1 * 10) %  11
  digito1 = digito1 if digito1 <= 9 else 0 


  # Extrai os 10 primeiros dígitos para calcular o segundo dígito verificador
  dez_digitos = cpf_usuario[:10]
  multiplica11 = 11
  resultado_segundo_digito = 0

  # Multiplica cada dígito pelo peso decrescente de 11 a 2 e soma os resultados
  for digito in dez_digitos:
    resultado_segundo_digito += int(digito) * multiplica11
    multiplica11 -= 1

  digito2 = (resultado_segundo_digito * 10) % 11
  digito2 = digito2 if digito2 <= 9 else 0 
  # Junta os 9 dígitos iniciais com os dois dígitos verificadores calculados
  cpf_calculado = nove_digitos + str(digito1) + str(digito2)
  # Formata o CPF para o padrão xxx.xxx.xxx-xx para exibição
  cpf_formatado = f'{cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}'

  # Compara o CPF informado com o calculado para validar
  if cpf_usuario == cpf_calculado:
    print(f'Seu CPF {cpf_formatado} é válido')
  else:
    print('Seu CPF é inválido')  