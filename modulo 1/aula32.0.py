#exercicio 2

horas = int(input('Que horas são?: '))

if horas >= 0 and horas <= 11:
    print('Bom dia')

elif horas >= 12 and horas <= 17:
    print('Boa tarde')

elif horas >= 18 and horas <= 23:
    print('Boa noite')

#EXEMPLO:
# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')    