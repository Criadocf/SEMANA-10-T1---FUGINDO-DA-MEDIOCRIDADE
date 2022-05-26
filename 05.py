ano = 2016
mes = 10

montante_salario = float(input())
montante_divida = float(input())

while (montante_salario > montante_divida):
  if mes == 3:
    montante_salario += ((5/100)*montante_salario)
  montante_divida += ((15/100)*montante_divida)
  mes += 1
  if (mes==13):
    mes = 1
    ano +=1
print(f'{mes}/{ano}')