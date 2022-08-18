#Calculadora básica
print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer tecla para sair')
op = input('Digite qual operação seja fazer: ')
if (op == '+' or op == '-' or op == '*' or op == '/'):
   a = float(input('Digite o primeiro número: '))
   b = float(input('Digite o segundo número: '))
if (op == '+'):
    print(a + b)
elif (op == '-'):
    print(a - b)
elif (op == '*'):
    print(a * b)
elif (op == '/'):
    print(a / b)
else:
    print('Opção inválida')
print('Encerrando o programa...')