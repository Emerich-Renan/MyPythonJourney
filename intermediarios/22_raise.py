# raise - lançando exceções (erros)
# Documentação oficial: https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

"""
 Exemplo de interrupção do código com raise:

 print(123)
 raise ValueError('Deu erro')   Isso para o programa aqui e exibe o erro
 print(456)                     Esta linha nunca será executada se o raise for chamado acima
"""


# Função que **não aceita zero** como divisor
def nao_aceito_zero(d):
    if d == 0:
        # Lança um erro específico se o divisor for zero
        raise ZeroDivisionError('Você está tentando dividir por zero.')
    return True  # Se passar, retorna True


# Função que **verifica se um valor é int ou float**
def deve_ser_int_ou_float(n):
    # Captura o tipo real do valor recebido
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        # Se não for número (int ou float), lança um erro do tipo TypeError
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'  # Mostra o tipo real recebido
        )
    return True                              # Se estiver tudo certo, retorna True


# Função principal que realiza a divisão com validações antes
def divide(n, d):
    deve_ser_int_ou_float(n)  # Verifica se o numerador é número
    deve_ser_int_ou_float(d)  # Verifica se o denominador é número
    nao_aceito_zero(d)        # Verifica se o denominador é diferente de zero
    return n / d              # Se tudo estiver certo, retorna a divisão


# Chamada da função com argumentos inválidos
# Aqui estamos passando uma string '0' como divisor
print(divide(8, '0'))  # Vai gerar um erro TypeError porque '0' é uma string
