#List Comprehension em Python
#List Comprehension é uma forma para criar listas
# a partir de iteráveis.

# lista = list(range(10))
# print(lista)

lista = []
for numero in range(11):
    lista.append(numero)
# print(lista)

lista = [numero + 1 for numero in range(10)]
print(lista)

