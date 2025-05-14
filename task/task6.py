"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input ('Que horas são: ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 18:
        print('Boa tarde')
    elif hora >=19 and hora <= 24:
        print('Boa noite')
    else:
        print('Não conheco essa hora')

except:
    print('Vc não digitou um hórario')