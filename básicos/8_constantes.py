'''
CONSTANTE = 'Variáveis' que não vão mudar
Muitas condições no mesmo if (ruim)
      <- Contagem de complexidade (ruim)
'''

velocidade = 80  # Velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade do carro passou o limite do Radar 1!')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('Você foi multado!!')
else:
    print('Não foi multado.')
