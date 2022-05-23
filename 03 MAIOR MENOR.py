maior = -9999
menor = 9999
num = 4500

while num > 0:
  num = int(input())
  if num > maior:
    maior = num
  if num != 0:
    if num < menor:
      menor = num

if maior != 0:
  print(f'{maior}\n{menor}')