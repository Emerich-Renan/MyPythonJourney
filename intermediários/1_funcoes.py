"""
  Introdução às funções (def) em Python
  Funções são trechos de código usados para
  replicar determinada ação ao longo do seu código.
  Elas podem receber valores para parâmetros (argumentos)
  e retornar um valor específico.
  Por padrão, funções Python retornam None (nada).

  A Sintaxe de uma função em python é:
  def nome_da_função(parâmetros):
    corpo da função

  Ela pode ser chamada assim:
  nome_da_função(argumentos)  
"""

# Função que exibe uma saudação personalizada
# Se nenhum nome for passado, usa "Sem nome" como parâmetro padrão
def saudacao(nome='Sem nome'):
  print(f'Olá {nome}!')


# Chamadas da função com diferentes argumentos
saudacao('Renan')
saudacao('Ana')
saudacao('Clara')
saudacao()  # Aqui não passa argumento, então imprime "Olá Sem nome!"


# Define uma função que verifica se um número é múltiplo de outro
def multiplo_de(numero, multiplo):
  # Calcula se o número é divisível pelo outro (ou seja, se o resto da divisão é zero)
  resultado = numero % multiplo == 0
  
  # Exibe a pergunta formatada sem quebrar a linha
  print(f'{numero} é múltiplo de {multiplo}?', end=' ')
  
  # Exibe o resultado (True ou False)
  print(resultado)

# Testes da função com diferentes pares de números
multiplo_de(16, 8)   # True, pois 16 é divisível por 8
multiplo_de(15, 3)   # True, pois 15 é divisível por 3
multiplo_de(10, 2)   # True, pois 10 é divisível por 2


# Define uma função que soma três valores, sendo c um valor padrão
def soma(a,b,c=20):
  # imprime os valores de a,b & c, depois imprime a soma
  print(f'{a=} b={b} {c=}', '|', 'a + b + c =', a + b + c) # {a=} é a mesma coisa que b={b}

soma(5,10)
soma(b=10, a=5) 

# Define uma função com um valor None no parâmetro e verifica se
# o terceiro valor foi passado ou não. Se não for passado, soma só x e y.
# Se for passado, soma x, y e z.
def somar(x, y, z=None):
  if z is None:
    print(f'{x=} {y=}', '|', 'A soma é:', x + y)
  else:
    print(f'{x=} {y=} {z=}', '|', 'A soma é:', x + y + z)  

somar(10, 20) # Chama a função com dois valores (z será None)
somar(10, 20, 30) # Teste com três valores, z será usado
somar(z=20, y=10, x=5) # Passando os parâmetros fora de ordem usando nomeação
somar(y=20, x=10) # Outro com nomeação e sem z
