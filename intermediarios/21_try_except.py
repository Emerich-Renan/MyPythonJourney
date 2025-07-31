# Try, except, else, finally – estrutura de tratamento de erros em Python

a = 10
b = 0  # Isso causará um erro de divisão por zero

try:
    print('Abriu o try')  # Indica que o bloco try foi iniciado

    # Essa linha está comentada, mas se fosse ativada causaria IndexError
    # print('Linha 1'[1000])

    # Aqui ocorre uma tentativa de divisão por zero -> ZeroDivisionError
    c = a / b

# Esse bloco captura especificamente o erro de divisão por zero
except ZeroDivisionError as e:
    print(e.__class__.__name__)  # Mostra o nome da exceção (ZeroDivisionError)
    print('Dividiu por zero')

# Captura se a variável B não estiver definida
except NameError:
    print('valor de B não definido')

# Captura dois tipos de erro ao mesmo tempo: TypeError e IndexError
except (TypeError, IndexError) as error:
    print('TypeError / IndexError')
    print('MSG:', error)  # Mostra a mensagem do erro
    print('Nome:', error.__class__.__name__)  # Nome da exceção

# Captura qualquer outro erro que não foi tratado anteriormente
except Exception:
    print('ERRO DESCONHECIDO')

# Executa apenas se **nenhum erro** ocorreu no bloco try
else:
    print('Não deu erro')

# Sempre executa, independentemente de erro ou não
finally:
    print('Fecha o try')

# Código continua normalmente após o tratamento de erro
print('CONTINUAR')
