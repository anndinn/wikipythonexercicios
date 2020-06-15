print('Faça um programa que pergunte o preço de três produtos e informe')
print('qual produto você deve comprar,sabendo que a decisão é sempre pelo mais barato.')
def menorpreco():
    item1=input('Insira o valor do primeiro produto: ')
    item2=input('O valor do segundo produto: ')
    item3=input('Valor do terceiro produto: ')
    if item1 < item2 and item1 < item3:
        print('Vamos comprar o de {}, pois é mais barato que {} e {}!'.format(item1,item2,item3))
    elif item2 < item1 and item2 < item3:
        print('Vamos compra o de {} é mais barato que {} e {}!!'.format(item2,item1,item3))
    elif item3 < item2 and item3 < item1:
        print('Vamos comprar o item de {}, é mais barato que {} e {}!!'.format(item3,item2,item1))
    else:
        print('Entrada invalida')
    novo()
def novo():
    new1=input('Quer fazer novamente? s ou n ')
    if new1 =='s':
        menorpreco()
    if new1 == 'n':
        print('Bye Bye')
        exit()
    else:
        novo()
menorpreco()