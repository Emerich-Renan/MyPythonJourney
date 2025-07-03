# Fatiamento [i:f:p] -> i = início, f = fim, p = passo
# Exemplo: [1:10:2] -> Inicia no índice 1,
# termina no índice 10 (não inclusivo) e avança de 2 em 2. 

# Exemplo de fatiamento de uma string
texto = 'Python é uma linguagem de programação incrível!'
# Fatiamento da string
fatiado = texto[0:6]  # Pega do índice 0 ao 5 (não inclui o 6)
print(fatiado)

print(texto[0:20:2])  # Pega do índice 0 ao 19 (não inclui o 20) e avança de 2 em 2
