import pprint
# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))
# lista = [
#     (x, y, z)
#     for x in range(3)
#     for y in range(3)
#     for z in range(3)
# ]

lista = [
    [letra for letra in 'Victor']
    for x in range(4)

]




pprint.pprint(lista)
