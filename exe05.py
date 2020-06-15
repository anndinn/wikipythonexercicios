print('Faça um programa para a leitura de duas notas parciais de um aluno.')
print('O programa deve calcular a média alcançada por aluno e apresentar:')
print('A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;')
print('A mensagem "Reprovado", se a média for menor do que sete;')
print('A mensagem "Aprovado com Distinção", se a média for igual a dez.')

def media():
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    if media >= 7 and media < 10:
        print('Aprovado')
    elif media < 7 :
        print('Reprovado')
    elif media == 10:
        print('Aprovadissimo')
    else:
        print('Entrada invalida')

    denovo()
def denovo():
    var1=input('Quer fazer novamente? s ou n '.lower())
    if var1 == 's':
        print('Reiniciando')
        media()
    if var1 == 'n':
        print('Até a proxima!')
        exit()
    else:
        denovo()
media()