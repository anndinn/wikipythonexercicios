print('Faça um Programa que verifique se uma letra digitada é vogal ou consoante.')
def fun1():
    va1=input('Digite uma letra: ')
    vogal =['a','e','i','o','u']
    if va1 in vogal:
        print('Vogal')
    else:
        print('Consoante')
    novo()
def novo():
    new=input('Quer fazer novamente: s ou n ')
    if new == 's':
        fun1()
    if new =='n':
        print('Bye bye')
        exit()
    else:
        novo()
fun1()