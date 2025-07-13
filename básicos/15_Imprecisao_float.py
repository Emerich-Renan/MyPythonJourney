"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
"""

import decimal

num1 = decimal.Decimal('0.1')
num2 = decimal.Decimal(str(0.7))
num3 = num1 + num2
print(num2)
print(num3)
print(f'Aqui está sendo utilizado a formatação de string {num3:.2f}')
print(f'Aqui está sendo utilizado o round() {round(num3, 1)}')
