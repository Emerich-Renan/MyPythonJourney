"""
Módulos padrão do Python (import, from, as e *)
https://docs.python.org/3/py-modindex.html
inteiro - import nome_modulo
Vantagens: você tem o namespace do módulo
Desvantagens: nomes grandes
"""

# import sys

# print(sys.platform)

"""
partes - from nome_modulo import objeto1, objeto2
Vantagens: nomes pequenos
Desvantagens: Sem o namespace do módulo
"""

# from sys import exit, platform

# print(platform)
# exit()

"""
alias 1 - import nome_modulo as apelido
alias 2 - from nome_modulo import objeto as apelido
Vantagens: você pode reservar nomes para seu código
Desvantagens: pode ficar fora do padrão da linguagem
"""


# from sys import platform as p
# import sys as s

# print(s.platform)
# print(p)

"""
má prática - from nome_modulo import *
Vantagens: importa tudo de um módulo
Desvantagens: importa tudo de um módulo
"""


from sys import *
print(platform)
print(dllhandle)
print(version)
print(version_info)
exit()
