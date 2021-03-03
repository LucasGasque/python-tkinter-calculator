n1 = float
n2 = float
funcao = ''
ms = float
ms_mais = float
ms_menos = float
resultado = float



while funcao != 'off': 
    n1 = float(input('Digite um numero: '))
    funcao = input('Digite uma função \(+ - * /)')
    n2 = float(input('Digite um numero: '))

    if funcao == '+':
        resultado = n1 + n2
        print(resultado)
    elif funcao == '-':
        resultado = n1 - n2
        print(resultado)
    elif funcao == '*':
        resultado = n1 * n2
        print(resultado)
    elif funcao == '/':
        resultado = n1 / n2
        print(resultado)
    else:
        print('Função invalida!')








