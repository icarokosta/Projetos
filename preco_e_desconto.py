km = float(input('Insira o quantidade de km percorridos: '))
dias = float(input('Insira a quantidade de dias utilizados: '))
rodado = km * 0.15
uso = dias * 60.0
preco = rodado + uso
print('O preço a pagar é de R${}'.format(preco))
