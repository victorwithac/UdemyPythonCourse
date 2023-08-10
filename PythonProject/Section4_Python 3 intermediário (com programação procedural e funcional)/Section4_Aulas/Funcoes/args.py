# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# print(soma(1, 2, 3, 4, 5, 6))
# numeros = 9, 8, 7, 6, 5, 4
# outra_soma = soma(*numeros)
# print(outra_soma)
# print(*numeros)

# soma1 = 1, 2, 3, 4, 5, 6
# soma(soma1)

def function(*args):
    total = 0
    # print(*args)
    for numero in args:
        # print(numero, end=' ')

        total += numero
    return total
# o retorno da função está dentro da variável
armazenamento = function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(armazenamento)



