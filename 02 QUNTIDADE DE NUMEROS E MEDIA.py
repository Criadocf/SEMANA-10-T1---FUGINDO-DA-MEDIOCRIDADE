num = 1

quant_numeros = 0

soma = 0

while num > 0:
  num = int(input())
  if num != 0:
    quant_numeros += 1
    soma += num

if soma != 0:
  print(f'{soma/quant_numeros:.2f}')