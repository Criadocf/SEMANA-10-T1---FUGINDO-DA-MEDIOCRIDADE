deposito_inicial = float(input())
taxa = float(input())
tempo = 0
deposito_atualizado = deposito_inicial


while not(deposito_atualizado >= 2*deposito_inicial):
  tempo += 1
  deposito_atualizado += ((taxa/100)*deposito_atualizado)
print(tempo)