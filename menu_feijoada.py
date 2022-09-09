def volumeFeijoada():  # Cria a função a ser usada na entrada de volume da feijoada
    while True:
        print('Menu volume de feijoada')
        global res  # torna global a variável e deixa a mesma ser utilizada no programa principal
        try:
            vol = int(input('Digite a quantidade desejada (em mL)\nMínimo de 300mL e máximo de 5000mL: \n'))
            res = (vol * 0.08)  # Calcula o valor da feijoada com base no valor por mL
        except:  # Verifica se ocorreu alguma exceção
            print('O valor digitado é inválido! Tente novamente...')
            continue
        if vol < 300:  # Verifica se o volume está abaixo do ofertado pelo restaurante
            print('Digite uma quantidade acima do mínimo!(300mL)')
        elif vol > 5000:  # Verifica se o volume está acima do ofertado pelo restaurante
            print('Digite uma quantidade abaixo do máximo!(5000mL)')
        else:
            return res  # Retorna o valor por mL da feijoada
            break


def opcaoFeijoada():  # Cria a função a ser usada na escolha de acompanhamentos
    while True:
        print('Menu opção de feijoada')
        try:  # Tenta obter a opção de feijoada
            opcao = input(
                'Digite a opção desejada: \nb - Básica (Feijão + paiol + costelinha) \np - Premium (Feijão + paiol + costelinha + partes de porco) \ns - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon): \n')
        except:
            print('Digite uma opçao válida!')
            continue
        if opcao == 'b':  # Verifica se a opção digitada é válida
            return 1.0
        elif opcao == 'p':
            return 1.25
        elif opcao == 's':
            return 1.5
        elif (opcao != 'b') or (opcao != 'p') or (opcao != 's'):  # Verifica se a opção digitada é inválida
            print('Digite uma opçao válida!')
            continue
        else:
            break


def acompanhamentoFeijoada():  # Cria a função a ser usada no somatório de acompanhamentos
    global contac  # torna global a variável e deixa a mesma ser utilizada no programa principal
    contac = 0  # deixa a acumuladora em 0 fora do laço para que não seja zerada a cada loop
    while True:
        try:  # Tenta obter o número de acompanhamentos da feijoada
            ac = int(input(
                'Deseja mais algum acompanhamento: \n0- Não desejo mais acompanhamentos (encerrar pedido) \n1- 200g de arroz \n2- 150g de farofa especial \n3- 100g de couve cozida \n4- 1 laranja descascada: '))
        except:
            print('Digite um número de opção válido ou digite 0 para sair...')
            continue
        if ac == 0:
            return contac
            break
        elif ac == 1:  # Verifica se a opção digitada é válida
            contac += 5
        elif ac == 2:
            contac += 6
        elif ac == 3:
            contac += 7
        elif ac == 4:
            contac += 3
        elif (ac != 0) or (ac != 1) or (ac != 2) or (ac != 3) or (ac != 4):  # Verifica se a opção digitada é inválida
            print('Digite um número de opção válido ou digite 0 para sair...')
        else:
            return contac
            break


print('Bem vindo ao Menu de feijoada de Icaro Rodrigues Costa!')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
print('Valor de R${:.2f} (volume = {} * opção = {} + acompanhamento = {:.2f})'.format(volume * opcao + acompanhamento,res, opcao, contac))
