'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''
def mouf():
    letra = input('Digite F para feminino e M para masculino: ')
    if letra == 'f':
        print('Voce escolheu {} de feminino.'.format(letra))
    elif letra == 'm':
        print('Voce escolhe {} de masculino'.format(letra))
    else:
        print('Entrada invalida!')

    novo()
def novo():
    var=input('Quer fazer de novo:? ')
    if var == 's':
        mouf()
    elif var == 'n':
        print('bye')
        exit()
    else:
        print('Entrada invalida! tente novamente')
        novo()
mouf()