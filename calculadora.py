rodando = True

while rodando:
    while True:
        try:
            num1 = float(input('Digite um número: \n'))
            break
        except:
            print('Digite apenas números.')
    while True:
        try:
            num2 = float(input('Digite o segundo número: \n'))
            break
        except:
            print('Digite apenas números.')

    operacao = input("""Digite o número correspondente à operação que você deseja realizar:
    ===================================
    1- Adição
    2- Subtração
    3- Multiplicação
    4- Divisão
    5- Parte inteira de uma divisão
    6- Resto de uma divisão
    7- Potenciação
    ===================================\n""")

    try:
        if operacao == '1':
            resultado = num1 + num2
            print(f'O resultado de {num1} + {num2} é igual a {resultado}.')
        elif operacao == '2':
            resultado = num1 - num2
            print(f'O resultado de {num1} - {num2} é igual a {resultado}.')
        elif operacao == '3':
            resultado = num1 * num2
            print(f'O resultado de {num1} * {num2} é igual a {resultado}.')
        elif operacao == '4':
            if num2 == 0:
                print('Não é possível dividir quaisquer valor por zero.')
            else:
                resultado = num1 / num2
                print(f'O resultado de {num1} / {num2} é igual a {resultado}.')
        elif operacao == '5':
            resultado = num1 // num2
            print(f'A parte inteira de {num1} dividido por {num2} é igual a {resultado}.')
        elif operacao == '6':
            resultado = num1 % num2
            print(f'O resto de {num1} dividido por {num2} é igual a {resultado}.')
        elif operacao == '7':
            resultado = num1 ** num2
            print(f'O resultado de {num1} elevado ao expoente {num2} é igual a {resultado}.')
        else:
            print(f'A opção de número {operacao} é inexistente, selecione uma das opções apresentadas anteriormente.')

    except:
        print('Digite apenas números nas operações.')

    while True:
        continuar = input('''Você deseja fazer outra operação?
1- Sim
2- Não \n''')
        if continuar == '1':
            break
        elif continuar == '2':
            print('Encerrando calculadora...')
            rodando = False
            break
        else:
            print('Escolha uma das opções fornecidas')
