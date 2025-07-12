

def escopo():
    """
    Cria uma variável 'x' no escopo local da função e a imprime.
    Fora da função, essa variável não existe.
    """
    x = 1
    print(x)  # Vai imprimir 1

# print(x)  # NameError: 'x' está no escopo local e não pode ser acessado aqui

escopo()


def saudacao():
    """
    Define uma variável local chamada 'mensagem' e a imprime dentro da função.
    Fora da função, a variável não está disponível.
    """
    mensagem = "Essa mensagem é local à função"
    print("Dentro da função:", mensagem)

saudacao()

# print("Fora da função:", mensagem)  # NameError: 'mensagem' não existe fora da função

