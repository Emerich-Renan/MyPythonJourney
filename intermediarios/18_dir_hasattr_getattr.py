# Define uma string comum
string = 'Renan'

# Define o nome de um método que você quer verificar se existe na string
metodo = 'lower'

# Verifica se o objeto 'string' possui um atributo/método com o nome contido na variável 'metodo'
if hasattr(string, metodo):
    print('Existe', metodo)  # Informa que o método existe

    # Usa getattr para obter dinamicamente o método 'lower' da string, e em seguida o executa com ()
    # Resultado será 'renan', pois o método 'lower' coloca tudo em minúsculo
    print(getattr(string, metodo)())
else:
    # Caso o método não exista, essa mensagem será exibida
    print('Não existe o método', metodo)
