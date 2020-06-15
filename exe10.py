print('Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino')
print('ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!')
print('ou "Valor Inválido!", conforme o caso.')
def turno():
    n1 = input('Qual seu turno, M V ou N? ')
    n1 = n1.lower()
    if n1 == 'm':
        print('Bom dia!')
    elif n1 == 'v':
        print('Boa tarde!!')
    elif n1 == 'n':
        print('Boa noite')
    else:
        print('Algo deu errado!!')
        novo()
    novo()
def novo():
    new = input('Quer fazer novamente? ')
    new = new.lower()
    if new =='s':
        turno()
    elif new =='n':
        print('bye bye')
        exit()
    else:
        new()
turno()