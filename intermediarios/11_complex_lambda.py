# Função que recebe outra função (funcao) e argumentos (*args), e executa essa função com os argumentos fornecidos
def executa(funcao, *args):
    return funcao(*args)


# Função comum que retorna a soma de dois números
def soma(x, y):
    return x + y


# Função que cria e retorna outra função (função de multiplicação personalizada)
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


# Executando uma função lambda que soma dois valores (2 + 3 = 5)
print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

# duplica será uma função que multiplica qualquer número por 2 (função retornada por outra função)
# Aqui, usamos uma função lambda para criar um multiplicador e passamos 2 como o valor do multiplicador
# O resultado é uma nova função: lambda n: n * 2
duplica = executa(
    lambda m: lambda n: n * m,
    2
)

# Chamamos a função 'duplica' com o valor 5 → 5 * 2 = 10
print(duplica(5))

# Executa uma função lambda que soma todos os argumentos recebidos (com uso de *args)
# Neste caso: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
