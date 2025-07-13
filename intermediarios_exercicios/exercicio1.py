# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total


num = 2, 5, 4, 8, 9, 6
print(multiply(*num))


def oddeven(x):
    if x % 2 == 0:
        return 'Seu número é par'
    return 'Seu número é ímpar'


print(oddeven(4))
