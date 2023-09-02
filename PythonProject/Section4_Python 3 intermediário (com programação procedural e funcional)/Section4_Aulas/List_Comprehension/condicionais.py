numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novos_numeros = [numero for numero in numeros if numero > 5]
# print(novos_numeros)
impares = [numero for numero in numeros if numero % 2 != 0]
# print(impares)
pares = [numero for numero in numeros if numero % 2 == 0]
# print(pares)
outros_if = [
    numero
    if numero != 6 else 600
    for numero in pares
]
print(outros_if)

