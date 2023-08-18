# pessoa = {
#     'nome': 'Victor',
#     'sobrenome': 'Marques',
#     'idade': 18,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
#
# }
#
# print(pessoa['endereços'])

pessoas = {'alguma coisa':
    [
    {'nome': ['João', 'Maria', 'Marcos', 'Lucas'],},
    {'sobrenome': ['Oliveira', 'Santos', 'Marques', 'Silva'],}
]

}

# print(pessoas['nome'][2])
# print(pessoas['sobrenome'][2])

print(pessoas['alguma coisa'][0]['nome'][1])
print(pessoas['alguma coisa'][1]['sobrenome'][1])
del pessoas['alguma coisa'][1]['sobrenome'][1]
print(pessoas)

# dicionario > chave > lista > 2 dicionarios

# for chave in pessoas:
#     print(chave, pessoas[chave][1])