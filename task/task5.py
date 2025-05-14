"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('digitar um número inteiro: ')  

try:
    num_int = int(entrada)

    if num_int % 2 == 0: 
        print(f'O número {entrada} é par! ') 

    else :
        print(f'o número {entrada} é impar! ')

except: 
    print('Vc não digitou um numero inteiro')

# entrada = input('digitar um número inteiro: ')  

# if entrada.isdigit() is True:
#     entrada = int(entrada)
#     if entrada % 2 == 0: 
#         print(f'O número {entrada} é par! ') 

#     else :
#         print(f'o número {entrada} é impar! ')

# else: 
#     print('Vc não digitou um numero inteiro')