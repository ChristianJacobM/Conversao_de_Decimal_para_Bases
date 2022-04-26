print('Programa para Conversão de Bases')
num= int(input("Digite um numero para a conversão que seja inteiro:"))
print('''Escolha uma das bases para esta conversão:
[1] Conversão para Binário.
[2] Conversão para Hexadecimal.
[3] Conversão para Octadecimal.''')
opção= int(input('Qual a sua opção:'))
if opção == 1:
    print('{} A conversão de decimal para binário é {}'.format(num, bin(num)))
elif opção == 2 :
    print('{} A conversão de decimal para hexadecimal é {}'.format(num, hex(num)))
elif opção == 3:
    print('{} A conversão de decimal para octadecimal é {}'.format(num, oct(num)))