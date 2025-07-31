# Interpolação de Strings
nome = 'Renan'
idade = 30

# Método 1: Usando f-strings
print(f'O meu nome é {nome} e eu tenho {idade} anos.')
# O f antes da string indica que é uma f-string, permitindo a interpolação de variáveis diretamente na string.

# Método 2: Usando str.format()
print('O meu nome é {} e eu tenho {} anos.'.format(nome, idade))
# O método str.format() permite inserir variáveis na string usando chaves {} como marcadores de posição.

# Método 3: Usando % (método antigo)
print('O meu nome é %s e eu tenho %d anos.' % (nome, idade))
# O operador % permite formatar strings, onde %s é usado para strings e %d para inteiros.

# Alguns exemplos de interpolação
# s -> String
# d -> Inteiro
# f -> Float
# x ou X -> Hexadecimal
# > Esquerda
# < Direita
# ^ Centro
# Conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
