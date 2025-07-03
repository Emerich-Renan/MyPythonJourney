'''
Repetições
while (Enquanto)
Eecuta uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''


'''
condicao = True

while condicao:
  nome = input('Qual o seu nome: ')
  print(f'Seu nome é {nome}')

  if nome == 'sair':
    break

print('Você saiu')
'''

contador = 0

while contador <= 50:
  contador += 1

  if contador == 6:
    print('Não vou mostrar o 6')
    continue

  print(contador)

  if contador == 37:
    break

print('Acabou') 

'''
O (continue) faz o while voltar ao início ignorando o loop.
O (break) faz o while parar o loop.
'''