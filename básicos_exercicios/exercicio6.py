import os
def clear_terminal():
  os.system('cls')


# Jogo de Adivinhação de Letras (Forca Simplificada)
# Implemente um jogo onde o usuário deve adivinhar a palavra secreta letra por letra.
# O programa deve:
# Pedir uma letra por vez ao usuário.
# Mostrar a palavra com as letras já acertadas e * nos espaços restantes.
# Contabilizar o número de tentativas feitas.
# Avisar se o usuário digitou mais de uma letra.
# Quando o usuário completar a palavra, mostrar mensagem de vitória e número de tentativas.
# Perguntar se o usuário quer sair ou continuar jogando.
'''
while True:
  palavra_chave = 'bananeira'
  letras_acertadas = ''
  num_tentativas = 0
  letra_digitada = input('Digite uma letra ')

  if len(letra_digitada) > 1:
    clear_terminal()
    print('Digite apenas uma letra!')
    continue

  if letra_digitada in palavra_chave:
    num_tentativas += 1
    letras_acertadas += letra_digitada
  else:
    clear_terminal()
    print(letra_digitada, 'não está na palavra abaixo:')  

  palavra_em_andamento = ''
  for letra_chave in palavra_chave:
    if letra_chave in letras_acertadas:
      palavra_em_andamento += letra_chave
    else:
      palavra_em_andamento += '*'

  print(palavra_em_andamento)

  if palavra_em_andamento == palavra_chave:
    clear_terminal()
    print('GANHOU!! PARABÉNS!')
    print('A palavra chave era ', palavra_chave)
    print(f'Você completou a palavra em {num_tentativas} tentativas')
    print('')
    letras_acertadas = ''
    num_tentativas = 0
    ganhou = True

    if ganhou:
      sair = input('Você gostaria de sair? [s]im [n]ão ').strip().lower()
      if sair == 's':
        clear_terminal()
        break
      else:
        continue
'''


# Exercício 2 — Verificador de Número Primo com Saída
# Faça um programa que:
# Solicite números ao usuário repetidamente.
# Permita que o usuário saia digitando "s".
# Valide se a entrada é um número inteiro válido (não aceitando letras nem símbolos).
# Rejeite números maiores que 100.000 e peça para tentar novamente.
# Verifique se o número digitado é primo (divisível apenas por 1 e por ele mesmo).
# Informe se o número é primo ou não.
# Repita o processo até que o usuário decida sair.
'''
while True:
  num_digitado = input('Se quiser sair, digite "s" \n' \
  'Digite um número e direi se é primo:').lower()

  if num_digitado == 's':
    clear_terminal()
    print('Obrigado!')
    exit()

  if num_digitado.isdigit():
    numero = int(num_digitado)
  else:
    print('Por favor, digite apenas números!')
    continue  

  if numero > 100000:
    print('Número muito grande! Tente um menor que 10.000')
    continue

  divisores = 0
  for i in range(1, numero + 1):
    if numero % i == 0:
      divisores += 1

  if divisores == 2:
    clear_terminal()
    print(numero, 'é primo!')
  else:
    clear_terminal()
    print(numero, 'não é primo')
'''


# Exercício 3 — Contador Simples de Vogais
# Escreva um programa que:
# Peça ao usuário para digitar uma frase.
# Conte quantas vogais (a, e, i, o, u) existem nessa frase.
# Imprima o total de vogais encontradas.
# Finalize após uma única contagem.
'''
while True:
  frase = input('Digite uma frase: ')
  vogais = 'aeiou'
  contador = 0

  for letra in frase:
    if letra.lower() in vogais:
      contador += 1

  print(f'A frase contém {contador} vogais')
  break
'''


# Exercício 4 — Análise Detalhada de Vogais com Frequência
# Construa um programa que:
# Receba uma frase do usuário (sem diferenciar maiúsculas e minúsculas).
# Conte quantas vezes cada vogal (a, e, i, o, u) aparece na frase.
# Calcule o total de vogais na frase.
# Identifique qual vogal apareceu com maior frequência e quantas vezes.
# Exiba o total de vogais e qual foi a vogal mais frequente com sua quantidade.

frase = input('Digite uma frase: ').lower()

vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in frase:
  if letra in vogais:
    vogais[letra] += 1

total_vogais = sum(vogais.values())

mais_frequente = max(vogais, key=vogais.get)
quantidade = vogais[mais_frequente]

print(f'A frase contém {total_vogais} vogais.')
print(f'A vogal que mais apareceu foi "{mais_frequente}", com {quantidade} vez(es)')
