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

"""
Validador de CPF (Cadastro de Pessoa Física) com base no algoritmo oficial da Receita Federal.

O script:
- Remove caracteres não numéricos da entrada.
- Verifica se o CPF possui exatamente 11 dígitos.
- Verifica se todos os dígitos são iguais (o que invalida o CPF).
- Calcula os dois dígitos verificadores com base nos 9 primeiros.
- Compara os dígitos calculados com os informados.
- Exibe se o CPF é válido ou não.
"""

while True:
  # Entrada do usuário, com limpeza de pontos e traços
  entrada = input('Digite seu CPF: ').replace('.', '').replace('-', '')
  
  # Remove tudo que não for número
  cpf_usuario = re.sub(r'\D', '', entrada)

  # Verifica se o CPF tem exatamente 11 dígitos
  if len(cpf_usuario) != 11:
      print('CPF inválido: Deve conter exatamente 11 dígitos.')
      continue

  # Verifica se todos os dígitos são iguais (ex: 111.111.111-11), o que invalida o CPF
  entrada_e_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
  if entrada_e_sequencial:
      print('CPF inválido: você enviou dados sequenciais.')
      sys.exit()

  # ----- Cálculo do primeiro dígito verificador -----
  
  nove_digitos = cpf_usuario[:9]  # Pega os 9 primeiros dígitos
  multiplica10 = 10
  resultado_digito1 = 0

  # Multiplica cada dígito por pesos de 10 até 2 e soma os produtos
  for digito in nove_digitos:
      resultado_digito1 += int(digito) * multiplica10
      multiplica10 -= 1

  # Aplica a fórmula para o primeiro dígito verificador
  digito1 = (resultado_digito1 * 10) % 11
  digito1 = digito1 if digito1 <= 9 else 0

  # ----- Cálculo do segundo dígito verificador -----

  dez_digitos = cpf_usuario[:10]  # Já inclui o primeiro dígito verificador
  multiplica11 = 11
  resultado_segundo_digito = 0

  # Multiplica por pesos de 11 até 2 e soma os produtos
  for digito in dez_digitos:
      resultado_segundo_digito += int(digito) * multiplica11
      multiplica11 -= 1

  # Aplica a fórmula para o segundo dígito verificador
  digito2 = (resultado_segundo_digito * 10) % 11
  digito2 = digito2 if digito2 <= 9 else 0

  # Junta os 9 dígitos com os dois verificadores calculados
  cpf_calculado = nove_digitos + str(digito1) + str(digito2)

  # Formata o CPF inserido para exibição (padrão xxx.xxx.xxx-xx)
  cpf_formatado = f'{cpf_usuario[:3]}.{cpf_usuario[3:6]}.{cpf_usuario[6:9]}-{cpf_usuario[9:]}'

  # Verifica se o CPF informado bate com o calculado
  if cpf_usuario == cpf_calculado:
      print(f'Seu CPF {cpf_formatado} é válido.')
  else:
      print('Seu CPF é inválido.')