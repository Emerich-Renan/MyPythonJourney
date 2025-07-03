''''
Solicite ao usuário dois números e exiba qual deles é maior, indicando ambos no resultado. 
'''

primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

if primeiro_valor > segundo_valor:
   print(f"O primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor}).")
else:
   print(f"O segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor}).")