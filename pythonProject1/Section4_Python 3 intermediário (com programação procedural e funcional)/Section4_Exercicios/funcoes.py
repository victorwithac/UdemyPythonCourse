# Exercício 1
# def multiplicar(*args):
#     total = 1
#     for c in args:
#         total = total * c
#     return total
# retorno = multiplicar(5, 2, 2, 2, 2)
# print(retorno)

#Exercício 2

def par_ou_impar(x):
    if x % 2 == 0:
        return 'É par'
    return 'É ímpar'

numero = int(input('Digite um número: '))
print(par_ou_impar(numero))

