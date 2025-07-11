"""
split, join e strip com list e str
split - divide uma string
join - una uma string
strip - remove os espaços que antecedem e sucedem a string
rstrip - remove os espaços apenas no final (na direita) da string
lstrip - remove os espaços apenas do início (na esquerda) da string

"""

frase = '     Olha só que     b      coisa interessante       '
lista_frases_cruas = frase.split('b ')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
  lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)  

frases_unidas = '-'.join(lista_frases)

print(frases_unidas)