print('Companhia Costa fornecimento de energia, Bom dia!')
print('Programa de cálculo de preço de fornecimento de energia elétrica')
consumo = float(input('Digite a quantidade de kWh consumidos: '))
print('Tipos de instalação:')
print('R para residência')
print('I para indústrias')
print('C para comércios')
tipo = input('Digite o tipo de instalação: ')
if (tipo == 'R' or tipo == 'r') and (consumo <= 500): #Utilização do ( or tipo == 'r') para aceitação da entrada de letra minúscula
  res = consumo * 0.40
  print('O valor é de R$ {:.2f}' .format(res)) #O :.2f utilizando dentros dos {} sinaliza a utilização de somente duas casas decimais
elif (tipo == 'R' or tipo == 'r') and (consumo > 500):
    res = consumo * 0.65
    print('O valor é de R$ {:.2f}' .format(res))
elif (tipo == 'C' or tipo == 'c') and (consumo <= 1000):
    res = consumo * 0.55
    print('O valor é de R$ {:.2f}' .format(res))
elif (tipo == 'C' or tipo == 'c') and (consumo > 1000):
    res = consumo * 0.60
    print('O valor é de R$ {:.2f}' .format(res))
elif (tipo == 'I' or tipo == 'i') and (consumo <= 5000):
    res = consumo * 0.55
    print('O valor é de R$ {:.2f}' .format(res))
elif (tipo == 'I' or tipo == 'i') and (consumo > 5000):
    res = consumo * 0.60
    print('O valor é de R$ {:.2f}' .format(res))
else:
    print('Operação inválida!')
print('Encerrando o programa...')
