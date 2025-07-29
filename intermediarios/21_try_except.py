# Try, except, else, finally

a = 10
b = 0

try:
    print('Linha 1'[1000])
    c = a / b
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('valor de B não definido')
except (TypeError):
    print('TypeError')
except Exception:
    print('ERRO DESCONHECIDO')
