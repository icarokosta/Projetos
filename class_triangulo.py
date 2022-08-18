a = float(input('Digite o primeiro lado triângulo: '))
b = float(input('Digite o segundo lado triângulo: '))
c = float(input('Digite o terceiro lado triângulo: '))
if (a and b and c > 0) and (max(a,b,c) < (a + b and a + c and b + c)):
  print('É um triângulo!')
  if (a == b == c):
     print('É um triângulo Equilátero')
  elif (a == c or a == c or b == c):
         print('É um triângulo Isósceles')
  else:
           print('É um triângulo Escaleno')
else:
  print('Não é um triângulo!')