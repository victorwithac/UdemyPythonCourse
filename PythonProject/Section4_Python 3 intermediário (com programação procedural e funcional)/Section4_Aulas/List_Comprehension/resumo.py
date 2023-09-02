#sintaxe

# numeros = [1, 2, 3, 4, 5]
# novos_numeros = numeros
# numeros = [6, 7, 8, 9]
# # print(novos_numeros)
# novos_numeros[0] = 20
# # print(numeros)
# # numeros = [9, 8, 7, 6]
# # print(novos_numeros)
# print(numeros)

# numeros = [1, 2, 3, 4, 5]
# novos_numeros = [numero for numero in numeros]

# # novos_numeros = []
# # for numero in numeros:
# #     novos_numeros.append(numero)
#
# numeros[0] = 20
# print(novos_numeros)
#

def division(x, y):
    return x / y
def multiplication(x, y):
    return x * y
def sum(x, y):
    return x + y
def subtraction(x, y):
    return x - y

# print(division(10, 2))
# print(multiplication(10, 2))
# print(sum(10, 2))
# print(subtraction(10, 2))


numeros = [10, 20, 30, 40, 50]
entrada = int(input('Digite um número: '))

division = [division(entrada, numero) for numero in numeros]
multiplication = [multiplication(entrada, numero) for numero in numeros]
sum = [sum(entrada, numero) for numero in numeros]
subtraction = [subtraction(entrada, numero) for numero in numeros]

print(division)
print(multiplication)
print(sum)
print(subtraction)
