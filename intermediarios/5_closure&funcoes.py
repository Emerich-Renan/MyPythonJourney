"""
  Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    """
    Cria uma função de saudação personalizada que lembra a mensagem inicial.

    Parâmetros:
    saudacao (str): A mensagem de saudação que será fixada.

    Retorna:
    function: Uma função que recebe um nome e retorna a saudação personalizada.
    """
    def saudar(nome):
        """
        Gera a saudação combinando a mensagem fixa com o nome dado.

        Parâmetros:
        nome (str): O nome da pessoa a ser saudada.

        Retorna:
        str: A saudação formatada, ex: 'Bom dia, Renan!'
        """
        return f'{saudacao}, {nome}!'

    # Retorna a função interna 'saudar' que "lembra" da saudação
    return saudar


# Cria funções de saudação específicas fixando mensagens diferentes
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# Lista de nomes para testar as saudações
for nome in ['Renan', 'Clara', 'Ana']:
    # Imprime a saudação de boa noite para cada nome
    print(falar_boa_noite(nome))
    # Imprime a saudação de bom dia para cada nome
    print(falar_bom_dia(nome))
