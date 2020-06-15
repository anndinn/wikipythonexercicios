print('Faça um Programa que leia três números e mostre-os em ordem decrescente.')
def ordem():
    n1 = input('Digite o primeiro numero: ')
    n2 = input('Digite o segundo numero: ')
    n3 = input('Digite o terceiro numero: ')
    if n1 < n2 and n1 < n3 and n2 < n3:
        print('A ordem decresente é {}, {}, {}!'.format(n1,n2,n3))
    if n1 < n2 and n1 < n3 and n3< n2:
        print('A ordem decresente é {}, {}, {}!'.format(n1,n3,n2))
    if n2 < n1 and n2 < n3 and n3 < n1:
        print('A ordem decresente é {}, {}, {}!'.format(n2,n3,n1))
    if n2 < n1 and n2 < n3 and n1 < n3:
        print('A ordem decresente é {}, {}, {}!'.format(n2,n1,n3))
    if n3 < n1 and n3 < n2 and n2 < n1:
        print('A ordem decresente é {}, {}, {}!'.format(n3,n2,n1))
    if n3 < n1 and n3 < n2 and n1 < n2:
        print('A ordem decresente é {}, {}, {}!'.format(n3,n1,n2))
    else:
        print('Algo deu errado!')
        novo()
    novo()
def novo():
    new = input('Voce quer fazer novamente? ')
    new = new.lower()
    if new == 's':
        ordem()
    if new =='n':
        print('bye bye')
        exit()
    else:
        novo()
ordem()