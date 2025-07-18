# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índices;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 4, 4, 4, 4, 5]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# Métodos úteis:
# add, update, clear, discard

# s1 = {1, 2, 3}
# s1.add(5)
# s1.add(4)
# # s1.update('Renan') # saída será cada letra na string sem ordem garantida

# # com uma tupla, ele atualiza com os valores dentro dela
# s1.update(('Renan', 6, 7, 8))
# s1.discard('Renan')  # não tem index, ou seja, precisa do valor a ser deletado
# print(s1)
# s1.clear()
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2  # saída {1, 2, 3, 4}

s3 = s1 & s2  # saída {2, 3}

s3 = s1 - s2  # saída {1}

s3 = s2 - s1  # saída {4}

s3 = s1 ^ s2  # saída {1,4}

print(s3)
