nome = 'Renan'
sobrenome = 'Emerich'
idade = 19
ano_nascimento = 2005
maior_de_idade = idade >= 18
altura_metros = 1.80
peso = 80

# print('Nome:', nome)
# print('Sobrenome:', sobrenome)
# print('Idade:', idade)
# print('Ano de nascimento:', ano_nascimento)
# print('É maior de idade?:', maior_de_idade)
# print('Altura em metros:', altura_metros)

def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  imc = round(imc, 1)

  faixas = [
    (18.5, 'Abaixo do peso'),
    (25.0, 'no Peso normal'),
    (30.0, 'com Sobrepeso'),
    (35.0, 'com Obesidade grau 1'),
    (40.0, 'com Obesidade grau 2'),
    (float("inf"), 'com Obesidade grau 3')
  ]

  for limite, classificacao in faixas:
    if imc < limite:
      return imc, classificacao
    
imc, classificacao = calcular_imc(peso, altura_metros)

print(f'{nome} tem {altura_metros:.2f} metros de altura, pesa {peso}kg e seu IMC é {imc}, estando {classificacao}.')
