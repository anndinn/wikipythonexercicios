print('Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.')
def inicio():
    n1=int(input('Insira um valor: '))
    if n1> 0:
        print('O numero {} é positivo!'.format(n1))
    elif n1 <0:
        print('O numero {} é negativo!!'.format(n1))
    else:
        print('Entrada incorreta')
        denovo()
    denovo()
def denovo():
        new=input('Deseja fazer novamente? s ou n')
        if new =='s':
            inicio()
        elif new =='n':
            print('Bye')
            exit()
        else:
            denovo()
inicio()