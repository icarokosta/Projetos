print('Bem vindo a loja do Icaro Rodrigues Costa!')
produto = float(input('Digite o valor unitário do produto: '))
qtd = int(input('Digite a quantidade do produto: '))
valor = qtd * produto
d1 = valor                     #Sem desconto
d2 = valor - valor * 3 / 100   #Desconto de 3%
d3 = valor - valor * 6 / 100   #Desconto de 6%
d4 = valor - valor * 10 / 100  #Desconto de 10%
if (qtd <= 4):
   print('O valor sem desconto foi R${}' .format(d1))
   print('Sem desconto para essa quantidade')
elif (qtd >=5) and (qtd <= 19):
    print('O valor sem desconto foi R${}' .format(d1))
    print('O valor com desconto foi R${}' .format(d2))
elif (qtd >=20) and (qtd <= 99):
     print('O valor sem desconto foi R${}' .format(d1))
     print('O valor com desconto foi R${}' .format(d3))
else:    #Quantidade de produtos maior ou igual a 100
      print('O valor sem desconto foi R${}' .format(d1))
      print('O valor com desconto foi R${}' .format(d4))