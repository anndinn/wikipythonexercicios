print('Faça um Programa que leia três números e mostre o maior e o menor deles.')
def maior():
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    n3 = int(input('Digite o terceiro numero: '))
    if n1 > n2 and n1 > n3:
        print('O numero {} é maior que {} e {}!'.format(n1,n2,n3))
    elif n2 > n1 and n2 > n3:
        print('O numero {} é maior que {} e {}!'.format(n2,n1,n3))
    elif n3 > n1 and n3 > n2:
        print('O numero {} é maior que {} e {}!'.format(n3,n2,n1))
    if n1 < n2 and n1 < n3:
        print('O numero {} é menor que {} e {}!'.format(n1,n2,n3))
    elif n2 < n1 and n2 < n3:
        print('O numero {} é menor que {} e {}!'.format(n2,n1,n3))
    elif n3 < n1 and n3 < n2:
        print('O numero {} é menor que {} e {}!'.format(n3,n2,n1))
    else:
        print('Entrada invalida')
        novo()
    novo()
def novo():
    new= input('Voce gostaria de fazer novamente: s ou n ')
    if new == 's':
        maior()
    if new == 'n':
        print('bye bye')
        exit()
    else:
        novo()
maior()