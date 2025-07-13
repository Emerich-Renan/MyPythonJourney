

def saudacao(msg, nome):
    """
    Retorna uma saudação personalizada.

    Parâmetros:
    msg (str): A mensagem de saudação (ex: 'Bom dia').
    nome (str): O nome da pessoa a ser saudada.

    Retorna:
    str: Uma string no formato 'msg, nome!'
    """
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    """
    Executa uma função passada como argumento, com argumentos variáveis.

    Parâmetros:
    funcao (callable): A função que será executada.
    *args: Argumentos posicionais que serão passados para a função.

    Retorna:
    Qualquer: O retorno da função chamada com os argumentos fornecidos.
    """
    return funcao(*args)  # Chama a função com os argumentos desempacotados


# Exibe a saudação "Bom dia, Renan!" usando a função executa
print(
    executa(saudacao, 'Bom dia', 'Renan')
)

# Exibe a saudação "Bom dia, Clara!" usando a função executa
print(
    executa(saudacao, 'Bom dia', 'Clara')
)