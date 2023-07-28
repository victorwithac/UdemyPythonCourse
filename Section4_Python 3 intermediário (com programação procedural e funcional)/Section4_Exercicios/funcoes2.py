#EXERCÍCIO

# def duplicar(numero):
#     return numero * 2
# def triplicar(numero):
#     return numero * 3
# def quadriplicar(numero):
#     return numero * 4
#
# print(duplicar(5))
# print(triplicar(5))
# print(quadriplicar(5))

def operacao(multiplicar):
    def operar(numero):
        return numero * multiplicar
    return operar

duplicar = operacao(2)
triplicar = operacao(3)
quadruplicar = operacao(4)

print(duplicar(10))
print(triplicar(5))
print(quadruplicar(20))
