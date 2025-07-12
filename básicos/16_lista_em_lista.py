"""
  Lista de listas e seus índices
"""

salas = [ 

  ['Ana', 'Clara', ],

  ['Helena', ],

  ['Eduarda', 'Renan', 'Elaine']
]

# print(salas[1][0])
# print(salas[0][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[1][1][2])

for sala in salas:
  print(f'A sala é {sala}')
  for aluno in sala:
    print(aluno)

