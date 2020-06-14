print('Faça um Programa que peça dois números e imprima o maior deles.')
def maiormenor():
    n1 = int(input('insira o primeiro numero: '))
    n2 = int(input('insira o segundo numero: '))
    if n1 > n2:
        print('O {} é maior que {}!'.format(n1,n2))
    elif n2 > n1:
        print('O numero {}é maior que {}!!'.format(n2,n1))
    elif n2 == n1 or n1 == n2:
        print('Os numeros {} e {} são iquais!'.format(n1,n2))
    else:
        print('Entrada invalida')
    novo()
def novo():
    new= input('Quer fazer novamente? s ou n')
    if new == 's':
        maiormenor()
    elif new == 'n':
        print('Bye')
        exit()
    else:
        novo()
maiormenor()