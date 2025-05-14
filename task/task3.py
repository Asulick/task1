primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

condicao1 = int( primeiro_valor ) >= int ( segundo_valor)

if condicao1:
    print(f'primeiro valor, {primeiro_valor} maior ou igual que o segundo {segundo_valor}' )
else:
    print(f'segundo valor, {segundo_valor} maior ou igual que o primeiro, {primeiro_valor}' )
