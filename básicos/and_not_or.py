# and (e): Retorna True se ambas as expressões forem True.
# Se qualquer valor for False, o resultado será False.
# OBS: 0 0.0 '' -> False

# or (ou): Retorna True se pelo menos uma das expressões for True.
# Se todas forem False, o resultado será False.

# not (não): Inverte o valor da expressão.
# Se a expressão for True, retorna False, e vice-versa.

      
entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '123456'

# Os parenteses permitem agrupar as condições
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: 
    print('Você entrou no sistema')
elif (entrada == 'E' or entrada == 'e') and senha_digitada != senha_permitida:
    print('Senha incorreta')
elif (entrada == 'S' or entrada == 's'):
    print('Você saiu do sistema')
if not (entrada == 'E' or entrada == 'e') and not (entrada == 'S' or entrada == 's'):
    print('Você não digitou nem entrar e nem sair. Para isso, digite "E" ou "S".')

# Neste exemplo o else não foi utilizado, pois o if not cobriu essa situação. (mas o else é mais 
# legível)